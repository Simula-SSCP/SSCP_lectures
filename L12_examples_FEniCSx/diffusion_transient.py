import ufl
from ufl import TestFunction, TrialFunction, dot, grad, dx

from dolfinx.mesh import create_interval
from dolfinx.fem import Constant, functionspace, Function, locate_dofs_geometrical, dirichletbc
from dolfinx.fem.petsc import LinearProblem

from mpi4py import MPI
import matplotlib.pyplot as plt
import numpy as np
import copy

plot_name = "diffusion_1D_transient.png"

# Interval mesh
mesh = create_interval(comm=MPI.COMM_WORLD, nx=20, points=(0, 1))
# Lagrange (CG1) function space
W = functionspace(mesh, ("Lagrange", 1))

# kappa
kappa = Constant(mesh, 1.0)
# Source term
S = Constant(mesh, 0.0)

# Time stepping
dt = 0.2
T = 2
time_steps = np.arange(0, T, dt)
time_steps = time_steps.round(decimals=2)

# Variational form including time derivative
v = TestFunction(W)  # the test function
u = TrialFunction(W)  # the unknown
uh_old = Function(W) # Solution at previous time step. Initialized to zero.

a = (u * v) / dt * dx + kappa * dot(grad(u), grad(v)) * \
    dx  # left hand side of our equation
L = (uh_old * v) / dt * dx + S * v * dx  # right hand side of our equation

# Dirichlet boundary conditions
value_left = Constant(mesh, 0.0)
value_right = Constant(mesh, 2.0)

dofs_left = locate_dofs_geometrical(W, lambda x: np.isclose(x[0], 0))
bc_left = dirichletbc(value_left, dofs_left, W)

dofs_right = locate_dofs_geometrical(W, lambda x: np.isclose(x[0], 1))
bc_right = dirichletbc(value_right, dofs_right, W)

bcs = [bc_left, bc_right]

fig, ax = plt.subplots()
dof_coords = W.tabulate_dof_coordinates()[:, 0]
for t in time_steps:
    problem = LinearProblem(a, L, bcs=bcs, petsc_options={"ksp_type": "preonly", "pc_type": "lu"})
    uh = problem.solve()
    ax.plot(dof_coords, uh.x.array)

    # update the old solution to the new one for next time step
    uh_old.x.array[:] = uh.x.array
    uh_old.x.scatter_forward()

ax.legend([f"t = {t}" for t in time_steps], ncols=2, loc='lower right')
print("steps = ", [f"t = {t}" for t in time_steps])
plt.savefig(plot_name)
