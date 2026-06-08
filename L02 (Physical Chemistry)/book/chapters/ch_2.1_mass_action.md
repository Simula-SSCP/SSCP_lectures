# The law of mass action

We start with looking at how to model simple chemical reactions. To do this we will use the _law of mass action_, which is one of the most fundamental concepts in chemistry. Note however that the mathematical models we define here are more general than chemical reactions themselves, and can also be applied to other processes in the cell.

As an example, we want to look at a _binding reaction_, between oxygen (O$_2$) and myoglobin (Mb). Myoglobin is an oxygen-binding globular protein found in muscle cells. If an environment contains both free oxygen molecules and myoglobin, the two will spontaneously bind together to form an _oxymyoglobin_ complex (MbO$_2$).

```{figure} ../../fig/myoglobin_reaction.png
---
scale: 50%
name: fig_myoglobin_reaction
---
Myoglobin is a complex globular protein, but for our example, the only important thing is that it has an oxygen binding group at its center which can bind a single oxygen protein. Image adapted from <a href="https://en.wikipedia.org/wiki/File:PicketFenceGenericRevised.png">Wikimedia</a> and used under CC BY-SA 3.0.
```

This can be written as the reaction equation

```{math}
:label: eq:unidirectional_reaction
\mathrm{Mb} + \mathrm{O_2} \overset{k}{\longrightarrow} \mathrm{MbO_2}
```

This reaction occurs _spontaneously_ (i.e., on its own), but not _instantaneously_. Instead it will progress at a certain _rate_, and this is where the law of mass action comes in.

## What decides the rate of a reaction?

For a binding reaction to occur at all, the two reacting molecules need to be close enough to each other to interact. At the molecular level, the reactants are not stationary, but move around in a random and chaotic manner called thermal motion. Due to this motion, many meetings between the two reactants will occur. Not every such meeting will result in a binding. Some will, and some will not.

However, it is clear that the number of bindings that occur in _total_ should be proportional to the number of such meetings that occur. Because thermal motion is inherently random, it is very reasonable to assume that the number of meetings will be proportional to the _concentrations_ of the reactants. The more molecules you have available, the more meetings will occur. If we use square brackets to denote the concentrations of the reactants, we write:

```{math}
:label: eq:rate_proportionality
\text{rate} \propto [\mathrm{Mb}]\times[\mathrm{O_2}]
```

Thus, the _rate_ of the binding reaction is proportional to the product of the concentration of the reactants. If you are not familiar with it, the $\propto$ symbol means "proportional to". Instead of writing out the word "rate", we typically write it out as the derivative of the concentrations themselves. If the rate is high, concentrations will change quickly, meaning a high derivative:

```{math}
:label: eq:rate_derivative_proportionality
\frac{\mathrm{d[MbO_2]}}{\mathrm{d}t} \propto [\mathrm{Mb}]\times[\mathrm{O_2}]
```

If you found the whole explanation of thermal motion and molecular meetings to be confusing---ignore the finer details for now. The main point is that the rate of _any_ reaction is proportional to the concentrations of the reactants themselves. This is precisely what the law of mass action states.

## Writing out a set of differential equations

To find an actual equation we can solve, we need an actual equality, not just a proportionality. We therefore introduce the proportionality constant $k$, which is typically called the _rate constant_. Thus we have three equations:

```{math}
:label: eq:mass_action_odes
\frac{\mathrm{d[MbO_2]}}{\mathrm{d}t} = k\mathrm{[Mb][O_2]}, \qquad \frac{\mathrm{d [Mb]}}{\mathrm{d}t} = -k\mathrm{[Mb]}\mathrm{[O_2]}, \qquad \frac{\mathrm{d [O_2]}}{\mathrm{d}t} = -k\mathrm{[Mb]}\mathrm{[O_2]}
```

Note that we get three equations because we have three concentrations that are changing. If binding occurs, we get more oxymyoglobin, but less free oxygen and myoglobin. These three equations form a set of ordinary differential equations (ODEs) we can solve to find how the concentrations change over time. In the next section, we will work through a [practical example of solving these ODEs numerically using Python](ch2-example).

## The rate constant

While we call $k$ the rate _constant_, note that it might not necessarily be completely constant. It is related to the probability of a reaction occurring, and so will be different for different chemical reactions. It will also depend on environmental factors like pH, temperature, and pressure. If these factors change during a chemical reaction, the rate constant will also change. The term "constant" is meant in relation to _concentrations_, as the rate constant is independent of the concentrations themselves. As concentrations change, the _rate_ of the reaction will change, but the _rate constant_ will not.

Note also that while we state that the rate is proportional to the concentrations of the reactants, it is technically more accurate to say it is proportional to their _activities_. The activity of a given molecular species can be described as its _effective concentration_. In complex solutions that do not behave like _ideal solutions_ (where reactants are not entirely free to move around independently of each other), the activity is generally lower than the actual concentration. While this distinction is important in strict physical chemistry, using concentrations directly is a standard and practical approximation for the mathematical models we will build in this course.

<h3>Determining and scaling rate constants</h3>

To actually apply the law of mass action and model concentrations over time, we will need to know the rate constants of any applicable reaction. These should therefore be considered _model parameters_. Put very simply, rate constants must typically be found empirically, or they must be adjusted to make a given model fit empirical data. If we do not have our own empirical data available, we can often lean on published data for most known chemical reactions.

It is important to remember that rate constants depend heavily on temperature. Rate constants found under standard lab settings (around 20$^\circ$C) will need to be adjusted to be applicable in a physiological setting (around 37$^\circ$C). There are techniques for scaling rate constants in this way, typically done by using a temperature coefficient denoted $Q_{10}$, which indicates how much a given model parameter needs to be scaled. While we will skip the finer details of this scaling for now, you can [read more about the $Q_{10}$ temperature coefficient on Wikipedia](<https://en.wikipedia.org/wiki/Q10_(temperature_coefficient)>) if you are curious.

## Activation energy and the Arrhenius equation

To get a better understanding of why chemical reactions typically speed up with temperature, we can turn to the _Arrhenius equation_. This simple equation states that a reaction rate typically can be written out on the form:

```{math}
:label: eq:arrhenius
k = Ae^{-E_{\rm a}/RT}
```

Here $k$ is a rate constant, and $A$ is the pre-exponential factor, which depends on the specific reaction but is independent of temperature. In the exponential term, $E_{\rm a}$ represents the _activation energy_ of the reaction, $R$ is the ideal gas constant, and $T$ is the absolute temperature.

The activation energy $E_{\rm a}$ represents the energy the reactants need to overcome to actually react. They need enough energy to overcome a "barrier" and undergo a chemical shift to change their structures. The bigger the barrier, the harder it is to react, and the slower the rate of the reaction at the macroscopic level.

The Arrhenius equation tells us that the rate constant has an exponential dependence on temperature. As the temperature is lowered, the rate constant is dampened. Conversely, when the temperature increases, the thermal motion of the reactants is energized, making it easier for them to overcome the activation barrier and actually react.

```{figure} ../../fig/activation_barrier.png
---
scale: 50%
name: fig_activation_barrier
---
A sketch of a conceptual energy landscape of oxygen binding to myoglobin. To actually bind together the two reactants have to meet with enough energy to overcome their activation energy $E_{\rm a}$. The chance of this occurring increases with the temperature $T$ of the system, because the reactants will have more thermal energy.
```
