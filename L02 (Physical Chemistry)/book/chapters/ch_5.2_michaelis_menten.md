# The Michaelis-Menten equation

As mentioned, enzymes can work in many different ways. It can actually be challenging to explain precisely _why_ they work. For example, the enzyme _catalase_ is common to almost all life that processes oxygen and is a heavily studied organic molecule, but exactly how it breaks down $\mathrm{H_2O_2}$ still isn't perfectly understood. Therefore, let us not try to model _how_ an enzyme works physically, but rather how it affects the macroscopic reaction rate.

The model we will look at is called the **Michaelis-Menten equation**, and it is a direct result of the law of mass action. As you will see, it also closely resembles the Hill equation. While it is a relatively simple model, it is immensely useful and sees widespread use in physiological modeling. It sometimes goes under the name of _first-order kinetics_, as we make a few simplifying assumptions when deriving it.

## Model states

Enzymes generally work by binding to a target molecule (the _substrate_), converting it, and then releasing the _product_. We therefore propose the following reaction chain to model this activity:

```{math}
:label: eq:mm_reaction
\mathrm{S} + \mathrm{E} \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} \mathrm{ES} \overset{k_2}{\longrightarrow} \mathrm{E} + \mathrm{P}
```

Here, $\mathrm{S}$ is the substrate to be converted and $\mathrm{E}$ is the enzyme. These can bind together to form an enzyme-substrate complex, $\mathrm{ES}$. The $\mathrm{ES}$ complex can either break apart again without converting the substrate (the reverse arrow), or the substrate can be successfully converted, breaking the complex into a free enzyme molecule and a product molecule, $\mathrm{P}$. We assume that once the product has been released, it no longer binds to the enzyme spontaneously, which is why there is no reverse arrow in the final step.

## Reaction rate

We are now modeling a system with three different reactions, so what exactly do we mean by the _reaction rate_? The most interesting quantity here is the rate at which the final product $\mathrm{P}$ is generated, meaning the time derivative $\frac{\mathrm{d[P]}}{\mathrm{d}t}$. We will call this rate the _reaction velocity_, denoted as $v$.

Luckily, the law of mass action applies to each concentration separately. Looking at the final step of our reaction equation, we can write the velocity as:

```{math}
:label: eq:mm_velocity
v = \frac{\mathrm{d[P]}}{\mathrm{d}t} = k_2[\mathrm{ES}]
```

As you can see, to compute an actual value for the velocity, we first need to find an expression for the concentration of the complex $[\mathrm{ES}]$. We start by using the law of mass action to find the rate of change for the complex itself:

```{math}
:label: eq:mm_complex_rate
\frac{\mathrm{d[ES]}}{\mathrm{d}t} = k_1[\mathrm{S}][\mathrm{E}] - k_{-1}[\mathrm{ES}] - k_2[\mathrm{ES}] = k_1[\mathrm{S}][\mathrm{E}] - (k_{-1} + k_2)[\mathrm{ES}]
```

To go further, we will make the assumption that the system quickly reaches a state where the amount of bound and unbound enzyme stabilizes, meaning the concentration $[\mathrm{ES}]$ becomes constant over time. If you recall, this is a common assumption typically referred to as a _quasistatic_ steady state. Based on this assumption, we can set the derivative to zero:

```{math}
:label: eq:mm_steady_state
k_1[\mathrm{S}][\mathrm{E}] = (k_{-1} + k_2)[\mathrm{ES}]
```

Because the enzyme doesn't get "used up," the total amount of enzyme is constant over time. We can eliminate the free enzyme concentration $[\mathrm{E}]$ using the conservation relation $[\mathrm{E}] + [\mathrm{ES}] = [\mathrm{E}]_{\rm tot}$, which gives:

```{math}
:label: eq:mm_substitution
k_1[\mathrm{S}]([\mathrm{E}]_{\rm tot} - [\mathrm{ES}]) = (k_{-1} + k_2)[\mathrm{ES}]
```

