# Thermodynamics and Gibbs free energy

When analyzing or modeling any reaction or process occurring within the cell, it can be very useful to go back to the basics and consider the underlying physical constraints present. To do this, we typically want to analyze the _thermodynamic quantities_ of a system, namely energy and _entropy_. Such analysis can give us a better understanding of what processes will occur spontaneously, how close they are to equilibrium, and other physical limits. A very useful concept here is called _Gibbs free energy_, which combines energy and entropy into a single quantity.

Let us very briefly cover the fundamental laws of thermodynamics, then explain what Gibbs free energy is and how we can use it.

## First law of thermodynamics

> Energy cannot be created or destroyed.

The first law is a statement about the conservation of energy. The total energy of any _isolated_ system will always be constant over time. A part of the cell, or a reacting molecule within the cell, however, is not isolated and can exchange energy with its environment through either heat exchange or mechanical work.

## Second law of thermodynamics

> In any spontaneous process, the total net entropy can never decrease, only increase.

The second law of thermodynamics is conceptually much trickier than the first, and it can be stated in many different, functionally equivalent ways.

Put simply, entropy is a measure of a system's _disorder_, and it is a physical property much like energy. Like energy, the entropy of the reactants in a process does not necessarily have to increase—they _can_ decrease—but the net entropy of the reactants and their environment combined can only increase. Because of this, the entropy of any isolated system will tend to grow over time and evolve towards some maximum possible entropy. This maximum will correspond to the system's thermodynamic equilibrium state. Put another way, we can say that entropy is the driving force of chemical reactions and other cellular processes.

## Gibbs free energy (energy + entropy combined)

The first and second laws of thermodynamics describe physical properties of how nature works; they must always be fulfilled. Since the two regard different physical properties, however, including both in any given analysis can be nontrivial. To make this easier, we combine the two quantities into a single quantity called the _Gibbs free energy_, or simply the _Gibbs energy_ of the system. It can be expressed as:

```{math}
:label: eq:gibbs_def
G = U + pV - TS
```

Here, $G$ is the Gibbs energy of the system, while $U$, $V$, and $S$ are the system's internal energy, volume, and entropy, respectively. Lastly, we have the pressure, $p$, and temperature, $T$, of the surrounding environment.

From this definition, $G$ will have units of energy, which is why we call it Gibbs _energy_, but note that entropy is also baked into this definition. With the introduction of Gibbs energy, we can restate the second law of thermodynamics not in terms of entropy, but in terms of Gibbs energy: The net Gibbs energy of any isolated system cannot increase, but only decrease. An isolated system will spontaneously tend towards its minimal Gibbs energy, which will then correspond to its thermodynamic equilibrium.

## Why is it called Gibbs _free_ energy?

Gibbs energy is known by many names, but many like to use the descriptor _free_ energy. When J. W. Gibbs introduced the concept in the 1870s, he dubbed it simply _available energy_. This is because the Gibbs energy can be thought of as the maximum amount of work that can be extracted as useful work from a given system. It would be impossible to extract more without breaking the two laws of thermodynamics.

A good metaphor for Gibbs energy is found in Schroeder's _An Introduction to Thermal Physics_. Schroeder asks you to imagine a wizard conjuring up a rabbit from nothing. Obviously, the wizard has to respect the laws of thermodynamics, which state that energy cannot be created, and so he will have to supply the needed energy in the process. But how much energy would the wizard need to supply to create the rabbit?

First, he has to produce the internal energy of the rabbit itself, $U$, which encompasses all the mass energy and all internal chemical energy. If the rabbit were to be created in a complete vacuum, this would be the end of it. However, to get the rabbit to pop into existence in front of you, the wizard actually has to make space for the rabbit by pushing some air aside, which costs mechanical energy. This cost would be $pV$; the higher the air pressure or the bigger the rabbit, the more work has to be performed. The energy bill is now $U + pV$.

However, the wizard is quite clever, and so he can save some energy as well. If he conjures up a cold rabbit, he knows the laws of thermodynamics state that heat will spontaneously flow from the high-temperature surroundings into the low-temperature rabbit, so the wizard can subtract this energy from his energy bill. This contribution is $TS$, where $T$ is the temperature of the surroundings and $S$ is the entropy of the rabbit. Why does the entropy enter into it? Because temperature is defined as the derivative $T = {\rm d}U/{\rm d}S$. So the more entropy the rabbit has, the more thermal energy it will absorb from its environment. The total energy bill the wizard needs to pay is therefore the Gibbs energy: $U + pV - TS$.

