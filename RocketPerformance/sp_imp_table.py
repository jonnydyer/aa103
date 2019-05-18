import numpy as np

gamma = 1.4
Ru = 8.314
M = .028              # kg / mol
Tt = 298              # K
P0_Pt = 0.1
Pe_P0 = 1.

def cstar_f(M, Tt, gamma):
    R = Ru / M
    return np.sqrt(R * Tt / gamma) * ((gamma + 1) / 2)**((gamma + 1.) / 2 / (gamma - 1.))

def Me2_f(Pe_Pt, gamma):
    return 2. * (Pe_Pt**((1 - gamma)/gamma) - 1) / (gamma - 1)

def Ae_Ac_f(Me, gamma):
    return (((gamma + 1.) / 2.)**((gamma + 1)/-2./(gamma - 1)) / Me *
            (1. + (gamma - 1) / 2. * Me**2)**((gamma + 1)/2./(gamma - 1)))

def Cf_f(Pe_Pt, P0_Pt, Ae_Ac, Me):
    return ((Pe_Pt - P0_Pt) * Ae_Ac + (gamma * Me / np.sqrt(1 + (gamma - 1.) / 2 * Me**2) *
            ((gamma + 1) / 2)**((gamma + 1.) / 2 / (1. - gamma))))

def compute_table(namesv, gammav, Mwv):
    tbl = '\\begin{table*}[h]\n\\centering\n\\begin{tabular}{llllll}\n\\toprule\n'
    tbl += 'Name & $\\gamma$ & $M_w$ & $c^*$ (m/s) & $C_f$ & $C$ (m/s) \\\\\n\\midrule\n'
    for i, n in enumerate(namesv):
        cstar = cstar_f(Mwv[i], Tt, gammav[i])
        Me = np.sqrt(Me2_f(Pe_P0 * P0_Pt, gammav[i]))
        Ae_Ac = Ae_Ac_f(Me, gammav[i])
        Cf = Cf_f(Pe_P0 * P0_Pt, P0_Pt, Ae_Ac, Me)
        C = cstar * Cf
        tbl += '%s & %.2f & %.0f & %.1f & %.2f & %.1f \\\\\n' % (namesv[i],
                                                                 gammav[i],
                                                                 Mwv[i]*1e3,
                                                                 cstar,
                                                                 Cf,
                                                                 C)
    tbl += '\n\\bottomrule\n\\end{tabular}\n'
    tbl += '''
        \n\caption{$c^*$, $C_f$, $C$ for several pure gasses at room temperature,
        $P_e/P_0 = 1$ and $P_0/P_t = 0.1$. Note how $C_f$ is essentially
        constant despite the differences in gas properties while $c^*$ and
        $C$ vary substantially.}\n
        \\end{table*}'''
    return tbl

names = ['$N_2$', '$H_2$', 'He']
gammav = [1.4, 1.41, 1.66]
Mwv = [0.028, .002, .004]

print compute_table(names, gammav, Mwv)
