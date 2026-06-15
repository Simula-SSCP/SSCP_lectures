"""Generate annotated action potential figure for section 12.1."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# --- HH rate functions (correct vtrap) ---
def vtrap(x):
    return np.where(np.abs(x) < 1e-6, 1.0 + x / 2.0, x / (1.0 - np.exp(-x)))


def alpha_m(V):
    return vtrap((V + 40) / 10)


def beta_m(V):
    return 4.0 * np.exp(-(V + 65) / 18)


def alpha_h(V):
    return 0.07 * np.exp(-(V + 65) / 20)


def beta_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35) / 10))


def alpha_n(V):
    return 0.1 * vtrap((V + 55) / 10)


def beta_n(V):
    return 0.125 * np.exp(-(V + 65) / 80)


def m_inf(V):
    return alpha_m(V) / (alpha_m(V) + beta_m(V))


def h_inf(V):
    return alpha_h(V) / (alpha_h(V) + beta_h(V))


def n_inf(V):
    return alpha_n(V) / (alpha_n(V) + beta_n(V))


# Parameters
C_m = 1.0
g_Na, g_K, g_L = 120.0, 36.0, 0.3
E_Na, E_K, E_L = 50.0, -77.0, -54.4


def hh_rhs(t, y):
    V, m, h, n = y
    I_app = 10.0 if 2 < t < 3 else 0.0
    I_Na = g_Na * m**3 * h * (V - E_Na)
    I_K = g_K * n**4 * (V - E_K)
    I_L = g_L * (V - E_L)
    dVdt = (-I_Na - I_K - I_L + I_app) / C_m
    dmdt = alpha_m(V) * (1 - m) - beta_m(V) * m
    dhdt = alpha_h(V) * (1 - h) - beta_h(V) * h
    dndt = alpha_n(V) * (1 - n) - beta_n(V) * n
    return [dVdt, dmdt, dhdt, dndt]


# --- Solve ---
V0 = -65.0
y0 = [V0, m_inf(V0), h_inf(V0), n_inf(V0)]
sol = solve_ivp(hh_rhs, [0, 25], y0, max_step=0.02, method="RK45")

t = sol.t
V, m, h, n = sol.y

# --- Identify AP phases ---
peak_idx = np.argmax(V)
t_peak = t[peak_idx]

upstroke_mask = (t < t_peak) & (V > -56)
thresh_idx = np.where(upstroke_mask)[0][0] if np.any(upstroke_mask) else 0

post_peak = np.where(t > t_peak)[0]
ahp_region = post_peak[post_peak < np.searchsorted(t, t_peak + 8)]
ahp_idx = ahp_region[np.argmin(V[ahp_region])] if len(ahp_region) > 0 else post_peak[0]
t_ahp = t[ahp_idx]

# --- Figure ---
fig, (ax1, ax2) = plt.subplots(
    2,
    1,
    figsize=(9, 7),
    sharex=True,
    gridspec_kw={"height_ratios": [3, 2], "hspace": 0.08},
)

ann_fs = 11
arrow_kw = dict(arrowstyle="->", color="C3", lw=1.3)

# ---- Top: Voltage trace ----
ax1.plot(t, V, "k", linewidth=2)

# Resting potential
ax1.axhline(V0, color="gray", linestyle="--", linewidth=0.8, alpha=0.4)
ax1.text(
    0.3,
    V0 + 1.8,
    r"$\mathbf{V}_\mathbf{\mathrm{rest}}$",
    fontsize=ann_fs,
    fontweight="bold",
    color="gray",
)

# Threshold line + annotation (well left of the upstroke)
ax1.axhline(-55, color="gray", linestyle=":", linewidth=1, alpha=0.6)
ax1.annotate(
    "Threshold\n(−55 mV)",
    xy=(t[thresh_idx], -55),
    xytext=(1.0, -42),
    fontsize=ann_fs,
    fontweight="bold",
    color="gray",
    arrowprops=dict(arrowstyle="->", color="gray", lw=1),
)

# 1. Stimulus
ax1.plot([2, 3], [-77, -77], linewidth=4, color="gray", solid_capstyle="butt")
ax1.annotate(
    "1. Stimulus",
    xy=(2.5, -77),
    xytext=(2.5, -87),
    ha="center",
    fontsize=ann_fs,
    fontweight="bold",
    color="0.15",
)

# 2. Depolarization (color-coded to m = C0)
t_mid_up = (t[thresh_idx] + t_peak) / 2
V_mid_up = V[np.searchsorted(t, t_mid_up)]
ax1.annotate(
    "2. Depolarization\n(m opens → Na⁺ in)",
    xy=(t_mid_up, V_mid_up),
    xytext=(t_peak + 1.0, 42),
    fontsize=ann_fs,
    fontweight="bold",
    color="0.15",
    arrowprops=arrow_kw,
)

# 3. Repolarization (dark, since it involves both h and n)
t_mid_down = t_peak + 1.2
V_mid_down = V[np.searchsorted(t, t_mid_down)]
ax1.annotate(
    "3. Repolarization\n(h closes, n opens → K⁺ out)",
    xy=(t_mid_down, V_mid_down),
    xytext=(t_mid_down + 4, 5),
    fontsize=ann_fs,
    fontweight="bold",
    color="0.15",
    arrowprops=arrow_kw,
)

# 4. Afterhyperpolarization (color-coded to n = C2, above curve)
ax1.annotate(
    "4. Afterhyperpolarization\n(excess K⁺ current)",
    xy=(t_ahp, V[ahp_idx]),
    xytext=(t_ahp + 1.5, -53),
    fontsize=ann_fs,
    fontweight="bold",
    color="0.15",
    arrowprops=arrow_kw,
)

ax1.set_ylabel("Membrane potential (mV)", fontsize=12)
ax1.set_ylim(-90, 55)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# ---- Bottom: Gating variables ----
ax2.plot(t, m, "C0", linewidth=2, label=r"$m$ (Na⁺ act.)")
ax2.plot(t, h, "C1", linewidth=2, label=r"$h$ (Na⁺ inact.)")
ax2.plot(t, n, "C2", linewidth=2, label=r"$n$ (K⁺ act.)")

ax2.set_xlabel("Time (ms)", fontsize=12)
ax2.set_ylabel("Gating variable", fontsize=12)
ax2.set_ylim(-0.05, 1.05)
ax2.set_xlim(0, 20)
ax2.legend(fontsize=10, loc="upper right")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

plt.savefig(
    "ap_phases.png",
    dpi=200,
    bbox_inches="tight",
    facecolor="white",
)
plt.show()
print("Saved to fig/ap_phases.png")
