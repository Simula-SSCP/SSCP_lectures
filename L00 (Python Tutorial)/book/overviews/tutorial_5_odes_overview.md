# Solving ODEs numerically

At the core of computational physiology lies the mathematical modeling of biological systems changing over time. These models are almost exclusively built using ordinary differential equations (ODEs).

While some simple ODEs can be solved analytically with pen and paper, the vast majority of real-world biological models are far too complex for exact solutions. Instead, we must rely on computers to approximate the solutions numerically.

In this chapter, we will show you how to solve an ODE in Python. We will start by manually building a simple numerical solver using a `for` loop and the Forward Euler method. Then, we will introduce `scipy.integrate.solve_ivp`, a powerful, professionally optimized solver from the SciPy library that we will rely on heavily throughout this course.
