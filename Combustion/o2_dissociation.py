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

with open('JANAF_O2_g.txt', 'r') as f:
    o2_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_O_g.txt', 'r') as f:
    o_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

def f_T(tbl, T, name):
    return np.interp(T, tbl['T(K)'], tbl[name])

R = 8.314
Tref = 298.15
Pref = 1e5
Rref = Pref / R / Tref
T = np.linspace(500, 6000, 30)

# O2 <-> 2O
N_O = 2
N_O2 = 1
log_K_p = (N_O * f_T(o_tbl, T, 'log Kf') + N_O2 * f_T(o2_tbl, T, 'log Kf'))
K_p = 10**log_K_p
n_o = 0.5 * (np.sqrt(K_p)*np.sqrt(K_p + 4) - K_p)
n_o2 = 1. - n_o

equil = ppp.Equilibrium()
equil.add_propellants([(ppp.PROPELLANTS['OXYGEN (GAS)'], N_O2)])
comp = {'O2': [], 'O':[]}
for i, Ti in enumerate(T):
    equil.set_state(P=1, T=Ti, type='TP')
    for k in comp:
        comp[k].append(equil.composition[k])

f = plt.figure()
for k in comp:
    plt.plot(T, comp[k], label=k)
plt.legend()

f = plt.figure()
plt.plot(T, n_o, label='O')
plt.plot(T, n_o2, label='O2')
plt.legend()

f = plt.figure()
plt.semilogy(T, K_p)
plt.xlabel('T (K)')
plt.ylabel(r'$K_p$')
plt.tight_layout(True)
#f.savefig('../imgs/Kp_h2o_formation.pdf')
plt.show()
