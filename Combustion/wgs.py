import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
rc('figure', figsize=(4,2.5))
rc('legend', fontsize='small')
rc('font', family='serif')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

with open('JANAF_H2O_g.txt', 'r') as f:
    h2o_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_CO2_g.txt', 'r') as f:
    co2_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_H2_g.txt', 'r') as f:
    h2_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

with open('JANAF_CO_g.txt', 'r') as f:
    co_tbl = pd.read_csv(f, sep='\t', header=1, na_values='INFINITE')

def f_T(tbl, T, name):
    return np.interp(T, tbl['T(K)'], tbl[name])

N_CO2 = 1
N_H2 = 1
N_CO = 1
N_H2O = 1

T = np.linspace(300, 4000)

K_p = 10**(N_CO2 * f_T(co2_tbl, T, 'log Kf') + N_H2 * f_T(h2_tbl, T, 'log Kf') -
       N_CO * f_T(co_tbl, T, 'log Kf') - N_H2O * f_T(h2o_tbl, T, 'log Kf'))

X_CO = 1. / (np.sqrt(K_p) + 1)
X_CO2 = 1- X_CO
X_H2 = X_CO2
X_H2O = X_CO

f = plt.figure()
plt.plot(T, np.log10(K_p))
plt.xlabel('T (K)')
plt.ylabel(r'$\log_{10}K_p$')
plt.tight_layout(True)
f.savefig('../imgs/wgs_Kp.pdf')

f = plt.figure()
plt.plot(T, X_CO, label='CO')
plt.plot(T, X_CO2, label='CO2')
plt.plot(T, X_H2O, '--', label='H2O')
plt.plot(T, X_H2, '--', label='H2')
plt.xlabel('T (K)')
plt.ylabel(r'$X_i$')
plt.legend()
plt.tight_layout(True)
f.savefig('../imgs/wgs_Xi.pdf')
plt.show()
