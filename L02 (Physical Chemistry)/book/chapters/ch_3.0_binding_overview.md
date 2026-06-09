# Ligand binding and cooperativity

In the previous chapter, we looked at how chemical reactions progress over time using the law of mass action. We primarily treated these systems as closed, tracking the absolute concentrations of every molecule involved.

However, when modeling physiological systems, we rarely care about the absolute number of protein molecules in a cell. Instead, we want to know what _fraction_ of those proteins are currently active or bound to a ligand. For example, in a muscle cell, how many myoglobin proteins actually have oxygen attached to them at a given oxygen level?

In this chapter, we will shift our focus to **fractional binding**. We will derive the binding curves that describe how proteins become saturated with ligands. Furthermore, we will explore **cooperativity**---a fascinating phenomenon where proteins with multiple binding sites (like hemoglobin) change their binding affinity dynamically. To model this, we will introduce the **Hill equation**, a cornerstone of biophysical modeling used to describe non-linear, switch-like behavior in biology.
