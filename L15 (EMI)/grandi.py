import numpy as np


def init_states(N_nodes):
    """Initializes the 38 Grandi ODE states for an array of nodes."""
    states = np.zeros((38, N_nodes))
    # --- I_Na ---
    states[0, :] = 0.00379308741444  # m
    states[1, :] = 0.626221949492  # h
    states[2, :] = 0.62455357249  # j

    # --- I_Kr ---
    states[3, :] = 0.0210022533039  # x_kr

    # --- I_Ks ---
    states[4, :] = 0.00428016666259  # x_ks

    # --- I_to ---
    states[5, :] = 0.000440445885643  # x_to_s
    states[6, :] = 0.785115828275  # y_to_s
    states[7, :] = 0.000440438103759  # x_to_f
    states[8, :] = 0.999995844039  # y_to_f

    # --- I_Ca ---
    states[9, :] = 2.92407183949e-06  # d
    states[10, :] = 0.995135796704  # f
    states[11, :] = 0.0246760872106  # f_Ca_Bj
    states[12, :] = 0.0152723084239  # f_Ca_Bsl

    # --- SR Fluxes ---
    states[13, :] = 0.890806040818  # Ry_Rr
    states[14, :] = 7.40481128854e-07  # Ry_Ro
    states[15, :] = 9.07666168961e-08  # Ry_Ri

    # --- Na Buffers ---
    states[16, :] = 3.45437733033  # Na_Bj
    states[17, :] = 0.753740951478  # Na_Bsl

    # --- Cytosolic Ca Buffers ---
    states[18, :] = 0.00893455096919  # Tn_CL
    states[19, :] = 0.117412025937  # Tn_CHc
    states[20, :] = 0.0106160166693  # Tn_CHm
    states[21, :] = 0.000295573424135  # CaM
    states[22, :] = 0.00192322252438  # Myo_c
    states[23, :] = 0.137560495023  # Myo_m
    states[24, :] = 0.00217360235649  # SRB

    # --- Junctional and SL Ca Buffers ---
    states[25, :] = 0.0074052452168  # SLL_j
    states[26, :] = 0.00990339304377  # SLL_sl
    states[27, :] = 0.0735890020284  # SLH_j
    states[28, :] = 0.114583623437  # SLH_sl

    # --- SR Ca Concentrations ---
    states[29, :] = 1.19723145924  # Csqn_b
    states[30, :] = 0.554760499828  # Ca_sr

    # --- Na Concentrations ---
    states[31, :] = 8.40537012593  # Na_j
    states[32, :] = 8.40491910001  # Na_sl
    states[33, :] = 8.40513364345  # Na_i

    # --- K Concentration ---
    states[34, :] = 120.0  # K_i

    # --- Ca Concentrations ---
    states[35, :] = 0.000175882395147  # Ca_j
    states[36, :] = 0.000106779509977  # Ca_sl
    states[37, :] = 8.72509677797e-05  # Ca_i

    return states


