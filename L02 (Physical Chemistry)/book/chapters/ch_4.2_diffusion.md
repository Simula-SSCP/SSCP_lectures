# Diffusion and Fick's law

The next physical principle that is useful to know about is _diffusion_. This is the process where concentration differences tend to smooth out over time. If a system has a non-uniform concentration of a given ion or molecule, then random thermal motion will tend to erase these differences over time. At the macroscopic level, this will look like there is a net _diffusive flux_ of mass going against the concentration gradient.

```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/DiffusionMicroMacro.gif/250px-DiffusionMicroMacro.gif
---
width: 250px
name: fig_diffusion_gif
---
A simple illustration of diffusion at the microscopic and macroscopic level. The top panel shows the thermal motion of a single particle; it is chaotic, random, and essentially uniform in space. In the middle panel, we see the motion of many such particles simultaneously. Because the initial distribution has more particles on the left than the right, more particles will tend to move right—even if they are all moving at random. In the bottom panel, we get the macroscopic view, where the concentration evens out over time, quickly at first, then slower and slower. Image from Wikimedia Commons.
```

To describe diffusion (at the macroscopic level) mathematically, we use Fick's law of diffusion (or Fick's _first_ law of diffusion, as it is sometimes called). This law states that the _net_ diffusive flux is proportional to the concentration gradient. In 1D, it can be expressed as:

```{math}
:label: eq:ficks_law_1d
J(x) = -D \frac{\partial c(x)}{\partial x}
```

While in higher dimensions we would state it in vector form as:

```{math}
:label: eq:ficks_law_vector
\vec{J}(\vec{r}) = -D \nabla c(\vec{r})
```

Here, $J$ is the net diffusive flux, $c$ is the concentration, and $D$ is the proportionality constant, called the _diffusivity_ or _diffusion coefficient_. Note that while both $J$ and $c$ are field variables, meaning they have different values in different locations $\vec{r}$, we will from now on forgo writing their spatial arguments to get a neater notation. They are, however, always spatially dependent.

Note that Fick's law holds true for each ionic or molecular species independently, so it is often written with a sub-index denoting specific species, generally as:

```{math}
:label: eq:ficks_law_species
\vec{J}_k = -D_k \nabla c_k
```

where $k$ denotes the species. Note that the diffusivity is also species-dependent.

Fick's law tells us that diffusion will spontaneously even out concentration differences. The bigger the differences present, the stronger the diffusive flux we will have. In the upcoming chapters, we will start looking at the transport of ions across the cell membrane, and this transport is in large part driven by precisely such _diffusive flux_ because there are significant differences in ion concentrations inside and outside the cell.
