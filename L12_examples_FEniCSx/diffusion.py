import ufl
from ufl import TestFunction, TrialFunction, dot, grad, dx

from dolfinx.mesh import create_interval
from dolfinx.fem import Constant, functionspace, Function, locate_dofs_geometrical, dirichletbc
from dolfinx.fem.petsc import LinearProblem

from mpi4py import MPI
import matplotlib.pyplot as plt
import numpy as np

plot_name = "diffusion_1D.png"
#### Introduced cases ###
noncst_kappa = False
noncst_source = True

# Interval mesh
mesh = create_interval(comm=MPI.COMM_WORLD, nx=20, points=(0, 1))
# Lagrange (CG1) function space
W = functionspace(mesh, ("Lagrange", 1))

# kappa
if (noncst_kappa):
    # Non-constant kappa
    kappa_space = functionspace(mesh, ("DG", 0))
    kappa = Function(kappa_space)
    kappa.x.array[:] = 0.1
    kappa.x.array[9] = 1
    print("kappa = ", kappa.x.array)
    plot_name = "diffusion_1D_noncst_kappa.png"
else:
    kappa = Constant(mesh, 1.0)

# Source term
if (noncst_source):
    # Non-constant source term
    S_space = functionspace(mesh, ("DG", 0))
    S = Function(S_space)
    S.x.array[:] = 0  # set all the vector entries to 1.0
    S.x.array[9] = 20  # set the 10th entry to 20.0
    S.x.array[15] = -20  # set the 16th entry to -20.0
    print(S.x.array)
    plot_name = "diffusion_1D_noncst_source.png"
else:
    S = Constant(mesh, 0.0)

# Variational formulation
v = TestFunction(W)  # the test function
u = TrialFunction(W)  # the unknown

a = kappa * dot(grad(u), grad(v)) * dx  # left hand side of our equation
L = S * v * dx  # right hand side of our equation

# Dirichlet boundary conditions
value_left = Constant(mesh, 0.0)
if (noncst_source):
    value_right = Constant(mesh, 0.0)
else:
    value_right = Constant(mesh, 2.0)

dofs_left = locate_dofs_geometrical(W, lambda x: np.isclose(x[0], 0))
bc_left = dirichletbc(value_left, dofs_left, W)

dofs_right = locate_dofs_geometrical(W, lambda x: np.isclose(x[0], 1))
bc_right = dirichletbc(value_right, dofs_right, W)

bcs = [bc_left, bc_right]

# Solve
problem = LinearProblem(a, L, bcs=bcs, petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
uh = problem.solve()

# Plot
dof_coords = W.tabulate_dof_coordinates()[:, 0]
plt.plot(dof_coords, uh.x.array)
plt.savefig(plot_name)