def grandi_rhs(states, V_m, GNa, d_states):
    """
    Computes the right-hand side (derivatives) of the Grandi ODE system.
    Results are saved in-place into the provided d_states array.
    """
    # Unpack states
    m, h, j, x_kr, x_ks, x_to_s, y_to_s, x_to_f, y_to_f, d, f = states[0:11]
    f_Ca_Bj, f_Ca_Bsl, Ry_Rr, Ry_Ro, Ry_Ri, Na_Bj, Na_Bsl = states[11:18]
    Tn_CL, Tn_CHc, Tn_CHm, CaM, Myo_c, Myo_m, SRB = states[18:25]
    SLL_j, SLL_sl, SLH_j, SLH_sl, Csqn_b, Ca_sr = states[25:31]
    Na_j, Na_sl, Na_i, K_i, Ca_j, Ca_sl, Ca_i = states[31:38]

    # --- Geometry ---
    Fjunc = 0.11
    Fjunc_CaL = 0.9
    cellLength = 100.0
    cellRadius = 10.25
    distJuncSL = 0.5
    distSLcyto = 0.45
    junctionLength = 0.16
    junctionRadius = 0.015

    # --- I_Na ---
    # GNa = 23.0

    # --- I_NaBK ---
    GNaB = 0.000597

    # --- I_NaK ---
    IbarNaK = 1.8
    KmKo = 1.5
    KmNaip = 11.0
    Q10KmNai = 1.39
    Q10NaK = 1.63

    # --- I_Kp ---
    gkp = 0.002

    # --- I_Ks ---
    pNaK = 0.01833

    # --- I_to ---
    epi = 1.0

    # --- I_ClCa ---
    GClB = 0.009
    GClCa = 0.0548125
    KdClCa = 0.1

    # --- I_Ca ---
    Q10CaL = 1.8
    pCa = 0.00027
    pK = 1.35e-07
    pNa = 7.5e-09

    # --- I_NCX ---
    IbarNCX = 4.5
    Kdact = 0.00015
    KmCai = 0.00359
    KmCao = 1.3
    KmNai = 12.29
    KmNao = 87.5
    Q10NCX = 1.57
    ksat = 0.32
    nu = 0.27

    # --- I_PCa ---
    IbarSLCaP = 0.0673
    KmPCa = 0.0005
    Q10SLCaP = 2.35

    # --- I_CaBK ---
    GCaB = 0.0005513

    # --- SR Fluxes ---
    Kmf = 0.000246
    Kmr = 1.7
    MaxSR = 15.0
    MinSR = 1.0
    Q10SRCaP = 2.6
    Vmax_SRCaP = 0.0053114
    ec50SR = 0.45
    hillSRCaP = 1.787
    kiCa = 0.5
    kim = 0.005
    koCa = 10.0
    kom = 0.06
    ks = 25.0

    # --- Na Buffers ---
    Bmax_Naj = 7.561
    Bmax_Nasl = 1.65
    koff_na = 0.001
    kon_na = 0.0001

    # --- Cytosolic Ca Buffers ---
    Bmax_CaM = 0.024
    Bmax_SR = 0.0171
    Bmax_TnChigh = 0.14
    Bmax_TnClow = 0.07
    Bmax_myosin = 0.14
    koff_cam = 0.238
    koff_myoca = 0.00046
    koff_myomg = 5.7e-05
    koff_sr = 0.06
    koff_tnchca = 3.2e-05
    koff_tnchmg = 0.00333
    koff_tncl = 0.0196
    kon_cam = 34.0
    kon_myoca = 13.8
    kon_myomg = 0.0157
    kon_sr = 100.0
    kon_tnchca = 2.37
    kon_tnchmg = 0.003
    kon_tncl = 32.7

    # --- Junctional and SL Ca Buffers ---
    Bmax_SLhighj0 = 0.000165
    Bmax_SLhighsl0 = 0.0134
    Bmax_SLlowj0 = 0.00046
    Bmax_SLlowsl0 = 0.0374
    koff_slh = 0.03
    koff_sll = 1.3
    kon_slh = 100.0
    kon_sll = 100.0

    # --- SR Ca Concentrations ---
    Bmax_Csqn0 = 0.14
    DcaJuncSL = 1.64e-06
    DcaSLcyto = 1.22e-06
    J_ca_juncsl = 8.2413e-13
    J_ca_slmyo = 3.7243e-12
    koff_csqn = 65.0
    kon_csqn = 100.0

    # --- Na Concentrations ---
    DnaJuncSL = 1.09e-05
    DnaSLcyto = 1.79e-05
    J_na_juncsl = 1.8313e-14
    J_na_slmyo = 1.6386e-12
    Nao = 140.0

    # --- K Concentration ---
    Ko = 5.4

    # --- Ca Concentration ---
    Cao = 1.8

    # --- Cl Concentrations ---
    Cli = 15.0
    Clo = 150.0

    # --- Mg Concentrations ---
    Mgi = 1.0

    # --- Membrane potential ---
    Cmem = 1.381e-10
    Frdy = 96485.0
    R = 8314.0
    Temp = 310.0

    # --- Expressions for the Geometry component ---
    Vcell = 1e-15 * np.pi * cellLength * cellRadius**2
    Vmyo = 0.65 * Vcell
    Vsr = 0.035 * Vcell
    Vsl = 0.02 * Vcell
    Vjunc = 0.000539 * Vcell
    Fsl = 1.0 - Fjunc
    Fsl_CaL = 1.0 - Fjunc_CaL

    # --- Expressions for the Reversal potentials component ---
    FoRT = Frdy / (R * Temp)
    ena_junc = np.log(Nao / Na_j) / FoRT
    ena_sl = np.log(Nao / Na_sl) / FoRT
    ek = np.log(Ko / K_i) / FoRT
    eca_junc = np.log(Cao / Ca_j) / (2.0 * FoRT)
    eca_sl = np.log(Cao / Ca_sl) / (2.0 * FoRT)
    ecl = np.log(Cli / Clo) / FoRT
    Qpow = -31.0 + Temp / 10.0

    # --- Expressions for the I_Na component ---
    mss = (1.0 + 0.00184221158117 * np.exp(-0.110741971207 * V_m)) ** (-2)
    taum = 0.1292 * np.exp(
        -((2.94658944659 + 0.0643500643501 * V_m) ** 2)
    ) + 0.06487 * np.exp(-((-0.0943466353678 + 0.0195618153365 * V_m) ** 2))
    ah = np.where(V_m >= -40.0, 0.0, 4.43126792958e-07 * np.exp(-0.147058823529 * V_m))
    bh = np.where(
        V_m >= -40.0,
        (0.77 / (0.13 + 0.0497581410839 * np.exp(-0.0900900900901 * V_m))),
        (310000.0 * np.exp(0.3485 * V_m) + 2.7 * np.exp(0.079 * V_m)),
    )
    tauh = 1.0 / (ah + bh)
    hss = (1.0 + 15212.5932857 * np.exp(0.134589502019 * V_m)) ** (-2)
    aj = np.where(
        V_m >= -40.0,
        0.0,
        (
            (37.78 + V_m)
            * (-25428.0 * np.exp(0.2444 * V_m) - 6.948e-06 * np.exp(-0.04391 * V_m))
            / (1.0 + 50262745826.0 * np.exp(0.311 * V_m))
        ),
    )
    bj = np.where(
        V_m >= -40.0,
        (0.6 * np.exp(0.057 * V_m) / (1.0 + 0.0407622039784 * np.exp(-0.1 * V_m))),
        (
            0.02424
            * np.exp(-0.01052 * V_m)
            / (1.0 + 0.0039608683399 * np.exp(-0.1378 * V_m))
        ),
    )
    tauj = 1.0 / (aj + bj)
    jss = (1.0 + 15212.5932857 * np.exp(0.134589502019 * V_m)) ** (-2)

    d_states[0] = (mss - m) / taum
    d_states[1] = (hss - h) / tauh
    d_states[2] = (jss - j) / tauj

    I_Na_junc = Fjunc * GNa * m**3 * (-ena_junc + V_m) * h * j
    I_Na_sl = GNa * m**3 * (-ena_sl + V_m) * Fsl * h * j

    # --- Expressions for the I_NaBK component ---
    I_nabk_junc = Fjunc * GNaB * (-ena_junc + V_m)
    I_nabk_sl = GNaB * (-ena_sl + V_m) * Fsl

    # --- Expressions for the I_NaK component ---
    sigma = -1.0 / 7.0 + np.exp(0.0148588410104 * Nao) / 7.0
    fnak = 1.0 / (
        1.0 + 0.1245 * np.exp(-0.1 * FoRT * V_m) + 0.0365 * np.exp(-FoRT * V_m) * sigma
    )
    I_nak_junc = (
        Fjunc * IbarNaK * Ko * fnak / ((1.0 + KmNaip**4 / Na_j**4) * (KmKo + Ko))
    )
    I_nak_sl = IbarNaK * Ko * Fsl * fnak / ((1.0 + KmNaip**4 / Na_sl**4) * (KmKo + Ko))
    I_nak = I_nak_junc + I_nak_sl

    # --- Expressions for the I_Kr component ---
    gkr = 0.0150616019019 * np.sqrt(Ko)
    xrss = 1.0 / (1.0 + np.exp(-2.0 - V_m / 5.0))
    tauxr = 230.0 / (1.0 + np.exp(2.0 + V_m / 20.0)) + 3300.0 / (
        (1.0 + np.exp(-22.0 / 9.0 - V_m / 9.0)) * (1.0 + np.exp(11.0 / 9.0 + V_m / 9.0))
    )
    d_states[3] = (xrss - x_kr) / tauxr
    rkr = 1.0 / (1.0 + np.exp(37.0 / 12.0 + V_m / 24.0))
    I_kr = (-ek + V_m) * gkr * rkr * x_kr

    # --- Expressions for the I_Kp component ---
    kp_kp = 1.0 / (1.0 + 1786.47556538 * np.exp(-0.167224080268 * V_m))
    I_kp_junc = Fjunc * gkp * (-ek + V_m) * kp_kp
    I_kp_sl = gkp * (-ek + V_m) * Fsl * kp_kp
    I_kp = I_kp_junc + I_kp_sl

    # --- Expressions for the I_Ks component ---
    eks = np.log((Ko + Nao * pNaK) / (pNaK * Na_i + K_i)) / FoRT
    gks_junc = 0.0035
    gks_sl = 0.0035
    xsss = 1.0 / (1.0 + 0.765928338365 * np.exp(-0.0701754385965 * V_m))
    tauxs = 990.1 / (1.0 + 0.841540408868 * np.exp(-0.070821529745 * V_m))
    d_states[4] = (xsss - x_ks) / tauxs
    I_ks_junc = Fjunc * gks_junc * x_ks**2 * (-eks + V_m)
    I_ks_sl = gks_sl * x_ks**2 * (-eks + V_m) * Fsl
    I_ks = I_ks_junc + I_ks_sl

    # --- Expressions for the I_to component ---
    GtoSlow = np.where(epi == 1.0, 0.0156, 0.037596)
    GtoFast = np.where(epi == 1.0, 0.1144, 0.001404)
    xtoss = 1.0 / (1.0 + np.exp(19.0 / 13.0 - V_m / 13.0))
    ytoss = 1.0 / (1.0 + 49.4024491055 * np.exp(V_m / 5.0))
    tauxtos = 0.5 + 9.0 / (1.0 + np.exp(1.0 / 5.0 + V_m / 15.0))
    tauytos = 30.0 + 800.0 / (1.0 + np.exp(6.0 + V_m / 10.0))
    d_states[5] = (xtoss - x_to_s) / tauxtos
    d_states[6] = (ytoss - y_to_s) / tauytos
    tauxtof = 0.5 + 8.5 * np.exp(-((9.0 / 10.0 + V_m / 50.0) ** 2))
    tauytof = 7.0 + 85.0 * np.exp(-((40.0 + V_m) ** 2) / 220.0)
    d_states[7] = (xtoss - x_to_f) / tauxtof
    d_states[8] = (ytoss - y_to_f) / tauytof
    I_tos = (-ek + V_m) * GtoSlow * x_to_s * y_to_s
    I_tof = (-ek + V_m) * GtoFast * x_to_f * y_to_f
    I_to = I_tof + I_tos

    # --- Expressions for the I_Ki component ---
    aki = 1.02 / (1.0 + 7.35454251046e-07 * np.exp(0.2385 * V_m - 0.2385 * ek))
    bki = (
        0.762624006506 * np.exp(0.08032 * V_m - 0.08032 * ek)
        + 1.15340563519e-16 * np.exp(0.06175 * V_m - 0.06175 * ek)
    ) / (1.0 + 0.0867722941577 * np.exp(0.5143 * ek - 0.5143 * V_m))
    kiss = aki / (aki + bki)
    I_ki = 0.150616019019 * np.sqrt(Ko) * (-ek + V_m) * kiss

    # --- Expressions for the I_ClCa component ---
    I_ClCa_junc = Fjunc * GClCa * (-ecl + V_m) / (1.0 + KdClCa / Ca_j)
    I_ClCa_sl = GClCa * (-ecl + V_m) * Fsl / (1.0 + KdClCa / Ca_sl)
    I_ClCa = I_ClCa_junc + I_ClCa_sl
    I_Clbk = GClB * (-ecl + V_m)

    # --- Expressions for the I_Ca component ---
    fss = 1.0 / (1.0 + np.exp(35.0 / 9.0 + V_m / 9.0)) + 0.6 / (
        1.0 + np.exp(5.0 / 2.0 - V_m / 20.0)
    )
    dss = 1.0 / (1.0 + np.exp(-5.0 / 6.0 - V_m / 6.0))
    taud = (1.0 - np.exp(-5.0 / 6.0 - V_m / 6.0)) * dss / (0.175 + 0.035 * V_m)
    tauf = 1.0 / (0.02 + 0.0197 * np.exp(-((0.48865 + 0.0337 * V_m) ** 2)))
    d_states[9] = (dss - d) / taud
    d_states[10] = (fss - f) / tauf
    d_states[11] = -0.0119 * f_Ca_Bj + 1.7 * (1.0 - f_Ca_Bj) * Ca_j
    d_states[12] = -0.0119 * f_Ca_Bsl + 1.7 * (1.0 - f_Ca_Bsl) * Ca_sl
    fcaCaMSL = 0.0
    fcaCaj = 0.0
    ibarca_j = (
        4.0
        * Frdy
        * pCa
        * (-0.341 * Cao + 0.341 * Ca_j * np.exp(2.0 * FoRT * V_m))
        * FoRT
        * V_m
        / (np.exp(2.0 * FoRT * V_m) - 1.0)
    )
    ibarca_sl = (
        4.0
        * Frdy
        * pCa
        * (-0.341 * Cao + 0.341 * Ca_sl * np.exp(2.0 * FoRT * V_m))
        * FoRT
        * V_m
        / (np.exp(2.0 * FoRT * V_m) - 1.0)
    )
    ibark = (
        Frdy
        * pK
        * (-0.75 * Ko + 0.75 * K_i * np.exp(FoRT * V_m))
        * FoRT
        * V_m
        / (np.exp(FoRT * V_m) - 1.0)
    )
    ibarna_j = (
        Frdy
        * pNa
        * (-0.75 * Nao + 0.75 * Na_j * np.exp(FoRT * V_m))
        * FoRT
        * V_m
        / (np.exp(FoRT * V_m) - 1.0)
    )
    ibarna_sl = (
        Frdy
        * pNa
        * (-0.75 * Nao + 0.75 * Na_sl * np.exp(FoRT * V_m))
        * FoRT
        * V_m
        / (np.exp(FoRT * V_m) - 1.0)
    )

    I_Ca_junc = (
        0.45 * Fjunc_CaL * Q10CaL**Qpow * (1.0 + fcaCaj - f_Ca_Bj) * d * f * ibarca_j
    )
    I_Ca_sl = (
        0.45 * Q10CaL**Qpow * (1.0 + fcaCaMSL - f_Ca_Bsl) * Fsl_CaL * d * f * ibarca_sl
    )
    I_CaK = (
        0.45
        * Q10CaL**Qpow
        * (Fjunc_CaL * (1.0 + fcaCaj - f_Ca_Bj) + (1.0 + fcaCaMSL - f_Ca_Bsl) * Fsl_CaL)
        * d
        * f
        * ibark
    )
    I_CaNa_junc = (
        0.45 * Fjunc_CaL * Q10CaL**Qpow * (1.0 + fcaCaj - f_Ca_Bj) * d * f * ibarna_j
    )
    I_CaNa_sl = (
        0.45 * Q10CaL**Qpow * (1.0 + fcaCaMSL - f_Ca_Bsl) * Fsl_CaL * d * f * ibarna_sl
    )

    # --- Expressions for the I_NCX component ---
    s1_junc = Cao * Na_j**3 * np.exp(nu * FoRT * V_m)
    s2_junc = Nao**3 * Ca_j * np.exp((-1.0 + nu) * FoRT * V_m)
    s3_junc = (
        Cao * Na_j**3
        + KmCao * Na_j**3
        + Nao**3 * Ca_j
        + KmCai * Nao**3 * (1.0 + Na_j**3 / KmNai**3)
        + KmNao**3 * (1.0 + Ca_j / KmCai) * Ca_j
    )

    s1_sl = Cao * Na_sl**3 * np.exp(nu * FoRT * V_m)
    s2_sl = Nao**3 * Ca_sl * np.exp((-1.0 + nu) * FoRT * V_m)
    s3_sl = (
        Cao * Na_sl**3
        + KmCao * Na_sl**3
        + Nao**3 * Ca_sl
        + KmCai * Nao**3 * (1.0 + Na_sl**3 / KmNai**3)
        + KmNao**3 * (1.0 + Ca_sl / KmCai) * Ca_sl
    )

    Ka_junc = 1.0 / (1.0 + Kdact**2 / Ca_j**2)
    Ka_sl = 1.0 / (1.0 + Kdact**2 / Ca_sl**2)

    I_ncx_junc = (
        Fjunc
        * IbarNCX
        * Q10NCX**Qpow
        * (-s2_junc + s1_junc)
        * Ka_junc
        / ((1.0 + ksat * np.exp((-1.0 + nu) * FoRT * V_m)) * s3_junc)
    )
    I_ncx_sl = (
        IbarNCX
        * Q10NCX**Qpow
        * (-s2_sl + s1_sl)
        * Fsl
        * Ka_sl
        / ((1.0 + ksat * np.exp((-1.0 + nu) * FoRT * V_m)) * s3_sl)
    )

    # --- Expressions for the I_PCa component ---
    I_pca_junc = (
        Fjunc * IbarSLCaP * Q10SLCaP**Qpow * Ca_j**1.6 / (KmPCa**1.6 + Ca_j**1.6)
    )
    I_pca_sl = IbarSLCaP * Q10SLCaP**Qpow * Ca_sl**1.6 * Fsl / (KmPCa**1.6 + Ca_sl**1.6)

    # --- Expressions for the I_CaBK component ---
    I_cabk_junc = Fjunc * GCaB * (-eca_junc + V_m)
    I_cabk_sl = GCaB * (-eca_sl + V_m) * Fsl

    # ---  Expressions for the SR Fluxes component ---
    kCaSR = MaxSR - (MaxSR - MinSR) / (1.0 + (ec50SR / Ca_sr) ** 2.5)
    koSRCa = koCa / kCaSR
    kiSRCa = kiCa * kCaSR
    RI = 1.0 - Ry_Ri - Ry_Ro - Ry_Rr

    d_states[13] = (
        kim * RI + kom * Ry_Ro - Ca_j**2 * Ry_Rr * koSRCa - Ca_j * Ry_Rr * kiSRCa
    )
    d_states[14] = (
        kim * Ry_Ri - kom * Ry_Ro + Ca_j**2 * Ry_Rr * koSRCa - Ca_j * Ry_Ro * kiSRCa
    )
    d_states[15] = (
        -kim * Ry_Ri - kom * Ry_Ri + Ca_j**2 * RI * koSRCa + Ca_j * Ry_Ro * kiSRCa
    )

    J_SRCarel = ks * (-Ca_j + Ca_sr) * Ry_Ro
    J_serca = (
        Vmax_SRCaP
        * Q10SRCaP**Qpow
        * ((Ca_i / Kmf) ** hillSRCaP - (Ca_sr / Kmr) ** hillSRCaP)
        / (1.0 + (Ca_i / Kmf) ** hillSRCaP + (Ca_sr / Kmr) ** hillSRCaP)
    )
    J_SRleak = 5.348e-06 * Ca_sr - 5.348e-06 * Ca_j

    # --- Expressions for the Na Buffers component ---
    d_states[16] = -koff_na * Na_Bj + kon_na * (Bmax_Naj - Na_Bj) * Na_j
    d_states[17] = -koff_na * Na_Bsl + kon_na * (Bmax_Nasl - Na_Bsl) * Na_sl

    # --- Expressions for the Cytosolic Ca Buffers component ---
    d_states[18] = -koff_tncl * Tn_CL + kon_tncl * (Bmax_TnClow - Tn_CL) * Ca_i
    d_states[19] = (
        -koff_tnchca * Tn_CHc + kon_tnchca * (Bmax_TnChigh - Tn_CHc - Tn_CHm) * Ca_i
    )
    d_states[20] = -koff_tnchmg * Tn_CHm + Mgi * kon_tnchmg * (
        Bmax_TnChigh - Tn_CHc - Tn_CHm
    )
    d_states[21] = -koff_cam * CaM + kon_cam * (Bmax_CaM - CaM) * Ca_i
    d_states[22] = (
        -koff_myoca * Myo_c + kon_myoca * (Bmax_myosin - Myo_c - Myo_m) * Ca_i
    )
    d_states[23] = -koff_myomg * Myo_m + Mgi * kon_myomg * (Bmax_myosin - Myo_c - Myo_m)
    d_states[24] = -koff_sr * SRB + kon_sr * (Bmax_SR - SRB) * Ca_i

    J_CaB_cytosol = (
        -koff_cam * CaM
        - koff_myoca * Myo_c
        - koff_myomg * Myo_m
        - koff_sr * SRB
        - koff_tnchca * Tn_CHc
        - koff_tnchmg * Tn_CHm
        - koff_tncl * Tn_CL
        + Mgi * kon_myomg * (Bmax_myosin - Myo_c - Myo_m)
        + Mgi * kon_tnchmg * (Bmax_TnChigh - Tn_CHc - Tn_CHm)
        + kon_cam * (Bmax_CaM - CaM) * Ca_i
        + kon_myoca * (Bmax_myosin - Myo_c - Myo_m) * Ca_i
        + kon_sr * (Bmax_SR - SRB) * Ca_i
        + kon_tnchca * (Bmax_TnChigh - Tn_CHc - Tn_CHm) * Ca_i
        + kon_tncl * (Bmax_TnClow - Tn_CL) * Ca_i
    )

    # --- Expressions for the Junctional and SL Ca Buffers component ---
    Bmax_SLlowsl = Bmax_SLlowsl0 * Vmyo / Vsl
    Bmax_SLlowj = Bmax_SLlowj0 * Vmyo / Vjunc
    Bmax_SLhighsl = Bmax_SLhighsl0 * Vmyo / Vsl
    Bmax_SLhighj = Bmax_SLhighj0 * Vmyo / Vjunc
    d_states[25] = -koff_sll * SLL_j + kon_sll * (-SLL_j + Bmax_SLlowj) * Ca_j
    d_states[26] = -koff_sll * SLL_sl + kon_sll * (-SLL_sl + Bmax_SLlowsl) * Ca_sl
    d_states[27] = -koff_slh * SLH_j + kon_slh * (-SLH_j + Bmax_SLhighj) * Ca_j
    d_states[28] = -koff_slh * SLH_sl + kon_slh * (-SLH_sl + Bmax_SLhighsl) * Ca_sl
    J_CaB_junction = (
        -koff_slh * SLH_j
        - koff_sll * SLL_j
        + kon_slh * (-SLH_j + Bmax_SLhighj) * Ca_j
        + kon_sll * (-SLL_j + Bmax_SLlowj) * Ca_j
    )
    J_CaB_sl = (
        -koff_slh * SLH_sl
        - koff_sll * SLL_sl
        + kon_slh * (-SLH_sl + Bmax_SLhighsl) * Ca_sl
        + kon_sll * (-SLL_sl + Bmax_SLlowsl) * Ca_sl
    )

    # --- Expressions for the SR Ca Concentrations component ---
    Bmax_Csqn = Bmax_Csqn0 * Vmyo / Vsr
    d_states[29] = -koff_csqn * Csqn_b + kon_csqn * (-Csqn_b + Bmax_Csqn) * Ca_sr
    d_states[30] = (
        -J_SRCarel
        + koff_csqn * Csqn_b
        - kon_csqn * (-Csqn_b + Bmax_Csqn) * Ca_sr
        - J_SRleak * Vmyo / Vsr
        + J_serca
    )

    # --- Expressions for the Na Concentrations component ---
    I_Na_tot_junc = (
        3.0 * I_nak_junc + 3.0 * I_ncx_junc + I_CaNa_junc + I_Na_junc + I_nabk_junc
    )
    I_Na_tot_sl = 3.0 * I_nak_sl + 3.0 * I_ncx_sl + I_CaNa_sl + I_Na_sl + I_nabk_sl

    d_states[31] = (
        -d_states[16]
        + J_na_juncsl * (-Na_j + Na_sl) / Vjunc
        - Cmem * I_Na_tot_junc / (Frdy * Vjunc)
    )
    d_states[32] = (
        -d_states[17]
        + J_na_juncsl * (-Na_sl + Na_j) / Vsl
        + J_na_slmyo * (-Na_sl + Na_i) / Vsl
        - Cmem * I_Na_tot_sl / (Frdy * Vsl)
    )
    d_states[33] = J_na_slmyo * (-Na_i + Na_sl) / Vmyo

    # --- Expressions for the K Concentration component ---
    I_K_tot = -2.0 * I_nak + I_CaK + I_ki + I_kp + I_kr + I_ks + I_to
    d_states[34] = 0.0

    # --- Expressions for the Ca Concentrations component ---
    I_Ca_tot_junc = -2.0 * I_ncx_junc + I_Ca_junc + I_cabk_junc + I_pca_junc
    I_Ca_tot_sl = -2.0 * I_ncx_sl + I_Ca_sl + I_cabk_sl + I_pca_sl

    d_states[35] = (
        -J_CaB_junction
        + J_ca_juncsl * (-Ca_j + Ca_sl) / Vjunc
        + J_SRCarel * Vsr / Vjunc
        + J_SRleak * Vmyo / Vjunc
        - Cmem * I_Ca_tot_junc / (2.0 * Frdy * Vjunc)
    )
    d_states[36] = (
        -J_CaB_sl
        + J_ca_juncsl * (-Ca_sl + Ca_j) / Vsl
        + J_ca_slmyo * (-Ca_sl + Ca_i) / Vsl
        - Cmem * I_Ca_tot_sl / (2.0 * Frdy * Vsl)
    )
    d_states[37] = (
        -J_CaB_cytosol + J_ca_slmyo * (-Ca_i + Ca_sl) / Vmyo - J_serca * Vsr / Vmyo
    )

    # --- Expressions for the Membrane potential component
    I_Na_tot = I_Na_tot_junc + I_Na_tot_sl
    I_Cl_tot = I_ClCa + I_Clbk
    I_Ca_tot = I_Ca_tot_junc + I_Ca_tot_sl

    I_tot = I_Ca_tot + I_Cl_tot + I_K_tot + I_Na_tot

    return I_tot


def step_grandi(states, V_m, GNa, dt, d_states):
    """
    Solves the Grandi ODE system over a timestep dt using pure Forward Euler sub-stepping.
    """
    dt_ode = min(0.001, dt)
    num_substeps = int(np.round(dt / dt_ode))

    #d_states = np.zeros_like(states)
    I_tot = np.zeros_like(V_m)

    for _ in range(num_substeps):
        # Calculate RHS and get current (updates d_states in place)
        I_tot = grandi_rhs(states, V_m, GNa, d_states)
        # Forward Euler update
        states += dt_ode * d_states

    return I_tot
