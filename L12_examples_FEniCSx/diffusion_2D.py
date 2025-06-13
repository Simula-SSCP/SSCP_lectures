import ufl
from ufl import TestFunction, TrialFunction, dot, grad, dx

from dolfinx.mesh import create_unit_square, CellType
from dolfinx.fem import Constant, functionspace, Function, locate_dofs_geometrical, dirichletbc
from dolfinx.fem.petsc import LinearProblem

from mpi4py import MPI
import matplotlib.pyplot as plt
import numpy as np
import pyvista

# Unit square mesh
mesh = create_unit_square(comm=MPI.COMM_WORLD, nx=20, ny=20, cell_type=CellType.triangle)
# Lagrange (CG1) function space
W = functionspace(mesh, ("Lagrange", 1))

# Constant kappa
kappa = Constant(mesh, 1.0)
# Constant source term
S = Constant(mesh, 0.0)

# Variational formulation
v = TestFunction(W)  # the test function
u = TrialFunction(W)  # the unknown

a = kappa * dot(grad(u), grad(v)) * dx  # left hand side of our equation
L = S * v * dx  # right hand side of our equation

# Dirichlet boundary conditions
value_left = Constant(mesh, 0.0)
value_right = Constant(mesh, 2.0)

dofs_left = locate_dofs_geometrical(W, lambda x: np.isclose(x[0], 0))
bc_left = dirichletbc(value_left, dofs_left, W)

dofs_right = locate_dofs_geometrical(W, lambda x: np.isclose(x[0], 1))
bc_right = dirichletbc(value_right, dofs_right, W)

bcs = [bc_left, bc_right]

# Solve
problem = LinearProblem(a, L, bcs=bcs, petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
uh = problem.solve()

# Plot - pyvista
from dolfinx import plot

pyvista.start_xvfb()
# Create the grid to plot the mesh
mesh.topology.create_connectivity(2, 2)
topology, cell_types, geometry = plot.vtk_mesh(mesh, 2)
u_grid = pyvista.UnstructuredGrid(topology, cell_types, geometry)
# Plot solution on the mesh
u_grid.point_data["u"] = uh.x.array
u_grid.set_active_scalars("u")
u_plotter = pyvista.Plotter()
u_plotter.add_mesh(u_grid, show_edges=True)
u_plotter.view_xy()
u_plotter.save_graphic('diffusion_2D.pdf')
