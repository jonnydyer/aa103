import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import pypropep as ppp
ppp.init()
rc('figure', figsize=(4,2.5))
rc('legend', fontsize='small')
rc('font', family='serif')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

with open('JANAF_H2O_g.txt', 'r') as f:
    h2o_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_CO2_g.txt', 'r') as f:
    co2_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_O2_g.txt', 'r') as f:
    o2_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_CH4_g.txt', 'r') as f:
    ch4_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

def f_T(tbl, T, name):
    return np.interp(T, tbl['T(K)'], tbl[name])

N_CO2 = 1
N_H2O = 2
N_CH4 = 1
N_O2 = 2
delta_H_rxn = 800      # kJ/mol

T = np.linspace(400, 6000)

delta_H_sens = (N_CO2 * f_T(co2_tbl, T, 'H-H(Tr)') +
                N_H2O * f_T(h2o_tbl, T, 'H-H(Tr)'))


Log_K_p = (N_CO2 * f_T(co2_tbl, T, 'log Kf') + N_H2O * f_T(h2o_tbl, T, 'log Kf') -
       N_CH4 * f_T(ch4_tbl, T, 'log Kf') + N_O2 * f_T(o2_tbl, T, 'log Kf'))

equil = ppp.Equilibrium()
equil.add_propellants([(ppp.PROPELLANTS['OXYGEN (GAS)'], N_O2),
                       (ppp.PROPELLANTS['METHANE'], N_CH4)])
comp = {'H2O': [], 'H': [],'H2': [], #'OH': [], 'O2': [],
        'O':[], 'CO2': [], 'CO': []}
for i, Ti in enumerate(T):
    equil.set_state(P=1, T=Ti, type='TP')
    for k in comp:
        comp[k].append(equil.composition[k])

f = plt.figure()
for k in comp:
    plt.plot(T, comp[k], label=k)
plt.legend(loc='upper left')
plt.xlabel('T(K)')
plt.ylabel(r'$n_i$')
plt.tight_layout(True)
f.savefig('../imgs/ch4_o2_full_composition.pdf')

#f = plt.figure()
#plt.plot(T, delta_H_sens, label=r'$\Delta H_{sens}$')
#plt.axhline(delta_H_rxn, c='r', label=r'$\Delta H_{rxn}^\circ$')
#plt.axvline(298.15, c='g', ls='--', label=r'$T_{ref}$')
#plt.plot(5200, 800, 'y*')
#plt.legend()
#plt.xlabel('T(K)')
#plt.ylabel(r'$\Delta H (kJ)$')
#plt.tight_layout(True)
#
#f.savefig('../imgs/adiabatic_naive.pdf')
f = plt.figure()
plt.plot(T, Log_K_p)
plt.xlabel('T (K)')
plt.ylabel(r'$\log(K_p)$')
plt.tight_layout(True)
f.savefig('../imgs/Kp_ch4_o2.pdf')

plt.show()
