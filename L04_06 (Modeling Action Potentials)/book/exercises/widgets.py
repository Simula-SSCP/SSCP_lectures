"""
Widgets for the Ion Channel Gating and Action Potential module.

This module provides interactive ipywidgets for exploring:
  - Gating kinetics with constant rates (Exercise 11.1b)
  - Voltage-dependent gating curves (Exercise 11.1d)
  - Two-current models with fixed conductances (Exercise 12.1a)
  - Voltage-dependent conductance models (Exercise 12.1b)
  - Full Hodgkin-Huxley AP explorer (Exercise 12.1f)
"""

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
from scipy.integrate import solve_ivp


# ===========================================================================
#  Exercise 11.1b: Gating with constant rates
# ===========================================================================


def gating_widget():
    """Interactive exploration of the gating equation dm/dt = alpha*(1-m) - beta*m.

    Students adjust alpha, beta, and the initial condition m0 to build intuition
    for steady-state (m_inf) and time constant (tau_m).
    """

    def _solve_and_plot(m0=0.0, alpha=1.0, beta=1.0):
        # Analytical solution parameters
        m_inf = alpha / (alpha + beta) if (alpha + beta) > 0 else 0.5
        tau_m = 1.0 / (alpha + beta) if (alpha + beta) > 0 else np.inf

        # Solve the ODE
        def rhs(t, m):
            return alpha * (1 - m) - beta * m

        t_span = (0, 5 * max(tau_m, 0.1))  # integrate for ~5 time constants
        t_eval = np.linspace(*t_span, 500)

        sol = solve_ivp(rhs, t_span, [m0], t_eval=t_eval, method="LSODA")

        # Plot
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(sol.t, sol.y[0], "C0", linewidth=2, label=r"$m(t)$")
        ax.axhline(m_inf, color="C1", linestyle="--", linewidth=1.5, label=rf"$m_\infty = {m_inf:.3f}$")
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel(r"$m$ (open probability)")
        ax.set_ylim(-0.05, 1.05)
        ax.set_title(rf"Gating kinetics — $\tau_m = {tau_m:.3f}$ ms")
        ax.legend(loc="center right")
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    interact(
        _solve_and_plot,
        m0=FloatSlider(value=0.0, min=0.0, max=1.0, step=0.05, description="m₀", continuous_update=False),
        alpha=FloatSlider(value=1.0, min=0.0, max=10.0, step=0.1, description="α", continuous_update=False),
        beta=FloatSlider(value=1.0, min=0.0, max=10.0, step=0.1, description="β", continuous_update=False),
    )


# ===========================================================================
#  Exercise 11.1d: Voltage-dependent gating curves
# ===========================================================================


def voltage_dependence_widget():
    """Interactive exploration of how rate parameters shape m_inf(V) and tau_m(V).

    Uses the exponential rate forms:
        alpha(V) = exp((V - V_alpha) / d_alpha)
        beta(V)  = exp((V - V_beta) / d_beta)
    """

    def _plot(V_alpha=-40, d_alpha=15, V_beta=-40, d_beta=-15):
        V = np.linspace(-120, 60, 500)
        alpha = np.exp((V - V_alpha) / d_alpha)
        beta = np.exp((V - V_beta) / d_beta)

        m_inf = alpha / (alpha + beta)
        tau_m = 1.0 / (alpha + beta)

        fig, axs = plt.subplots(1, 3, figsize=(14, 4))

        # Panel 1: Rate constants
        axs[0].plot(V, alpha, "C0", linewidth=2, label=r"$\alpha(V)$")
        axs[0].plot(V, beta, "C1", linewidth=2, label=r"$\beta(V)$")
        axs[0].set_ylim(0, 5)
        axs[0].set_xlabel("V (mV)")
        axs[0].set_ylabel("Rate (1/ms)")
        axs[0].set_title("Rate constants")
        axs[0].legend()
        axs[0].grid(True, alpha=0.3)

        # Panel 2: Steady-state
        axs[1].plot(V, m_inf, "k", linewidth=2)
        axs[1].set_xlabel("V (mV)")
        axs[1].set_ylabel(r"$m_\infty$")
        axs[1].set_title("Steady-state activation")
        axs[1].set_ylim(-0.05, 1.05)
        axs[1].grid(True, alpha=0.3)

        # Panel 3: Time constant
        axs[2].plot(V, tau_m, "k", linewidth=2)
        axs[2].set_xlabel("V (mV)")
        axs[2].set_ylabel(r"$\tau_m$ (ms)")
        axs[2].set_title("Time constant")
        axs[2].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    interact(
        _plot,
        V_alpha=FloatSlider(value=-40, min=-100, max=100, step=1, description="V_α", continuous_update=False),
        d_alpha=FloatSlider(value=15, min=1, max=50, step=1, description="d_α", continuous_update=False),
        V_beta=FloatSlider(value=-40, min=-100, max=100, step=1, description="V_β", continuous_update=False),
        d_beta=FloatSlider(value=-15, min=-50, max=-1, step=1, description="d_β", continuous_update=False),
    )


