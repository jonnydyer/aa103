from matplotlib import pyplot as plt
import numpy as np
from matplotlib import rc
import pypropep as ppp
ppp.init()
rc('figure', figsize=(4,2.5))
rc('legend', fontsize='small')
rc('font', family='serif')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

Ru = 8.314e3

ch4 = ppp.PROPELLANTS['METHANE']
ch4 = ppp.PROPELLANTS['HYDROGEN (GASEOUS)']
o2 = ppp.PROPELLANTS['OXYGEN (GAS)']

Pt = 70.
Pe = 1.

OF = np.linspace(1, 8)
cstar = np.zeros([len(OF), 2])
Cf = np.zeros([len(OF), 2])
C = np.zeros([len(OF), 2])
T = np.zeros_like(OF)
gamma = np.zeros_like(OF)
Mw = np.zeros_like(OF)
species = {'H2O': [], 'H': [],'H2': [], 'OH': [], 'O2': [],
        'O':[], 'CO2': [], 'CO': []}

c = ['r', 'b', 'g', 'm', 'c', 'y', 'r', 'b']

comp = (dict(species), dict(species), dict(species))
print comp

for i in range(len(OF)):
    fp = ppp.FrozenPerformance()
    sp = ppp.ShiftingPerformance()

    m_o2 = OF[i]
    m_ch4 = 1.0

    fp.add_propellants_by_mass([(ch4, m_ch4), (o2, m_o2)])
    sp.add_propellants_by_mass([(ch4, m_ch4), (o2, m_o2)])

    fp.set_state(P=Pt, Pe=Pe)
    sp.set_state(P=Pt, Pe=Pe)

    T[i] = fp.properties[0].T
    gamma[i] = fp.properties[0].Isex
    Mw[i] = fp.properties[0].M

#    for k in species:
#        comp[0][k].append(sp.composition['chamber'][k])
#        comp[1][k].append(sp.composition['throat'][k])
#        comp[2][k].append(sp.composition['exit'][k])

    cstar[i,0] = fp.performance.cstar
    cstar[i,1] = sp.performance.cstar

    C[i,0] = fp.performance.Isp
    C[i,1] = sp.performance.Isp

    Cf[i,0] = fp.performance.cf
    Cf[i,1] = sp.performance.cf

C_ideal = np.sqrt(2 * gamma / (gamma - 1) * Ru * T / Mw * (1 - (Pe/Pt)**((gamma - 1)/gamma)))
cstar_ideal = np.sqrt(Ru * T / gamma / Mw) * ((gamma + 1)/2)**((gamma + 1)/(2*(gamma - 1)))

f = plt.figure()
plt.plot(OF, cstar[:,0], label='Frozen')
plt.plot(OF, cstar[:,1], label='Shifting')
plt.xlabel('O/F')
plt.ylabel(r'$c^*$ (m/s)')
plt.tight_layout(True)
plt.legend()
#f.savefig('../imgs/cstar_ppp.pdf')

f = plt.figure()
plt.plot(OF, C[:,0], label='Frozen')
plt.plot(OF, C[:,1], label='Shifting')
plt.xlabel('O/F')
plt.ylabel(r'$C$ (m/s)')
plt.tight_layout(True)
plt.legend()
#f.savefig('../imgs/C_ppp.pdf')

f = plt.figure()
plt.plot(OF, Cf[:,0], label='Frozen')
plt.plot(OF, Cf[:,1], label='Shifting')
plt.xlabel('O/F')
plt.ylabel(r'$C_f$')
plt.tight_layout(True)
plt.legend()
#f.savefig('../imgs/Cf_ppp.pdf')

f = plt.figure()
plt.plot(OF, T)
plt.xlabel('O/F')
plt.ylabel(r'$T_t (K)$')
plt.tight_layout(True)
#f.savefig('../imgs/Tt_ppp.pdf')

f = plt.figure()
plt.plot(OF, gamma)
plt.xlabel('O/F')
plt.ylabel(r'$\gamma$')
plt.tight_layout(True)
#f.savefig('../imgs/gamma_ppp.pdf')

f = plt.figure()
plt.plot(OF, C[:, 0]/C_ideal, label=r'$\frac{C}{C_{ideal}}$')
plt.plot(OF, cstar[:, 0]/cstar_ideal, label=r'$\frac{c^*}{c^*_{ideal}}$')
plt.xlabel('O/F')
plt.ylabel('Ratio')
plt.tight_layout(True)
plt.legend()
#f.savefig('../imgs/fzn_ideal_ppp.pdf')

plt.show()
