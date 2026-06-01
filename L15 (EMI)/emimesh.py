import dolfinx
import gmsh
from mpi4py import MPI

scale = 1e-4
pad = 8.0 * scale
L_O, W_O, H_O = 100.0 * scale, 12.0 * scale, 12.0 * scale
L_WE, W_WE_y, W_WE_z = 4.0 * scale, 8.0 * scale, 8.0 * scale
#L_SN, W_SN_x, W_SN_z = 4.0 * scale, 60.0 * scale, 8.0 * scale
#L_UD, W_UD_x, W_UD_y = 4.0 * scale, 60.0 * scale, 8.0 * scale

step_x = L_O + 2 * L_WE
step_y = 0 #W_O + 2 * L_SN
step_z = 0 #H_O + 2 * L_UD

def generate_emi_mesh(N_cells=(8, 1, 1), mesh_res=0.001, outfile=None):

    dim = len(N_cells)
    nx, ny, nz = N_cells[0], N_cells[1], N_cells[2]

    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    gmsh.model.add(f"emi_cells")

    min_x, min_y, min_z = -pad, -pad, -pad
    ext_box = gmsh.model.occ.addBox(
        min_x,
        min_y,
        min_z,
        nx * step_x + 2 * pad,
        ny * step_y + 2 * pad,
        nz * step_z + 2 * pad,
    )

    cell_vols = []
    for i in range(nx):
        cx = i * step_x + step_x / 2.0
        cy, cz = step_y / 2.0, step_z / 2.0
        parts = [
            gmsh.model.occ.addBox(cx - L_O / 2, cy - W_O / 2, cz - H_O / 2, L_O, W_O, H_O),
            gmsh.model.occ.addBox(cx - L_O / 2 - L_WE, cy - W_WE_y / 2, cz - W_WE_z / 2, L_WE, W_WE_y, W_WE_z),
            gmsh.model.occ.addBox(cx + L_O / 2, cy - W_WE_y / 2, cz - W_WE_z / 2, L_WE, W_WE_y, W_WE_z),
            #gmsh.model.occ.addBox(cx - W_SN_x / 2, cy - W_O / 2 - L_SN, cz - W_SN_z / 2, W_SN_x, L_SN, W_SN_z),
            #gmsh.model.occ.addBox(cx - W_SN_x / 2, cy + W_O / 2, cz - W_SN_z / 2, W_SN_x, L_SN, W_SN_z),
            #gmsh.model.occ.addBox(cx - W_UD_x / 2, cy - W_UD_y / 2, cz - H_O / 2 - L_UD, W_UD_x, W_UD_y, L_UD),
            #gmsh.model.occ.addBox(cx - W_UD_x / 2, cy - W_UD_y / 2, cz + H_O / 2, W_UD_x, W_UD_y, L_UD),
        ]
        fused, _ = gmsh.model.occ.fuse([(3, parts[0])], [(3, p) for p in parts[1:]])
        cell_vols.append(fused[0][1])

    ext_space, _ = gmsh.model.occ.cut([(dim, ext_box)], [(dim, c) for c in cell_vols], removeTool=False)
    out, out_map = gmsh.model.occ.fragment(ext_space, [(dim, c) for c in cell_vols])
    gmsh.model.occ.synchronize()

    # Tag extracellular space as 1
    extracellular_tags = [tag for i in range(len(ext_space)) for d, tag in out_map[i]]
    gmsh.model.addPhysicalGroup(dim, extracellular_tags, 1)

    # Iteratively tag each cell with unique markers (2, 3, 4...)
    all_intra_tags = []
    for i in range(len(cell_vols)):
        cell_tags = [tag for d, tag in out_map[len(ext_space) + i]]
        all_intra_tags.extend(cell_tags)
        gmsh.model.addPhysicalGroup(dim, cell_tags, 2 + i)

    ext_faces = set([t for d, t in gmsh.model.getBoundary([(dim, t) for t in extracellular_tags], oriented=False)])
    intra_bndry = gmsh.model.getBoundary([(dim, t) for t in all_intra_tags], oriented=True, combined=False)

    from collections import Counter
    face_counts = Counter([abs(t) for d, t in intra_bndry])
    gap_faces = [face for face, count in face_counts.items() if count == 2]
    mem_faces = ext_faces.intersection(set([face for face, count in face_counts.items() if count == 1]))

    if mem_faces:
        gmsh.model.addPhysicalGroup(dim - 1, list(mem_faces), 4)
    if gap_faces:
        gmsh.model.addPhysicalGroup(dim - 1, list(gap_faces), 5)

    gmsh.option.setNumber("Mesh.MeshSizeMax", mesh_res)
    gmsh.model.mesh.generate(dim)

    mesh_data = dolfinx.io.gmsh.model_to_mesh(gmsh.model, MPI.COMM_WORLD, 0, gdim=dim)
    gmsh.finalize()
    
    return mesh_data.mesh, mesh_data.cell_tags, mesh_data.facet_tags
