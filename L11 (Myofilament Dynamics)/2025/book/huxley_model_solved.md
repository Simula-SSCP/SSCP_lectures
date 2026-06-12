# Huxley model of contraction - with solutions

## Notebook prepared by: K.J. McCabe

Here we will work through A.F. Huxley's formulation of muscle contraction, first outlined in his 1957 paper "Muscle Structure and Theories of Contraction".

The model operates on several important assumptions regarding the crossbridge (XB) cycle:

1. Disregard thin filament activation - only deals with the contractile machinery
2. Operating in the plateau region of the length-tension relation
3. Constant velocity on whole filament level
4. Crossbridges always complete full cycle to detach and hydrolyze 1 ATP per cycle
5. Interaction between one myosin near an actin site is independent of all other pairs of actin sites and myosins

<img src="fig/Huxley_1.png" width=600></img>
**Figure** This diagram from Huxley's 1957 paper illustrates the simplified mechanism by which he hypothesized the myosin thick filament and actin thin filament slide in opposite directions during a contraction event. A = binding site on the actin thin filament, M = myosin head, O = equilibrium position at which no force would be generated. The model assumes only 1D force is generated, parallel to both filaments.

The main variable of significance in the Huxley model is x, displacement from the equilibrium. Over the population of the enormous amount of crossbridges in the cardiomyocyte, the model assumes a constant distribution $\hat{h}$ in x between -l/2 and l/2 (where l is the distance between 2 action binding sites).

<img src="fig/Prob_distribution.png" width=300></img>

If n(x,t) is a conditional probability describing the likelihood that a XB is attached given that the A site is at displacement x from equilibrium, at steady state:

$$
\begin{align}
\frac{dn(x,t)}{dt} = 0
\end{align}
$$

Applying the chain rule,

$$
\begin{align}
\frac{\partial n}{\partial x}\frac{dx}{dt} + \frac{\partial n}{\partial t}\frac{dt}{dt} = 0
\end{align}
$$

This simplifies to

$$
\begin{align}
\frac{\partial n}{\partial x}v + \frac{\partial n}{\partial t} = 0
\end{align}
$$

$$
\begin{align}
-v\frac{\partial n}{\partial x} = \frac{\partial n}{\partial t}
\end{align}
$$

$\partial$n/$\partial$t is equal to the rate of attachment to the A site minus the rate of detachment from the A site.

$$
\begin{align}
\frac{\partial n}{\partial t} = f(x)[1-n(x,t)]-g(x)n(x,t)
\end{align}
$$

Remembering that we are at steady state where dn(x,t)/dt = 0, we can substitute n(x,t) with n(x).

$$
\begin{align}
\frac{\partial n(x)}{\partial t} = f(x)[1-n(x)]-g(x)n(x)
\end{align}
$$

We can combine this with the above solution:

$$
\begin{align}
-v\frac{\partial n(x)}{\partial x} = \frac{\partial n(x)}{\partial t}
\end{align}
$$

$$
\begin{align}
-v\frac{\partial n(x)}{\partial x} = f(x)[1-n(x)]-g(x)n(x)
\end{align}
$$

The model defines rates $f$ and $g$ as piecewise functions of $x$, as described in the Figure below (units = 1/sec).

$$
\begin{align}
x<0: f(x) = 0, g(x) = g_2 \\
0<x<h: f(x) = \frac{f_1 x}{h}, g(x) = \frac{g_1 x}{h} \\
x>h: f(x) = 0, g(x) = \frac{g_1 x}{h}
\end{align}
$$

<img src="fig/f_g_functions.png" width=500></img>

In order to solve the ODE in each of the 3 piecewise regions, we can apply the constraint that for V $\neq$ 0, the solution is continuous, or

$$
\begin{align}
n(0^+)=n(0^-) \\
n(h^+)=n(h^-)
\end{align}
$$

In Region 1, x<0:

$$
\begin{align}
-v\frac{dn(x)}{dx} = f(x)[1-n(x)]-g(x)n(x) \\
-v\frac{dn(x)}{dx} = -g(x)n(x) \\
-v\frac{dn(x)}{dx} = -g_2n \\
\int{\frac{dn}{n}} = \int{\frac{g_2}{v}dx}\\
\ln{n} = {\frac{g_2}{v}dx}+ C_0\\
n(x) = C_1e^{\frac{g_2x}{v}}
\end{align}
$$

In Region 2, 0<x<h:

