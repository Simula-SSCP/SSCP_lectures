"""Generate annotated Boltzmann + time constant figure for section 11.2."""

import matplotlib.pyplot as plt
import numpy as np

# --- Rate function parameters (generic exponential) ---
V_half = -40  # half-activation voltage (mV)
k = 6  # slope factor (mV)

# Exponential rates that produce the desired Boltzmann
# alpha(V) = A * exp((V - Va) / da),  beta(V) = A * exp((V - Vb) / db)
# Choose symmetric rates for a clean illustration
A = 1.0  # ms^-1 at crossover
da = 12  # mV
db = -12  # mV


def alpha(V):
    return A * np.exp((V - V_half) / da)


def beta(V):
    return A * np.exp((V - V_half) / db)


# --- Compute ---
V = np.linspace(-100, 20, 500)
m_inf = alpha(V) / (alpha(V) + beta(V))
tau_m = 1.0 / (alpha(V) + beta(V))

tau_peak_idx = np.argmax(tau_m)
V_peak = V[tau_peak_idx]
tau_peak = tau_m[tau_peak_idx]

# --- Figure ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), sharex=True)

# ---- Panel A: Steady-state curve ----
ax1.plot(V, m_inf, color="#2563EB", linewidth=2.5)

# Midpoint marker and dashed lines
ax1.hlines(0.5, V[0], V_half, colors="gray", linestyles="--", linewidth=1)
ax1.vlines(V_half, 0, 0.5, colors="gray", linestyles="--", linewidth=1)
ax1.plot(V_half, 0.5, "o", color="#2563EB", markersize=8, zorder=5)

# Tangent line at V_1/2
slope_at_half = 1 / (4 * k)
V_tangent = np.linspace(V_half - 2.5 * k, V_half + 2.5 * k, 100)
m_tangent = 0.5 + slope_at_half * (V_tangent - V_half)
ax1.plot(V_tangent, m_tangent, "--", color="#DC2626", linewidth=1.2, alpha=0.8)

# Annotate V_1/2
ax1.annotate(
    r"$V_{1/2}$", xy=(V_half, 0), xytext=(V_half + 2, -0.08), fontsize=14, ha="left"
)

# Slope annotation
y_lo = 0.5 - slope_at_half * k
y_hi = 0.5 + slope_at_half * k
ax1.annotate(
    "",
    xy=(V_half + k, y_hi),
    xytext=(V_half - k, y_lo),
    arrowprops=dict(arrowstyle="<->", color="#DC2626", lw=1.5),
)
ax1.text(
    V_half + k + 3,
    0.5,
    f"slope $\\propto 1/k$\n($k = {k}$ mV)",
    fontsize=10,
    color="#DC2626",
    va="center",
)

# Asymptotic labels
ax1.text(-90, 0.05, "All channels\nclosed", fontsize=10, color="gray", ha="center")
ax1.text(10, 0.88, "All channels\nopen", fontsize=10, color="gray", ha="center")

ax1.set_xlabel("Membrane potential $V$ (mV)", fontsize=12)
ax1.set_ylabel(r"Steady-state $m_\infty$", fontsize=12)
ax1.set_ylim(-0.12, 1.08)
ax1.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax1.set_title("A", fontsize=14, fontweight="bold", loc="left")
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.grid(True, alpha=0.2)

# ---- Panel B: Time constant curve ----
ax2.plot(V, tau_m, color="#059669", linewidth=2.5)

# Peak marker and dashed lines
ax2.vlines(V_peak, 0, tau_peak, colors="gray", linestyles="--", linewidth=1)
ax2.hlines(tau_peak, V[0], V_peak, colors="gray", linestyles="--", linewidth=1)
ax2.plot(V_peak, tau_peak, "o", color="#059669", markersize=8, zorder=5)

# Annotate peak
ax2.annotate(
    rf"$\tau_{{m,\mathrm{{max}}}} = {tau_peak:.2f}$ ms"
    + "\n"
    + r"(where $\alpha \approx \beta$)",
    xy=(V_peak, tau_peak),
    xytext=(V_peak + 15, tau_peak * 0.85),
    fontsize=10,
    color="#059669",
    arrowprops=dict(arrowstyle="->", color="#059669", lw=1.2),
    ha="left",
    va="top",
)

# Asymptotic labels
ax2.text(
    -90,
    tau_m[10] + 0.04,
    r"$\beta$ dominates" + "\n" + "(fast closing)",
    fontsize=9,
    color="gray",
    ha="center",
)
ax2.text(
    12,
    tau_m[-10] + 0.04,
    r"$\alpha$ dominates" + "\n" + "(fast opening)",
    fontsize=9,
    color="gray",
    ha="center",
)

ax2.set_xlabel("Membrane potential $V$ (mV)", fontsize=12)
ax2.set_ylabel(r"Time constant $\tau_m$ (ms)", fontsize=12)
ax2.set_ylim(bottom=0)
ax2.set_title("B", fontsize=14, fontweight="bold", loc="left")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(
    "boltzmann_and_tau.png",
    dpi=200,
    bbox_inches="tight",
    facecolor="white",
)
plt.show()
print("Saved to fig/boltzmann_and_tau.png")
