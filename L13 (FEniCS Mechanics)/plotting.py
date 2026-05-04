import pyvista as pv
import numpy as np
import ufl
from dolfinx import plot, fem


def setup_gif_visualizer(mesh, u, filename="deformation.gif", fps=3, clim=[0, 0.5]):
    """Initializes the PyVista plotter with an undeformed reference frame."""
    plotter = pv.Plotter(off_screen=True)
    plotter.open_gif(filename, fps=fps)

    # 1. Create the base PyVista grid
    topology, cells, geometry = plot.vtk_mesh(u.function_space)
    grid = pv.UnstructuredGrid(topology, cells, geometry)
    plotter.add_axes(line_width=3, labels_off=False)

    # Add the original mesh as a static wireframe outline
    plotter.add_mesh(grid, style="wireframe", color="black")

    # 2. Setup displacement vectors
    u_dim = len(u)
    values = np.zeros((geometry.shape[0], 3))
    values[:, :u_dim] = u.x.array.reshape(geometry.shape[0], u_dim)
    grid["u"] = values
    grid.set_active_vectors("u")

    # 3. Setup magnitude expression (for coloring)
    degree = u.function_space.ufl_element().degree
    Vs = fem.functionspace(mesh, ("CG", degree))
    magnitude = fem.Function(Vs)
    us_expr = fem.Expression(ufl.sqrt(ufl.inner(u, u)), Vs.element.interpolation_points)
    magnitude.interpolate(us_expr)

    # 4. Create the dynamically warping mesh
    warped = grid.warp_by_vector("u", factor=1.0)
    warped.set_active_vectors("u")
    warped["Displacement Magnitude"] = magnitude.x.array

    # 5. Add the deformed mesh to the plotter
    # Adjust clim based on expected maximum displacement
    actor = plotter.add_mesh(
        warped,
        scalars="Displacement Magnitude",
        show_edges=True,
        clim=clim,
        cmap="viridis",
    )
    plotter.camera.zoom(0.8)
    return plotter, grid, magnitude, us_expr, actor


def update_gif_frame(plotter, grid, u, magnitude, us_expr, actor):
    """Updates the grid data, re-warps, and writes a frame."""
    # 1. Update displacement vectors and magnitude
    grid["u"][:, : len(u)] = u.x.array.reshape(grid.points.shape[0], len(u))
    magnitude.interpolate(us_expr)

    # 2. Create newly warped mesh and update scalars
    warped = grid.warp_by_vector("u", factor=1.0)
    warped.point_data["Displacement Magnitude"] = magnitude.x.array
    warped.set_active_scalars("Displacement Magnitude")

    # 3. Copy new geometry and data to existing actor and write frame
    actor.mapper.dataset.copy_from(warped)
    plotter.write_frame()


def plot_fibers(domain, fiber_funcs, names, colors, arrow_scale=1.0):
    """
    Plots fiber directions as arrows using PyVista.

    Args:
        domain: The dolfinx mesh.
        fiber_funcs: List of fem.Function objects (e.g., [f0, s0, n0]).
        names: List of string names for the vectors.
        colors: List of PyVista compatible colors (e.g., ['red', 'green', 'blue']).
        arrow_scale: Float to adjust the physical size of the arrows.
    """
    plotter = pv.Plotter(window_size=[1000, 300], shape=(1, len(fiber_funcs)))

    # Create a base grid for the domain mesh to plot as a reference
    topology, cells, geometry = plot.vtk_mesh(domain)
    base_grid = pv.UnstructuredGrid(topology, cells, geometry)

    # Create a PyVista grid for the fiber data
    topology_f, cells_f, geometry_f = plot.vtk_mesh(fiber_funcs[0].function_space)
    grid = pv.UnstructuredGrid(topology_f, cells_f, geometry_f)

    for func, name, color in zip(fiber_funcs, names, colors):
        plotter.subplot(0, names.index(name))

        # Attach vector data and generate glyphs
        grid[name] = func.x.array.reshape(-1, domain.geometry.dim)
        glyphs = grid.glyph(orient=name, factor=arrow_scale, geom=pv.Arrow())

        # Add to plotter
        plotter.add_mesh(base_grid, color="lightgray")
        plotter.add_mesh(glyphs, color=color, label=name)
        plotter.add_text(name, position="upper_edge", font_size=10, color=color)
        plotter.view_isometric()

    plotter.show()
