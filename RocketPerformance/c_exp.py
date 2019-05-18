import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
rc('figure', figsize=(6,3.5))
rc('legend', fontsize='small')
rc('font', family='serif')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

def fix_fig(f):
    for a in f.get_axes():
        a.spines['right'].set_visible(False)
        a.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        #a.yaxis.set_ticks_position('left')
        a.xaxis.set_ticks_position('bottom')
    f.set_tight_layout(True)

Ru = 8314.
gamma = [1.1, 1.2, 1.3]
Pe_Pt = 1./ np.array([10, 50, 100])

T_Mw = np.linspace(50, 250)

c = ['r', 'g', 'b']
ls = ['-', '-.', '--']

for i,g in enumerate(gamma):
    for j,pp in enumerate(Pe_Pt):
        C = np.sqrt((2 * g)/(g - 1) * Ru * T_Mw * (1 - pp**((g - 1) / g)))
        plt.plot(T_Mw, C / 9.81, ls=ls[i], c=c[j], label=r'$P_e/P_t=%d, \gamma=%.2f$' % (1./pp, g))

plt.legend([r'$P_e/P_t=%d$' % (1./Pe_Pt[0]),
            r'$P_e/P_t=%d$' % (1./Pe_Pt[1]),
            r'$P_e/P_t=%d$' % (1./Pe_Pt[2])])
plt.xlabel(r'$T_t/M_w$')
plt.ylabel(r'$I_{sp}$')
plt.tight_layout(True)
plt.gcf().savefig('imgs/C_exp.svg')
plt.show()