# ===========================================================================
#  Exercise 12.1a: Two-current model with fixed conductances
# ===========================================================================


def fixed_conductance_widget():
    """Explore a minimal two-current model with fixed (non-gated) conductances.

    C_m dV/dt = -g_Na*(V - E_Na) - g_K*(V - E_K) + I_app

    Key insight: with fixed conductances, the system is linear and cannot
    generate an action potential. External current is needed to change V.
    """

    # Fixed biophysical parameters
    Cm = 0.05  # nF
    E_Na = 50.0  # mV
    E_K = -80.0  # mV

    def _solve_and_plot(V0=-65, I_amp=1.0, g_Na=0.0, g_K=0.2):
        def rhs(t, y):
            V = y[0]
            I_app = I_amp if t < 1 else 0.0
            dV = (-g_Na * (V - E_Na) - g_K * (V - E_K) + I_app) / Cm
            return [dV]

        t_span = (0, 5)
        t_eval = np.linspace(*t_span, 500)
        sol = solve_ivp(rhs, t_span, [V0], t_eval=t_eval, method="LSODA")

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(sol.t, sol.y[0], "C0", linewidth=2, label="$V(t)$")
        ax.axhline(E_Na, color="C3", linestyle="--", alpha=0.5, label=f"$E_{{Na}}$ = {E_Na} mV")
        ax.axhline(E_K, color="C4", linestyle="--", alpha=0.5, label=f"$E_{{K}}$ = {E_K} mV")
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("V (mV)")
        ax.set_title("Two-current model with fixed conductances")
        ax.legend(loc="center right")
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    interact(
        _solve_and_plot,
        V0=FloatSlider(value=-65, min=-100, max=100, step=1, description="V₀ (mV)", continuous_update=False),
        I_amp=FloatSlider(value=1.0, min=0.0, max=10, step=0.1, description="I_app (nA)", continuous_update=False),
        g_Na=FloatSlider(value=0.0, min=0.0, max=1.0, step=0.01, description="g_Na (µS)", continuous_update=False),
        g_K=FloatSlider(value=0.2, min=0.0, max=1.0, step=0.01, description="g_K (µS)", continuous_update=False),
    )


# ===========================================================================
#  Exercise 12.1b: Voltage-dependent conductance (single gate)
# ===========================================================================


