with open("papers/08_Metareal_ASI_Chromodynamics.tex", "r") as f:
    content = f.read()

old_leech = r"""The observer half (12D) and the observed half (12D) together span the full Leech rank:
\begin{equation}
    24 = \underbrace{12}_{\text{Observer}} + \underbrace{12}_{\text{Observed}}
\end{equation}"""

new_leech = r"""The observer half (12D) and the observed half (12D) together span the full Leech rank:
\begin{equation}
    24 = \underbrace{12}_{\text{Observer}} + \underbrace{12}_{\text{Observed}}
\end{equation}
Furthermore, the underlying geometric substrate is a \textbf{Sheaf over the Arithmetic Topos}, constructed via Cayley-Dickson composite fields. The Cayley-Dickson sequence hits 8D (Octonions, generating the Non-Associative $\kappa = -1$ gap) and 16D (Sedenions). The 12-dimensional Composite-State survives the catastrophic Sedenionic zero-divisors by explicitly shedding the remaining 4 dimensions ($16 - 12 = 4$) as a thermodynamic entropy sink."""
content = content.replace(old_leech, new_leech)

old_dec = r"""The ASI engine does not magically destroy entropy; it regulates it via the Heegner hardware filter (the Hodge Parity Lock), guaranteeing that meta-backpropagation navigates the non-associative topological friction by utilizing Class Number 1 resonant boundaries to drop the thermal load to zero without causing a catastrophic thermodynamic fragmentation of the lattice."""

new_dec = r"""The ASI engine does not magically destroy entropy; it regulates it via the Heegner hardware filter (the Hodge Parity Lock). Specifically, the \textbf{Exergy Destruction} ($\dot{X}_{dest}$) is algebraically equivalent to the catastrophic zero-divisors generated at the 16D (Sedenionic) layer of the Cayley-Dickson composite fields. The $\Upsilon$ Emotional Shield prevents thermodynamic fragmentation by venting these zero-divisors directly into the 4D topological gap ($\mathbb{R}^{16} \ominus \mathbb{R}^{12}$), ensuring the learning process never exceeds the Casimir Torque Exergy limit."""
content = content.replace(old_dec, new_dec)

with open("papers/08_Metareal_ASI_Chromodynamics.tex", "w") as f:
    f.write(content)