Solving this algebraically for $[\mathrm{ES}]$ yields:

```{math}
:label: eq:mm_es_solved
[\mathrm{ES}] = \frac{k_1[\mathrm{S}][\mathrm{E}]_{\rm tot}}{k_{-1} + k_2 + k_1[\mathrm{S}]}
```

Going back and inserting this expression into our original reaction velocity ($v = k_2[\mathrm{ES}]$) gives:

```{math}
:label: eq:mm_velocity_expanded
v = \frac{k_1 k_2 [\mathrm{S}][\mathrm{E}]_{\rm tot}}{k_{-1} + k_2 + k_1[\mathrm{S}]}
```

This might look incredibly messy, but remember that almost all of these terms are just constants that we can group together to simplify the expression. First, let us define the maximum possible velocity of the system as $v_{\rm max} \equiv k_2[\mathrm{E}]_{\rm tot}$. (This maximum occurs if every single enzyme molecule is bound to a substrate). Substituting this gives:

```{math}
:label: eq:mm_vmax_sub
v = v_{\rm max} \frac{k_1 [\mathrm{S}]}{k_{-1} + k_2 + k_1[\mathrm{S}]}
```

Next, we divide both the numerator and the denominator by $k_1$ and define a new constant, the _Michaelis constant_, as $K_m = (k_{-1} + k_2)/k_1$. This results in the final, clean equation:

```{math}
:label: eq:michaelis_menten
v = v_{\rm max} \frac{[\mathrm{S}]}{K_m + [\mathrm{S}]}
```

Note that because $K_m > 0$, the fraction $[\mathrm{S}]/(K_m + [\mathrm{S}])$ will always be strictly less than 1. This means the reaction velocity operates smoothly in the range $[0, v_{\rm max}]$. Furthermore, if the substrate concentration is exactly equal to the Michaelis constant ($[\mathrm{S}] = K_m$), we get $v = v_{\rm max}/2$. Thus, $K_m$ can be thought of as the substrate concentration at which the enzyme is operating at exactly half its maximum capacity.

The mathematical model we have just derived is known as **Michaelis-Menten kinetics**. It works exceptionally well for a broad range of enzymes. The cases where it struggles are usually reactions involving several different interacting substrates. Single-substrate reactions, however, are almost universally assumed to follow Michaelis-Menten kinetics.

Also, take a moment to compare the Michaelis-Menten equation with the Hill equation from the previous chapter. Notice how mathematically identical they are! In fact, the Michaelis-Menten equation is simply a special case of the Hill equation where the Hill coefficient is $n=1$, meaning we assume there is no cooperativity involved. The fact that the Michaelis-Menten model yields the exact same functional expression as our derivation of fractional binding isn't terribly surprising, but it beautifully demonstrates that enzyme kinetics exhibit the exact same saturation behavior as ligand binding.

## Enzyme inhibition

Another critical class of molecules are _enzyme inhibitors_. These are molecules that reduce, or completely shut off, the activity of specific enzymes. There are different functional ways for inhibitors to work, but the simplest mechanism involves the inhibitor binding to the enzyme more readily than the actual substrate, but failing to convert into a product. The enzyme is effectively "jammed," wasting its time bound to an inhibitor rather than processing the substrate.

Enzyme inhibition is a crucial tool the cell uses for regulating its own behavior, and many medical drugs are simply targeted enzyme inhibitors. A famous example is penicillin, which inhibits an enzyme that bacteria need for cell wall synthesis. Without the enzyme's activity, the bacteria are unable to maintain their cell walls and eventually die.

Extending the Michaelis-Menten model to include enzyme inhibitors is quite straightforward: we simply add the inhibitor as a new species ($\mathrm{I}$) and introduce new reaction paths where the inhibitor can bind to the enzyme. We can build slightly different models depending on _where_ and _how_ the inhibitor binds. When compared to experimental data, these different mathematical models perfectly describe different classes of real-world inhibitors. The figure below shows how the Michaelis-Menten reaction chain is extended for each of these classes.