$$
\begin{align}
-v\frac{dn(x)}{dx} = \frac{f_1}{h}x[1-n]-\frac{g_1}{h}xn \\
-vh\frac{dn(x)}{dx} = f_1x[1-n]-g_1xn \\
-vh\frac{dn(x)}{dx} = f_1x-(f_1+g_1)xn \\
-vh\frac{dn(x)}{dx} = x(f_1+g_1)(\frac{f_1}{f_1+g_1})-n)\\
\int{\frac{dn}{-n+\frac{f_1}{f_1+g_1}}}=\int{\frac{f_1+g_1}{vh}xdx}\\
\ln{(-n+\frac{f_1}{f_1+g_1})}=\frac{f_1+g_1}{vh}\frac{x^2}{2}+C_2\\
-n+\frac{f_1}{f_1+g_1}=e^{\frac{f_1+g_1}{vh}\frac{x^2}{2}+C_2}\\
n = \frac{f_1}{f_1+g_1}-C_3e^{\frac{f_1+g_1}{vh}\frac{x^2}{2}}\\
\end{align}
$$

In Region 3, x>h, no crossbridges can be attached, which is equivalent to n(x,t)= 0 for x>h.

We can determine constants $C_1$ and $C_3$ using the continuity conditions:

$$
\begin{align}
n(h^+)=n(h^-) \\
0 = \frac{f_1}{f_1+g_1}-C_3e^{\frac{f_1+g_1}{vh}\frac{x^2}{2}} \\
C_3 = \frac{f_1}{f_1+g_1}e^{\frac{f_1+g_1}{vh}\frac{h^2}{2}}
\end{align}
$$

Substituting back into the original equation:

$$
\begin{align}
n(x) = \frac{f_1}{f_1+g_1}(1-e^{-\frac{f_1+g_1}{2vh}(h^2-x^2)})
\end{align}
$$

We can find $C_1$ using the other continuity condition: $n(0^-) = n(0^+)$

$$
\begin{align}
n(0^-)=C_1e^{\frac{0x}{v}} = C_1\\
n(0^+) = \frac{f_1}{f_1+g_1}(1-e^{-\frac{f_1+g_1}{2vh}h^2})\\
C_1 = \frac{f_1}{f_1+g_1}(1-e^{-\frac{f_1+g_1}{2vh}h^2})
\end{align}
$$

Substituting back into the original equation,

$$
\begin{align}
n(x) = \frac{f_1}{f_1+g_1}(1-e^{-\frac{f_1+g_1}{2vh}h^2})e^{-\frac{g_2x}{v}}
\end{align}
$$

Define $\phi=\frac{h}{S}(f_1+g_1)$ and $v = \frac{S}{2}V$

Where S = sarcomere length (~2um), V = normalized velocity (half sarcomeres/second)

We can now define the 3 regions:

$$
\begin{align}
x<0: n(x) = \frac{f_1}{f_1+g_1}(1-e^{-\frac{\phi}{V}})e^{-\frac{g_2x}{SV}}\\
0<x<h: n(x) = \frac{f_1}{f_1+g_1}(1-e^{(\frac{x^2}{h^2}-1)\frac{\phi}{V}})\\
x>h: n(x) = 0
\end{align}
$$

Use the code below to explore how altering velocity (v) can change the relationship between x and n.

```
# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
%matplotlib inline

# Set Parameters
S = 2e-3           #Sarcomere length, mm
f1 = 4.333          #1/sec, attachment rate (0<x<h)
g1 = 1.00              #1/sec
g2 = 20.91          #1/sec
l = 3e-5  #distance from equilibrium where Actin sites are distributed
h = 1e-5   #distance at which XBs can no longer attach
delta_x = 1e-6      #mm
k_spring = 10.00        #dyne/mm
phi = (h/S)*(f1+g1)

V = 0.03             #Normalized Velocity (half sarcomere length/second)

# Make a vector of points where solutions are to be computed
dx = 1e-10
X = 1.5
x = np.arange(-X*h, X*h, dx)
i = 0
n=[None]*len(x)

#compute solutions to piecewise function
while i < len(x):
    if x[i]<0:
        n[i] = (f1/(f1+g1))*(1-np.exp(-phi/V))*np.exp(g2*x[i]/(S*V))
    elif x[i]<h:
        n[i] = (f1/(f1+g1))*(1-np.exp(((np.power(x[i],2)/np.power(h,2))-1)*(phi/V)))
    else:
        n[i] = 0
    i+=1

x_plot = x/h

# Plot data with labels
plt.plot(x_plot, n)

plt.xlabel('x/h')
plt.ylabel('Probability of attached XBs')
plt.xlim(-1.5, 1.0)
plt.ylim(0,1)

plt.show()
```

