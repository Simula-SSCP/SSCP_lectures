# Ion channels

We have now seen how the membrane itself behaves electrically as an insulator. The other critical component for understanding the action potential is the _ion channels_.

While the lipid bilayer of the membrane is a simple barrier structure, the membrane also contains a vast number of highly complex proteins embedded within it. Perhaps the most important class of such membrane proteins are the **ion channels**. These are proteins that span the bilayer and create a _pore_ (a hole) in the membrane through which electrically charged ions can pass.

These channels typically contain a _selectivity filter_, meaning they only allow ions of a very specific type to pass through. Most channels also have the ability to physically open and close in response to various factors and conditions—this opening and closing is called _gating_, which will be the topic for most of tomorrow's lectures.

```{figure} ../../fig/ion_channel.png
---
width: 800px
name: fig_ion_channels
---
**Ion channels make the membrane permeable to charged ions.** <br>
**Left:** A schematic of an ion channel embedded in the lipid bilayer. The black ring represents a *selectivity filter*, enabling the channel to only allow specific ions through. <br>
**Right:** The protein structure of a K$^+$-specific ion channel. *(Image from Wikimedia Commons, CC BY-SA 4.0 license).*
```

As charged ions move through these channels, they carry an electric _transmembrane current_ that will shift the membrane potential. Modeling the currents through ion channels is therefore fundamental if we aim to understand the action potential. For now, let us ignore _how_ these channels open and close, and simply look at how to model the current that passes through them when they are open.

## Passive and active ion transport

Ion channels create a pathway through which charged ions can move. The actual movement of ions has to occur spontaneously, driven either by diffusion or by an electrical force pushing them. This is known as **passive ion transport**.

The opposite is **active transport**, where molecular machinery in the membrane known as _ion pumps_ or _exchangers_ actively burn energy (ATP) to force ions across the membrane against their natural gradients.

A useful analogy is to think of charged particles as people inside a building. If they want to move to a different floor, they can use either a staircase or an elevator. The staircase acts like an ion channel: it allows for movement, but the person still needs to provide their own energy to walk (passive transport). The elevator acts like an ion pump: it _actively_ moves people across floors using external power.

For now, we will focus strictly on passive ion transport. The most important characteristic of this transport is that it must satisfy $\Delta G < 0$; otherwise, it would break the laws of thermodynamics. This constraint will allow us to derive exact mathematical expressions for the currents these channels conduct.
