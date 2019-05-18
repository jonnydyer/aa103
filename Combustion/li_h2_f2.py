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


li = ppp.PROPELLANTS['LITHIUM (PURE CRYSTALINE)']
f2 = ppp.PROPELLANTS['FLUORINE (LIQUID)']
h2 = ppp.PROPELLANTS['HYDROGEN (GASEOUS)']

Pt = 70.
Pe = .01

OF = np.linspace(2, 4)
C = np.zeros([len(OF), 2])
T = np.zeros_like(OF)

for i in range(len(OF)):
    fp = ppp.FrozenPerformance()

    m_f2 = 0.2
    m_h2 = OF[i]
    m_Li = 0.3

    fp.add_propellants([(li, m_Li),
                        (h2, m_h2),
                        (f2, m_f2)])

    fp.set_state(P=Pt, Pe=Pe)

    T[i] = fp.properties[0].T

    C[i] = fp.performance.Isp

f = plt.figure()
plt.title('Lithium/Fluorine/Hydrogen System')
plt.plot(OF / (OF + 0.5), C)
plt.xlabel(r'$\frac{\dot{m}_{H2}}{\dot{m}}$')
plt.ylabel(r'$C$ (m/s)')
plt.tight_layout(True)
f.savefig('../imgs/li_f2_h2.pdf')
plt.show()