From Huxley's paper, we can see that when V = 0, the probability of bound XBs is highest, with the number of attached XBs decreasing as sliding speed increases.
<img src="fig/n_vs_x_Huxley.png" width=300></img>

Now, we wish to generate a Force-Velocity relation. We will define force generated by a single XB as:

$$
\begin{align}
force_{XB} = kx
\end{align}
$$

So, the sum total of force generated by all crossbridges will depend on the probability distribution of $x$. We can write a function for $<T>$, or the expected value of tension, by adding the expected force produced by all attached XBs and the expected force produces by all detached XBs.

$$
\begin{align}
<T_{XB}> = \int_{-\inf}^{\inf}(kx\hat{n}(x)+0*(\hat{h}(x)-\hat{n}(x))) dx\\
<T_{XB}> = \int_{-\inf}^{\inf}(kx\hat{n}(x)) dx
\end{align}
$$

Recalling that we are assuming a constant probability distribution, and that $\hat{n}(x) = n(x)*\hat{h}(x)$ (or: total attached A sites = conditional probability of attachment \* probability distribution in x),
<img src="fig/Prob_distribution.png" width=300></img>

$$
\begin{align}
\begin{cases}
      n(x)/l & l/2<x<l/2 \\
      0 & other \\
\end{cases}
\end{align}
$$

So substituting this into our expected value of tension,

$$
\begin{align}
<T_{XB}> = \int_{-\inf}^{\inf}(kx\hat{n}(x)) dx\\
<T_{XB}> = \int_{-l/2}^{l/2}\frac{kx}{l}n(x) dx
\end{align}
$$

We plot this function below.

```
#compute solutions to piecewise function - for tension - x curve
new_x = np.arange(-l/2, l/2, dx)
i = 0
tension_deriv = [None]*len(new_x)
tension =[None]*len(new_x)

while i < len(new_x):
    if new_x[i]<0:
        n[i] = (f1/(f1+g1))*(1-np.exp(-phi/V))*np.exp(g2*new_x[i]/(S*V))
    elif new_x[i]<h:
        n[i] = (f1/(f1+g1))*(1-np.exp(((np.power(new_x[i],2)/np.power(h,2))-1)*(phi/V)))
    else:
        n[i] = 0
    tension_deriv[i] = k_spring*new_x[i]/(l)*n[i]
    i+=1

# Plot data with labels
plt.plot(new_x, tension_deriv)

plt.xlabel('x')
plt.ylabel('Derivative of Tension')

plt.show()
```

Substituting for n(x) and integrating, we arrive at:

$$
\begin{align}
<T_{XB}> = \frac{f_1}{f_1+g_1}\frac{kh^2}{2l}(1-\frac{V}{\phi}e^{-\frac{\phi}{V}})(1+\frac{1}{2}(\frac{f_1+g_1}{g_2})^2\frac{V}{\phi}))\\
\end{align}
$$

Where $\phi=\frac{h}{S}(f_1+g_1)$

In the case of isometric force, v=0 and $<T>=<T^{max}_{XB}>$

$$
\begin{align}
<T^{max}_{XB}> = \frac{f_1}{f_1+g_1}\frac{kh^2}{2l}
\end{align}
$$

```
#Compute the Tension for V=0.03, in units of T/Tmax
Tension_out = 1-((V)/phi)_(1-np.exp(-phi/V))_(1+(0.5*pow(((f1+g1)/g2),2))*(V/phi))

print(Tension_out)
```

```
#write code to generate Force-Velocity relationship
V_vector = np.linspace(0,0.11)
tension = [None]*len(V_vector)
T_vector = [0]*len(V_vector)
x = None
x = np.arange(-l, l, dx)
j = 1
T_vector[0] = 1
#re-compute solutions to piecewise function
while j < len(V_vector):
    T_vector[j]=1-((V_vector[j])/phi)*(1-np.exp(-phi/V_vector[j]))*(1+(0.5*pow(((f1+g1)/g2),2))*(V_vector[j]/phi))
    j+=1

```

```
# Plot data with labels
plt.plot(T_vector, V_vector)

plt.xlabel('Tension/Tmax')
plt.ylabel('Velocity')
plt.xlim(0, 1)
plt.ylim(0,0.104)


plt.show()
```

The best parameters to fit the experimental data shown in the Huxley paper are:

$$
\begin{align}
\frac{g_1}{f_1+g_1} = \frac{3}{16}\\
\frac{g_2}{f_1+g_1} = 3.919
\end{align}
$$

<img src="fig/Force_Velocity_Huxley.png" width=300></img>