```{figure} ../../fig/gibbs_rabbit.png
---
width: 400px
name: fig_gibbs_rabbit
---
Schroeder introduces a metaphor to explain the concept of Gibbs free energy. Envision a wizard conjuring a rabbit out of nothing. He would need to supply a total amount of energy equal to $G = U + pV - TS$.
```

Schroeder's analogy nicely illustrates how Gibbs energy combines different thermodynamic considerations into a single quantity. But if the Gibbs energy represents a _cost_, why is it called the _free_ energy? The name describes the reverse process. If an evil wizard were to annihilate a rabbit and extract as much energy as possible in the process, they would first get the internal energy $U$ and some extra mechanical work from the surrounding air collapsing into the resulting vacuum. However, they would have to dump some of that energy as heat into the environment to satisfy the second law. The Gibbs energy is thus the amount of energy a system could release if it were to cease existing.

Of course, in the real world, a system doesn't simply cease existing in this manner. However, any reaction or process can be thought of as one system being annihilated and a new one being created. It is the _net change_ in the Gibbs energy that is the important quantity.

## Change in Gibbs energy

In a given reaction, the energy, volume, or entropy of the system can change. Any change in the pressure or temperature, however, can be neglected because we assume the surrounding environment to be much larger than the reacting system. Thus, the total change in Gibbs energy can generally be written out as:

```{math}
:label: eq:gibbs_change
\Delta G = \Delta U + p\Delta V - T\Delta S
```

Thus, the net change in Gibbs energy will be a weighted sum of its change in internal energy ($\Delta U$), its change in volume ($\Delta V$), or a change in net entropy ($\Delta S$).

Recall now that the net Gibbs energy of any system will tend to spontaneously decrease over time. So we can now state the following for any reaction or process:

- If $\Delta G < 0$, it can occur spontaneously.
- If $\Delta G > 0$, it cannot happen (as this would break the first and/or second law).
- If $\Delta G = 0$, the system is at thermodynamic equilibrium.

Note that when we say any process where $\Delta G > 0$ cannot happen, we mean this for an isolated system. In certain reactions in the cell, one process with a $\Delta G > 0$ is _coupled_ to another with $\Delta G < 0$. As long as the _net_ change is negative, this is fine, as one process is used to power another.

### Gibbs energy of molecular species

For any molecular species, we can express its Gibbs free energy as:

```{math}
:label: eq:gibbs_species
G = G^0 + RT \ln c
```

Here, the first term, $G^0$, is called the standard free energy, which is dependent on what chemical species is being discussed, but independent of the concentrations involved. The second term is dependent on the concentration of the species, but is otherwise independent of what the actual species is. Here, $R$ is the ideal gas constant, $T$ the temperature, and $c$ the concentration of the species.

If a reaction occurs where A $\rightarrow$ B, the net change in Gibbs energy will then be expressed as:

```{math}
:label: eq:gibbs_reaction_full
\Delta G = G_{\rm B} - G_{\rm A} = (G_{\rm B}^0 - G_{\rm A}^0) + RT (\ln c_{\rm B} - \ln c_{\rm A})
```

Which simplifies to:

```{math}
:label: eq:gibbs_reaction_simplified
\Delta G = \Delta G^0 + RT \ln \frac{c_{\rm B}}{c_{\rm A}}
```

Note that the change in Gibbs energy can be written as two terms. The first is the change in standard free energy, which depends on what molecular species are interacting. This value is tabulated for most molecular species under standard conditions. The second term only cares about the ratio of the concentrations of the species, and so is not specific to what reaction is occurring.

### Chemical equilibrium from Gibbs energy

As stated, a system is in equilibrium with respect to a given reaction if the net change in Gibbs energy for that reaction is equal to zero. If a system can inhabit two given states, A and B, then we know that at thermodynamic equilibrium we have:

```{math}
:label: eq:gibbs_equilibrium
\Delta G = \Delta G^0 + RT \ln \frac{c_{\rm B}}{c_{\rm A}} = 0
```

If we take the exponential of this expression, we find:

```{math}
:label: eq:gibbs_ratio
\frac{c_{\rm B}}{c_{\rm A}} = e^{-\Delta G^0/RT}
```

The left-hand side is now the ratio of the two concentrations, while the right-hand side contains all constants. While this equilibrium condition looks very different from the one we derived when discussing the law of mass action, it effectively states the exact same thing. This also implies, perhaps not surprisingly, that the standard free energy $\Delta G^0$ for a given reaction is directly related to its dissociation constant $K_{\rm d}$.