def voltage_gated_conductance_widget():
    """Explore a model where the Na+ conductance is voltage-gated via m_inf(V).

    C_m dV/dt = -g_Na * m_inf(V) * (V - E_Na) - g_K*(V - E_K) + I_app

    Key insight: the voltage-dependent Na gate creates positive feedback,
    introducing a threshold phenomenon — but no inactivation, so no AP.
    """

    Cm = 0.05  # nF
    E_Na = 50.0  # mV
    E_K = -80.0  # mV
    g_Na = 0.8  # µS
    g_K = 0.1  # µS

    def _m_inf(V, Vs, d):
        alpha = np.exp((V - Vs) / d)
        beta = np.exp(-(V - Vs) / d)
        return alpha / (alpha + beta)

    def _solve_and_plot(V0=-65, I_amp=0.0, Vs=-20, d=10):
        def rhs(t, y):
            V = y[0]
            I_app = I_amp if t < 1 else 0.0
            m = _m_inf(V, Vs, d)
            dV = (-g_Na * m * (V - E_Na) - g_K * (V - E_K) + I_app) / Cm
            return [dV]

        t_span = (0, 10)
        t_eval = np.linspace(*t_span, 1000)
        sol = solve_ivp(rhs, t_span, [V0], t_eval=t_eval, method="LSODA")

        # Also compute the I-V relationship
        V_sweep = np.linspace(-100, 100, 500)
        m_ss = _m_inf(V_sweep, Vs, d)
        I_total = -g_Na * m_ss * (V_sweep - E_Na) - g_K * (V_sweep - E_K)

        fig, axs = plt.subplots(1, 3, figsize=(14, 4))

        # V(t)
        axs[0].plot(sol.t, sol.y[0], "C0", linewidth=2, label="$V(t)$")
        axs[0].axhline(E_Na, color="C3", linestyle="--", alpha=0.4, label="$E_{Na}$")
        axs[0].axhline(E_K, color="C4", linestyle="--", alpha=0.4, label="$E_{K}$")
        axs[0].set_xlabel("Time (ms)")
        axs[0].set_ylabel("V (mV)")
        axs[0].set_title("$V(t)$")
        axs[0].legend(loc="center right")
        axs[0].grid(True, alpha=0.3)

        # m_inf(V)
        axs[1].plot(V_sweep, m_ss, "k", linewidth=2)
        axs[1].set_xlabel("V (mV)")
        axs[1].set_ylabel(r"$m_\infty$")
        axs[1].set_title("Steady-state activation")
        axs[1].set_ylim(-0.05, 1.05)
        axs[1].grid(True, alpha=0.3)

        # I(V) curve
        axs[2].plot(V_sweep, I_total, "C2", linewidth=2)
        axs[2].axhline(0, color="gray", linewidth=0.5)
        axs[2].set_xlabel("V (mV)")
        axs[2].set_ylabel("Total current (nA)")
        axs[2].set_title(r"$I(V) = -I_{\rm Na}(V) - I_{\rm K}(V)$")
        axs[2].set_ylim(-10, 10)
        axs[2].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    interact(
        _solve_and_plot,
        V0=FloatSlider(value=-65, min=-100, max=100, step=1, description="V₀ (mV)", continuous_update=False),
        I_amp=FloatSlider(value=0.0, min=0.0, max=10, step=0.1, description="I_app (nA)", continuous_update=False),
        Vs=FloatSlider(value=-20, min=-100, max=100, step=1, description="V_s (mV)", continuous_update=False),
        d=FloatSlider(value=10, min=1, max=50, step=1, description="d (mV)", continuous_update=False),
    )


# ===========================================================================
#  Exercise 12.1f: Full HH Action Potential Explorer
# ===========================================================================


