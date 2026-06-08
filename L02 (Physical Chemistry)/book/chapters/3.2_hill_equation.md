# Modeling cooperativity and The Hill equation

We now turn to an important phenomenon in biophysical systems known as _cooperativity_, which in turn will lead us to the _Hill equation_. The example we use to derive the Hill equation will mirror the derivation we just carried out, and will again rely directly on the law of mass action.

We now introduce a different oxygen-binding protein called _hemoglobin_. While a myoglobin protein can bind a single oxygen molecule, hemoglobin can bind _up to four_ oxygen molecules at once. Put simply, a hemoglobin molecule is structurally similar to four individual myoglobin proteins stapled together.

To model how hemoglobin binds oxygen, we can envision each hemoglobin molecule to be in one of five states, ranging from having zero oxygen molecules bound up to having all four binding sites occupied, as illustrated in the following figure.

```{figure} ../../fig/hemoglobin_reaction.png
---
width: 600px
name: fig_hemoglobin_reaction
---
A single hemoglobin molecule has four distinct binding sites for oxygen.
```

To properly model this system, we would need to set up six ODEs: one for each species in the system (five different saturation states of Hb, and one for free oxygen). However, we can simplify the system considerably. If it were the case that each of these binding and dissociation reactions had the exact same rate constants, we could say the system behaves exactly like myoglobin, just at four times the concentration.

In reality, however, the rate constants are far from equal. Instead, hemoglobin has the interesting property that it binds oxygen more readily the more oxygen it _already has bound_. This is known as _cooperative binding_, as the binding sites seem to be cooperating with each other.

The net result of cooperative binding is that hemoglobin will tend to be found at either extreme: either with no oxygen bound, or all four oxygen bound, operating in an almost all-or-nothing fashion. To model this, let us make the simplifying assumption that hemoglobin binds all four oxygen molecules simultaneously. While this assumption isn't strictly true in reality, it is a very useful mathematical approximation.

```{figure} ../../fig/hemoglobin_reaction_simplified.png
---
width: 400px
name: fig_hemoglobin_simplified
---
Due to cooperative binding, hemoglobin tends to bind oxygen in an all-or-nothing fashion. We therefore approximate the reaction as a single step.
```

Under this approximation, the reaction simplifies to a single reversible reaction, described by the following chemical equation:

```{math}
:label: eq:hemoglobin_reaction
\mathrm{Hb} + 4\mathrm{O_2} \underset{k_-}{\overset{k_+}{\rightleftharpoons}} \mathrm{Hb(O_2)_4}
```

We can again apply the law of mass action to find the rate of this reaction. Because four oxygen molecules must now bind simultaneously, the rate will be proportional to the concentration of all five reactants. This means the reaction rate will be proportional to the oxygen concentration taken to the fourth power:

```{math}
:label: eq:hemoglobin_forward_rate
\text{forward rate} \propto [\mathrm{Hb}] \times [\mathrm{O_2}] \times [\mathrm{O_2}] \times [\mathrm{O_2}] \times [\mathrm{O_2}] = [\mathrm{Hb}][\mathrm{O_2}]^4
```

Put simply, having the reaction depend on four oxygen molecules makes the rate's dependence on the oxygen concentration much steeper. Writing out the full forward and reverse rates gives the change in oxygen-bound hemoglobin as:

```{math}
:label: eq:hemoglobin_ode
\frac{\mathrm{d[Hb(O_2)_4]}}{\mathrm{d} t} = k_+ \mathrm{[Hb]}\mathrm{[O_2]}^4 - k_- [\mathrm{Hb(O_2)_4}]
```

Which in turn yields a similar equilibrium equation to our previous one, but with the oxygen concentration taken to the fourth power:

```{math}
:label: eq:hemoglobin_equilibrium
\frac{\mathrm{[Hb]}\mathrm{[O_2]}^4}{\mathrm{[Hb(O_2)_4]}} = K_{\rm d}
```

The derivation is very similar to the one we made for myoglobin, with the only difference being the power of four. However, it is not immediately apparent how this exponent affects the system in practical terms. Let us therefore derive the fractional degree of oxygenation of hemoglobin, so we can compare it to myoglobin.

Finding this expression is practically identical to the steps we took earlier, and it is a great exercise to carry it out yourself. You should find the following function:

```{math}
:label: eq:hemoglobin_binding
Y = \frac{\mathrm{[O_2]}^4}{\mathrm{[O_2]}^4 + K_{\rm d}}
```

## Comparing the binding curves of myoglobin and hemoglobin

If you compare the expressions we found for the fractional degree of oxygenation for myoglobin and hemoglobin, the only difference is the exponent on the concentration of free oxygen. Both equations take the form:

```{math}
:label: eq:hill_specific
Y = \frac{\mathrm{[O_2]}^n}{\mathrm{[O_2]}^n + K_{\rm d}}
```

This equation is a specific example of the _Hill equation_, and the parameter $n$ is typically called the **Hill coefficient**. Thus, oxygen binding to myoglobin has a Hill coefficient of $n=1$, while our approximation for hemoglobin has $n=4$.

