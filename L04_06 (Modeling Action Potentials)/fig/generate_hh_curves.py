"""Generate two-panel HH gating curves figure for section 11.4."""

import matplotlib.pyplot as plt
import numpy as np


# --- HH rate functions ---
def vtrap(x):
    """Numerically stable x / (1 - exp(-x))."""
    return np.where(np.abs(x) < 1e-6, 1.0 + x / 2.0, x / (1.0 - np.exp(-x)))

def alpha_m(V): return vtrap((V + 40) / 10)
def beta_m(V):  return 4.0 * np.exp(-(V + 65) / 18)
def alpha_h(V): return 0.07 * np.exp(-(V + 65) / 20)
def beta_h(V):  return 1.0 / (1.0 + np.exp(-(V + 35) / 10))
def alpha_n(V): return 0.1 * vtrap((V + 55) / 10)
def beta_n(V):  return 0.125 * np.exp(-(V + 65) / 80)


# --- Compute ---
V = np.linspace(-100, 50, 500)

m_inf = alpha_m(V) / (alpha_m(V) + beta_m(V))
h_inf = alpha_h(V) / (alpha_h(V) + beta_h(V))
n_inf = alpha_n(V) / (alpha_n(V) + beta_n(V))

tau_m = 1.0 / (alpha_m(V) + beta_m(V))
tau_h = 1.0 / (alpha_h(V) + beta_h(V))
tau_n = 1.0 / (alpha_n(V) + beta_n(V))

# --- Figure ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), sharex=True)

# ---- Panel A: Steady-state curves ----
ax1.plot(V, m_inf, "C0", linewidth=2.2, label=r"$m_\infty$ (Na⁺ activation)")
ax1.plot(V, h_inf, "C1", linewidth=2.2, label=r"$h_\infty$ (Na⁺ inactivation)")
ax1.plot(V, n_inf, "C2", linewidth=2.2, label=r"$n_\infty$ (K⁺ activation)")

ax1.set_xlabel("Membrane potential (mV)", fontsize=11)
ax1.set_ylabel("Steady-state value", fontsize=11)
ax1.set_xlim(-100, 50)
ax1.set_ylim(-0.05, 1.05)
ax1.legend(fontsize=9, loc="center right")
ax1.set_title("A", fontsize=14, fontweight="bold", loc="left")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.grid(True, alpha=0.2)

# ---- Panel B: Time constants ----
ax2.plot(V, tau_m, "C0", linewidth=2.2, label=r"$\tau_m$")
ax2.plot(V, tau_h, "C1", linewidth=2.2, label=r"$\tau_h$")
ax2.plot(V, tau_n, "C2", linewidth=2.2, label=r"$\tau_n$")

ax2.set_xlabel("Membrane potential (mV)", fontsize=11)
ax2.set_ylabel("Time constant (ms)", fontsize=11)
ax2.set_xlim(-100, 50)
ax2.set_ylim(0, 10)
ax2.legend(fontsize=9, loc="upper right")
ax2.set_title("B", fontsize=14, fontweight="bold", loc="left")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(
    "/Users/nicolai/github/SSCP_lectures/L04_06 (Modeling Action Potentials)/fig/hh_gating_curves.png",
    dpi=200,
    bbox_inches="tight",
    facecolor="white",
)
plt.show()
print("Saved to fig/hh_gating_curves.png")
