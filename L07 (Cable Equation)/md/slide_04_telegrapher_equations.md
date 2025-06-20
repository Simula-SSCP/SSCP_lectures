# The Telegrapher's Equations

## Heaviside's Mathematical Framework

### Partial Differential Equations

**Voltage Equation:**
$$\frac{\partial V}{\partial x} = -R \cdot I - L \frac{\partial I}{\partial t}$$

**Current Equation:**
$$\frac{\partial I}{\partial x} = -G \cdot V - C \frac{\partial V}{\partial t}$$

### Wave Equation Form

Combining the equations yields:

$$\frac{\partial^2 V}{\partial x^2} = LC \frac{\partial^2 V}{\partial t^2} + (RC + LG) \frac{\partial V}{\partial t} + RG \cdot V$$

---

## Line Parameters

| Parameter | Description |
|-----------|-------------|
| **R** | Resistance per unit length |
| **L** | Inductance per unit length |
| **C** | Capacitance per unit length |
| **G** | Conductance per unit length |

## Variables

| Variable | Description |
|----------|-------------|
| **V** | Voltage - Function of position (x) and time (t) |
| **I** | Current - Function of position (x) and time (t) |

---

### Mathematical Description

These equations describe both the spatial and temporal evolution of voltage and current, capturing the wave-like nature of signal propagation.

The telegrapher's equations represent a fundamental advance in understanding electromagnetic wave propagation in guided media, forming the basis for modern transmission line theory.