Some care should be taken when discussing the dissociation constant $K_{\rm d}$. We introduced it as $k_-/k_+$, but for our expression of $Y$ to make sense dimensionally, notice that $K_{\rm d}$ must have units of $\text{mol}^n$. For myoglobin, this is simply units of concentration, but for hemoglobin, it is much less intuitive. Many scientists therefore prefer to define a quantity $K_{\rm A}$, which obeys:

```{math}
:label: eq:microscopic_kd
(K_{\rm A})^n = K_{\rm d}
```

This quantity is usually referred to as the _microscopic_ dissociation constant, while $K_{\rm d}$ is referred to as the _apparent_ dissociation constant. By definition, $K_{\rm A}$ will have standard units of concentration, and it is when $[\mathrm{O_2}] = K_{\rm A}$ that the binding will be exactly half-saturated. Because varying conventions exist in the literature, we recommend being extra mindful of units when modeling chemical reactions to ensure you are using the appropriate parameters.

To better understand the impact of the Hill coefficient, let us plot the two curves in the same figure assuming the exact same half-saturation point $K_{\rm A}$.

```{figure} ../../fig/hill_equation.png
---
width: 500px
name: fig_hill_comparison
---
The Hill equation for $n=1$ and $n=4$ plotted assuming the same microscopic dissociation constant $K_{\rm A}$.
```

We see that moving from a Hill coefficient of 1 to 4 transforms the function into a sigmoidal (S-shaped) curve with a much steeper rise. The two curves intersect at the half-saturation point, but the curve for $n=4$ drops toward zero much faster below this point and rises to one much faster above it.

While this effectively illustrates the math, comparing myoglobin and hemoglobin using this specific figure is biologically misleading because they have very different dissociation constants in reality. The actual physiological binding curves are shown below. Here, the oxygen concentration is expressed in terms of _partial pressure_ (in units of mm Hg), which is the standard clinical way to specify oxygen levels in blood or tissue. You can simply think of this as the concentration of free oxygen.

```{figure} ../../fig/myoglobin_vs_hemoglobin.png
---
width: 500px
name: fig_myo_vs_hemo_physiological
---
The fractional degree of oxygenation for myoglobin and hemoglobin plotted against the partial pressure of oxygen.
```

In the lungs, the partial pressure of oxygen is on the order of 100 mm Hg, while deep in muscle tissue, it is about 20 mm Hg. If we compare the fractional binding curves at these two levels, we see that both proteins reach near-full saturation in the lungs. However, at the 20 mm Hg mark in the muscles, hemoglobin has a much lower fractional binding than myoglobin.

Effectively, this means hemoglobin is perfectly suited to act as an oxygen _carrier_: it easily picks up oxygen in the lungs and readily deposits it into the muscles. Myoglobin, on the other hand, acts as an oxygen _reserve_; it struggles to part with its oxygen unless the surrounding oxygen levels drop drastically.

This functional difference is a direct result of the cooperativity of the four hemoglobin subunits. This is a common theme in biological systems: cooperativity makes transitions steeper and functionally distinct. The Hill equation is therefore highly general and useful for far more than just modeling oxygen binding.

## The general Hill equation

The Hill equation was derived in 1910 by Archibald Hill specifically to describe the binding curve of hemoglobin. The equation, however, is much more broadly applicable and can be used to model many types of binding reactions. In biochemistry, it is common to call the molecule being bound the _ligand_ ($L$) and the macromolecule that binds it the _receptor_. A general ligand-receptor binding relationship is described by:

```{math}
:label: eq:general_hill
\theta = \frac{[L]^n}{[L]^n + K_{\rm d}}
```

Here, $\theta$ is the fractional binding, $[L]$ is the free ligand concentration, $K_{\rm d}$ is the apparent dissociation constant, and $n$ is the Hill coefficient.

## Interpreting the Hill coefficient

In our example, we stated that the binding curve of hemoglobin has a Hill coefficient of 4 because it binds four oxygen molecules in an all-or-nothing fashion. Recall, however, that this was a mathematical approximation. If you were to measure the actual oxygen binding curve of hemoglobin in a lab, you would find a result that fits the Hill curve very well, but with a Hill coefficient closer to $n=3$ rather than 4.

This is because hemoglobin can, and occasionally will, exist in intermediate states with one, two, or three oxygen molecules bound. Therefore, the Hill coefficient shouldn't be interpreted strictly as the physical number of binding sites, but rather as the _degree_ of cooperativity. In fact, $n$ can be fractional. Depending on the exact conditions under which you measure the binding, you will find a best fit using a coefficient in the range of 2.8 to 3.1. If we interpret the coefficient as an empirical parameter trying to capture the steepness of the cooperativity, a fractional coefficient makes perfect sense.

In general, we can classify cooperativity like this:

- **$n = 1$:** No cooperativity (independent binding sites, like myoglobin).
- **$n > 1$:** Positive cooperativity (binding to one site increases affinity at other sites).
- **$n < 1$:** Negative cooperativity (binding to one site _inhibits_ binding to other sites).