def hh_explorer_widget():
    """Interactive exploration of the full Hodgkin-Huxley model.

    Students can adjust maximal conductances, stimulus current, and initial
    voltage to explore the action potential, refractory period, and individual
    ionic currents.
    """

    # Standard HH parameters
    Cm = 1.0  # µF/cm²
    E_Na = 50.0  # mV
    E_K = -77.0  # mV
    E_L = -54.4  # mV

    def _alpha_m(V):
        return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))

    def _beta_m(V):
        return 4.0 * np.exp(-(V + 65) / 18)

    def _alpha_h(V):
        return 0.07 * np.exp(-(V + 65) / 20)

    def _beta_h(V):
        return 1.0 / (1 + np.exp(-(V + 35) / 10))

    def _alpha_n(V):
        return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))

    def _beta_n(V):
        return 0.125 * np.exp(-(V + 65) / 80)

    def _solve_and_plot(g_Na=120, g_K=36, g_L=0.3, I_amp=10, stim_start=2, stim_dur=1, V0=-65):
        stim_end = stim_start + stim_dur

        def rhs(t, y):
            V, m, h, n = y
            I_app = I_amp if stim_start <= t <= stim_end else 0.0

            am, bm = _alpha_m(V), _beta_m(V)
            ah, bh = _alpha_h(V), _beta_h(V)
            an, bn = _alpha_n(V), _beta_n(V)

            I_Na = g_Na * m**3 * h * (V - E_Na)
            I_K = g_K * n**4 * (V - E_K)
            I_L = g_L * (V - E_L)

            dV = (-I_Na - I_K - I_L + I_app) / Cm
            dm = am * (1 - m) - bm * m
            dh = ah * (1 - h) - bh * h
            dn = an * (1 - n) - bn * n

            return [dV, dm, dh, dn]

        # Initial gating values at resting potential
        m0 = _alpha_m(V0) / (_alpha_m(V0) + _beta_m(V0))
        h0 = _alpha_h(V0) / (_alpha_h(V0) + _beta_h(V0))
        n0 = _alpha_n(V0) / (_alpha_n(V0) + _beta_n(V0))

        t_span = (0, 30)
        t_eval = np.linspace(*t_span, 2000)
        sol = solve_ivp(rhs, t_span, [V0, m0, h0, n0], t_eval=t_eval, method="LSODA")
        V, m, h, n = sol.y

        # Compute currents for plotting
        I_Na = g_Na * m**3 * h * (V - E_Na)
        I_K = g_K * n**4 * (V - E_K)
        I_L = g_L * (V - E_L)

        fig, axs = plt.subplots(1, 3, figsize=(16, 4))

        # Panel 1: Membrane potential
        axs[0].plot(sol.t, V, "C0", linewidth=2)
        axs[0].axhspan(stim_start, stim_end, alpha=0.1, color="yellow")
        axs[0].set_xlabel("Time (ms)")
        axs[0].set_ylabel("V (mV)")
        axs[0].set_title("Membrane potential")
        axs[0].grid(True, alpha=0.3)

        # Panel 2: Gating variables
        axs[1].plot(sol.t, m, label="m (Na act.)", linewidth=1.5)
        axs[1].plot(sol.t, h, label="h (Na inact.)", linewidth=1.5)
        axs[1].plot(sol.t, n, label="n (K act.)", linewidth=1.5)
        axs[1].set_xlabel("Time (ms)")
        axs[1].set_ylabel("Gate value")
        axs[1].set_title("Gating variables")
        axs[1].set_ylim(-0.05, 1.05)
        axs[1].legend(fontsize=8)
        axs[1].grid(True, alpha=0.3)

        # Panel 3: Individual currents
        axs[2].plot(sol.t, -I_Na, label=r"$-I_{\rm Na}$", linewidth=1.5)
        axs[2].plot(sol.t, -I_K, label=r"$-I_{\rm K}$", linewidth=1.5)
        axs[2].plot(sol.t, -I_L, label=r"$-I_{\rm L}$", linewidth=1.5)
        axs[2].set_xlabel("Time (ms)")
        axs[2].set_ylabel("Current (µA/cm²)")
        axs[2].set_title("Ionic currents (positive = inward)")
        axs[2].legend(fontsize=8)
        axs[2].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    interact(
        _solve_and_plot,
        g_Na=FloatSlider(value=120, min=0, max=200, step=5, description="ḡ_Na", continuous_update=False),
        g_K=FloatSlider(value=36, min=0, max=100, step=1, description="ḡ_K", continuous_update=False),
        g_L=FloatSlider(value=0.3, min=0, max=2, step=0.1, description="ḡ_L", continuous_update=False),
        I_amp=FloatSlider(value=10, min=0, max=50, step=1, description="I_app (µA/cm²)", continuous_update=False),
        stim_start=FloatSlider(value=2, min=0, max=10, step=0.5, description="Stim start (ms)", continuous_update=False),
        stim_dur=FloatSlider(value=1, min=0.1, max=10, step=0.1, description="Stim dur (ms)", continuous_update=False),
        V0=FloatSlider(value=-65, min=-100, max=0, step=1, description="V₀ (mV)", continuous_update=False),
    )
