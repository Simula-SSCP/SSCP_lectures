# Reversible reactions and equilibrium

When formulating our model for the binding reaction, we made an implicit assumption that the _reverse_ reaction doesn't occur---that is, an oxymyoglobin splitting into an oxygen molecule and a myoglobin, a process we call _dissociation_. Many chemical reactions are reversible and will occur in both directions, especially in a closed system such as the inside of a cell. The binding and dissociation of oxygen will occur in parallel, and we therefore modify our chemical equation to reflect this:

```{math}
:label: eq:reversible_reaction
\mathrm{Mb} + \mathrm{O_2} \underset{k_-}{\overset{k_+}{\rightleftharpoons}} \mathrm{MbO_2}
```

Here we have replaced the unidirectional arrow with a bi-directional pair of arrows representing both the forward and reverse directions of the reaction. The two directions of a reaction do not necessarily have the same rate constant, so we denote the two separate rate constants $k_+$ and $k_-$ to tell them apart.

The rate of the forward reaction will be the same as before, and the rate of the reverse reaction can be formulated as:

```{math}
:label: eq:forward_reverse_rates
\begin{aligned}
\text{forward rate} &= k_+\mathrm{[Mb]}\mathrm{[O_2]}, \\
\text{reverse rate} &= k_-\mathrm{[MbO_2]}.
\end{aligned}
```

The rate is again found by assuming the rate is proportional to the reactant concentrations, and this holds true even if the reactant is a single molecule. This makes sense: any given oxymyoglobin molecule in the system will have a specific probability of dissociating at any given time, meaning the total number of molecules splitting apart per unit of time should be proportional to the total amount of oxymyoglobin (i.e., its concentration).

In an environment containing both oxygen and myoglobin, we now have a complex dynamic situation where myoglobin and oxygen are continuously binding together and dissociating. The _net_ change in concentrations over time can be found by looking at the difference between the forward and reverse rates. To formulate the change in oxymyoglobin over time, we use the following ODE:

```{math}
:label: eq:oxymyoglobin_ode
\frac{\mathrm{d[MbO}_2\mathrm{]}}{\mathrm{d}t} = k_+[\mathrm{Mb}][\mathrm{O_2}] - k_-[\mathrm{MbO_2}]
```

The first term corresponds to the forward rate and is positive because oxymyoglobin is formed when a binding reaction occurs. The second term is the reverse rate, which we subtract because oxymyoglobin is removed from the system when it dissociates.

## Chemical equilibrium

When modeling a unidirectional chemical reaction, the concentration of the reactants can only drop over time while the concentration of the product can only increase. When we look at a reversible reaction, however, the concentrations of the different molecules can both increase and decrease. Looking at the ODE we just formulated, we see that the concentration of oxymyoglobin increases if the forward rate is larger than the reverse rate, and decreases if the situation is flipped. As the concentration changes over time, these two rates will also change and approach each other until we end up in a chemical _equilibrium_.

An equilibrium is reached once the forward and reverse rates of the reaction are of equal magnitude and effectively cancel each other out. We can write this as the following equilibrium criteria:

```{math}
:label: eq:equilibrium_criteria
\frac{\mathrm{d[MbO}_2\mathrm{]}}{\mathrm{d} t} = k_+[\mathrm{Mb}][\mathrm{O_2}] - k_-[\mathrm{MbO_2}] = 0 \quad (\text{at equilibrium})
```

This criteria does not say that the reaction has stopped, but rather that the forward and reverse reactions are now occurring at the exact same rate, meaning there is no _net_ change in concentrations. This is referred to as a _dynamic_ equilibrium, to emphasize that the reaction is still continuously occurring at the molecular level.

The equilibrium condition states that the two rates are equal:

```{math}
:label: eq:equilibrium_equality
k_+[\mathrm{Mb}][\mathrm{O_2}] = k_-[\mathrm{MbO_2}] \quad (\text{at equilibrium})
```

From this criteria, we can see that the _ratio_ of the reactants and the product must be constant at equilibrium:

```{math}
:label: eq:equilibrium_constant
\frac{[\mathrm{Mb}][\mathrm{O_2}]}{[\mathrm{MbO_2}]} = \frac{k_-}{k_+} \equiv K_{\rm d} \quad (\text{at equilibrium})
```

The ratio of the rate constants is typically referred to as the _dissociation constant_ of the reaction, and it is denoted $K_{\rm d}$. The higher the dissociation constant, the higher the concentrations of the free molecules will tend to be at equilibrium. Some refer to the dissociation constant simply as the _equilibrium_ constant, $K_{\rm eq}$. Note, however, that the term "equilibrium" doesn't indicate which direction of the reaction we are referring to, so this term could also mean the inverse relation $k_+/k_-$, which would be the _association_ constant. There are no strict conventions on which of these are used, and some care should be taken to interpret how the equilibrium constant for a reaction is formulated and used.

This equation is referred to as _the equilibrium equation_ or _the equilibrium condition_, and it describes how the ratio of concentrations will settle at equilibrium. It is a direct consequence of the law of mass action. If someone refers to the law of mass action as a single equation, it is typically this equilibrium equation they mean. Note that the equilibrium equation does not hold at all times, but only when a system is actually at equilibrium. However, any chemical system will spontaneously tend towards this state, and for many reactions, this occurs so swiftly that one can consider the system to always be at equilibrium for all practical purposes (typically called a _quasistatic_ process).

The equilibrium equation is very useful, but it might be a bit challenging to see how it is interpreted or used in practice. We will shortly look at an illustrative example, but first, let us take the time to solve the system of ODEs for the reversible reaction.

In the next section, you will computationally model this reversible reaction to verify that the system does indeed tend towards equilibrium.
