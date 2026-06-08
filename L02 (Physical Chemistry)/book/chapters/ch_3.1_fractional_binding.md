# Fractional binding

So far we have treated the binding reaction of myoglobin and oxygen to be occurring in a closed system, where the total concentration of all three species is constant over time. However, in a muscle cell, this might not actually be the most realistic assumption. Inside the cell, we can typically think of the total amount of _myoglobin_ as fixed, i.e.,

$$[\mathrm{Mb}]_{\rm tot} = [\mathrm{Mb}] + [\mathrm{MbO_2}] = \text{const.}$$

The total amount of oxygen in the cell, however, can change over time. Oxygen is supplied by the circulatory system and is free to diffuse into and out of the cell. When oxygen binds to myoglobin, the amount of free oxygen inside the cell will decrease, and so more oxygen will tend to spontaneously enter the cell. This means that the total amount of oxygen in the cell is _not_ constant. Instead, we can assume that it is the concentration of free oxygen, $[\mathrm{O_2}]$, that is constant within the cell—at least over shorter time scales.

We now introduce a new quantity, the _fractional degree of oxygenation_, i.e., the fraction of all myoglobin molecules that currently have oxygen bound to them. This corresponds to the following ratio:

```{math}
:label: eq:fractional_oxygenation_def
Y = \frac{[\text{bound Mb}]}{[\text{total Mb}]} = \frac{[\mathrm{MbO_2}]}{[\mathrm{Mb}] + [\mathrm{MbO_2}]}
```

We will now use the equilibrium equation to find an expression for $Y$ as a function of the free oxygen concentration. To simplify this derivation, we are only concerned with the fractional oxygenation at equilibrium. We start by solving the equilibrium equation for $[\mathrm{MbO_2}]$, giving:

```{math}
:label: eq:mb02_equilibrium
[\mathrm{MbO_2}] = K_{\rm d}^{-1}[\mathrm{Mb}][\mathrm{O_2}]
```

We can now insert this into our expression for $Y$, yielding:

```{math}
:label: eq:y_substituted
Y = \frac{K_{\rm d}^{-1}[\mathrm{Mb}][\mathrm{O_2}]}{[\mathrm{Mb}] + K_{\rm d}^{-1}[\mathrm{Mb}][\mathrm{O_2}]}
```

Simplifying by multiplying the numerator and denominator by $K_{\rm d}/[\mathrm{Mb}]$, we find a much neater expression:

```{math}
:label: eq:myoglobin_binding
Y = \frac{[\mathrm{O_2}]}{[\mathrm{O_2}] + K_{\rm d}}
```

To summarize, this expression describes the ratio of myoglobin molecules that will have oxygen bound to them as a function of the concentration of free oxygen. We graph this expression in the following figure.

```{figure} ../../fig/myoglobin.png
---
width: 500px
name: fig_myoglobin_binding
---
The fractional degree of oxygenation of myoglobin as a function of free oxygen, which we have scaled by the dissociation constant $K_{\rm d}$.
```

It is worth taking a few minutes to think about the implications of this curve. For one, we have effectively assumed that the amount of oxygen available is an endless resource, so one _might_ assume that this would imply over time that all myoglobin molecules would end up saturated with oxygen. But from the binding curve, we see that this is _not_ the case; even when the oxygen concentrations grow very large, there will be some small ratio of myoglobin that is not oxygenated. This is simply because of the rates of the reaction. If all myoglobin were oxygenated, the forward rate of the binding reaction would be zero, but the reverse rate would be very high—so it is clear that the fractional degree of oxygenation will stabilize at some number strictly below 100%.

The curve tells us exactly what number this will be. If there is no oxygen available, no myoglobin can bind oxygen. As the concentration of free oxygen is low, the fractional oxygenation will also be low. Regardless of how much oxygen is available _in total_, it is the concentration of free oxygen that is important, due to the law of mass action.

Note especially that when $[\mathrm{O_2}] = K_{\rm d}$, we get $Y = 0.5$. In this scenario, the dissociation constant is equal to the point of half-saturation of the system. As the oxygen levels rise higher than this, the oxygenation rises slower and slower, and you can see the oxygen concentrations need to be very high for the oxygenation of myoglobin to truly approach full saturation.

In this example, we have derived the fractional oxygenation of myoglobin using the law of mass action and the equilibrium equation. This might seem like a very specific example, especially due to our assumption of a constant level of free oxygen. However, all the derivations we have done come directly from the law of mass action and are therefore very general. The assumption of a constant amount of free oxygen can also be a good approximation for any system where there is plenty of one reactant and comparatively little of the other. At the end of this module, we will turn to enzyme kinetics, which will be precisely such a system: a large amount of reactant compared to a small amount of a given enzyme.