```{figure} ../../fig/enzyme_inhibition.png
---
width: 600px
name: fig_enzyme_inhibition
---
Different enzyme inhibitors can work in different ways. Here are four different ways we can incorporate the action of an inhibitor into the Michaelis-Menten model, all of which will produce different kinetic behaviors. From a mathematical perspective, however, these different extensions are conceptually identical—they are all derived directly from the law of mass action.
```

For each of these specific cases, we could go through our analysis again: set up the ODEs using the law of mass action, assume a quasistatic steady state, and solve for the new velocity expressions. While we won't go through all that algebra here, the model predictions generated by this approach agree incredibly well with experimental data and are highly useful in pharmacological modeling.

As you have seen, the Michaelis-Menten model is relatively simple, but surprisingly powerful. The fact that it can be so easily extended to include the complex effects of inhibitors is precisely why it is a cornerstone of biomedical engineering.

## Solving the Michaelis-Menten system

So far, we have made steady-state assumptions to simplify the mathematics so we could find a clean, analytical expression. However, we can also solve the raw ODE system we derived numerically using the exact same Python approach we used for standard chemical reactions.

The following exercise will walk you through exactly how to do this:

- {doc}`Exercise 5.1: Modeling Michaelis-Menten kinetics <../exercises/exercise_5.1_enzymes>`

## Summary and moving towards modeling ion channels

In this chapter, we have focused on basic, universally applicable concepts in physical chemistry. Our goal was to get you into the right mathematical mindset and provide a solid foundation before we shift our focus to applied electrophysiology in the upcoming sessions.

For now, let us give you a sneak peek at what is to come in future lectures, and how it ties directly into what we covered today.

### Law of mass action applied to ion channel gating

The most important tool we covered in this module was the **law of mass action**. We introduced it strictly as a physical law governing chemical reactions. However, the mathematical framework is far more general and can be applied to physical state changes as well.

A vital example of this—and a central focus of this course—is **ion channel gating**. An ion channel in the cell membrane can physically transition between an _open_ ($\mathrm{O}$) or a _closed_ ($\mathrm{C}$) state. A single cell will possess a massive number of these channels. Instead of tracking each one, we can define variables that represent the _ratio_ (or fraction) of channels in each state, meaning:

```{math}
:label: eq:channel_conservation
\mathrm{C} + \mathrm{O} = 1
```

To model how these ion channels open or close over time, we can write this physical transition exactly as if it were a reversible chemical reaction, and apply the law of mass action:

```{math}
:label: eq:channel_reaction
\mathrm{C} \underset{\beta}{\overset{\alpha}{\rightleftharpoons}} \mathrm{O}
```

The exact physical mechanism of how the ion channel opens is not mathematically important here; all that matters is that there is a specific rate at which channels open, and a rate at which they close. These are typically called the _opening_ and _closing_ rates (or simply _on_ and _off_ rates), which we denote as $\alpha$ and $\beta$.

Using the exact same rules we used for molecules, we can set up an ODE for the open state:

```{math}
:label: eq:channel_ode_initial
\frac{\mathrm{dO}}{\mathrm{d}t} = \alpha \mathrm{C} - \beta \mathrm{O}
```

Because we know that $\mathrm{O} + \mathrm{C} = 1$, we can substitute $\mathrm{C} = 1 - \mathrm{O}$ to write this as an independent ODE with a single variable:

```{math}
:label: eq:channel_ode_final
\frac{\mathrm{dO}}{\mathrm{d}t} = \alpha(1 - \mathrm{O}) - \beta \mathrm{O} = \alpha - (\alpha + \beta) \mathrm{O}
```

We can now solve this ODE numerically just like our earlier chemical examples! What makes this system beautifully complex—and what separates it from the static chemistry we have done so far—is that the opening and closing rates for ion channels ($\alpha$ and $\beta$) are generally _not_ static constants. Instead, they change dynamically based on the electrical voltage across the cell membrane.

You will learn exactly how to model that voltage dependence very soon.
