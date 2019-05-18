import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
rc('figure', figsize=(4,2.5))
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

gamma = 1.2
Ru_Cp = 1. - 1. / gamma

Pt_Pe = np.linspace(5, 100)

eta_therm = gamma / (gamma - 1) * Ru_Cp * (1 - (1./Pt_Pe)**((gamma - 1)/gamma))

eta_carnot = 1. - (1. / Pt_Pe)**((gamma - 1)/gamma)

plt.plot(Pt_Pe, eta_therm, label='Rocket Calculation')
plt.xlabel(r'$P_t/P_e$')
plt.ylabel(r'$\eta_{thermal}$')
plt.tight_layout(True)
plt.gcf().savefig('imgs/eta_therm.pdf')

plt.show()
