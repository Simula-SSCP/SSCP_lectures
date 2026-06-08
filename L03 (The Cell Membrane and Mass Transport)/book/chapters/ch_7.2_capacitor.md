# The cell membrane as a capacitor

The inside and outside of the cell are both fluid-filled environments with plenty of charged ions that can conduct electrical currents quite well. These two environments are separated by the membrane, which acts as an electrical insulator. When two electrical conductors are separated by a thin insulator, we get what we call an electric _capacitor_.

If an electric potential is applied across a capacitor, an electric current _wants_ to flow through, but the insulator prevents it. Instead, we get a pile-up of charge on both sides of the insulator. This build-up of charge continues until the static charge is large enough to set up an electric field of equal strength—but opposite direction—to the applied potential, effectively canceling it out. We can say that the capacitor acts like a tiny battery that gets charged up, and once it is fully charged, the current stops.

```{figure} ../../fig/capacitor.png
---
width: 400px
name: fig_capacitor_concept
---
The *intracellular* and *extracellular* environments conduct charges well, but the membrane does not. If we apply an electric field across the membrane, it will act like a capacitor, leading to a build-up of charge on either side.
```

## Modeling a capacitor

Let us now look at how to model this process mathematically. The amount of charge that is built up on either side of the membrane at equilibrium will be proportional to the applied potential:

```{math}
:label: eq:capacitor_charge
V = \frac{Q}{C_{\mathrm{m}}}
```

Here, $V$ is the potential, or _voltage_, across the capacitor and $Q$ is the total charge separated by it. The proportionality factor is called the _capacitance_, which is a physical property of the capacitor in question. Here we denote it $C_{\mathrm{m}}$ to clarify that it is the _membrane_ capacitance.

The capacitance of the lipid bilayer is about 1 µF/cm$^2$, where F is the unit of capacitance, the Farad. If we multiply this quantity by the full surface area of the cell membrane, the whole cell has a capacitance of about 0.05 nF. This might seem like a very small quantity because it is given in nanofarads; however, the Farad is an absolutely huge unit. Most capacitances seen in electrical components are in the range of pF to µF. Having around 50 pF for the microscopic size of the cell means the membrane capacitance is actually fairly high!

The variable $V$ represents the electric potential difference across the membrane, which we often just call the _membrane potential_. (Some prefer to denote it $V_{\mathrm{m}}$ for clarity, but we will stick with the simple $V$ here). It is precisely this quantity that changes throughout the action potential, and it is therefore the primary variable we are interested in modeling in electrophysiology.

## How does the membrane potential change?

While the equation above is technically only true at equilibrium, electrical phenomena are typically extremely fast. As such, we can assume the potential across the membrane is directly proportional to the charge separation at all times (_quasistatic conditions_). This means that if there is a _change_ in the charge, that will directly shift the membrane potential.

To see how the membrane potential changes, we take the time derivative of the equation:

```{math}
:label: eq:membrane_derivative
\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{1}{C_{\mathrm{m}}} \frac{\mathrm{d}Q}{\mathrm{d}t}
```

The time derivative of a charge can be physically interpreted as a current. We call this the _capacitive current_, or $I_{\mathrm{cap}}$. The capacitive current is a _virtual_ current, as it isn't an actual physical current flowing across the insulator (which cannot happen), but rather a mathematical description of the charge building up or decaying at the surface of the membrane.

Thus, our equation can be written as:

```{math}
:label: eq:membrane_ode_base
\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{1}{C_{\mathrm{m}}} I_{\mathrm{cap}}
```

We now have a differential equation we can use to model how the membrane potential changes over time. To actually solve it, we obviously need to find an expression for the capacitive current $I_{\mathrm{cap}}$, which we will do in the next chapter.

Since it is useful to model the membrane as an electrical component, it is also useful to draw an electrical circuit diagram summarizing our model. In this basic case, it will be very simple, as shown below.

```{figure} ../../fig/membrane_capacitor.png
---
width: 400px
name: fig_membrane_circuit
---
A *circuit diagram* of the cell membrane. The membrane acts like a simple capacitor that separates the inside and outside of the cell.
```

Because the intracellular and extracellular environments are good conductors, it is fair to say that the electric potential in these environments is constant in space. We therefore denote these simply as _scalar_ quantities $V_{\mathrm{i}}$ and $V_{\mathrm{e}}$. The membrane potential is then the difference between these two. It can be defined in either direction, but it is standard to define it with respect to the inside of the cell:

```{math}
:label: eq:potential_diff
\Delta V = V_{\mathrm{i}} - V_{\mathrm{e}}
```

Even though the membrane potential is technically a potential _difference_, it is very common to denote it simply as $V$, dropping the $\Delta$ symbol for neater notation.

## Your turn: Looking at a simple _voltage clamp_ model

To get a better feel for the equations we have just shown you. Please turn to the accompanying exercises in the next section: {doc}`Exercise 7.2: A simple voltage clamp model <../exercises/exercise_7.2_voltage_clamp>`.
