import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
rc('figure', figsize=(4,2.5))
rc('legend', fontsize='small')
rc('font', family='serif')
#rc('xtick', labelsize='small')
#rc('ytick', labelsize='small')

def fix_fig(f):
    for a in f.get_axes():
        a.spines['right'].set_visible(False)
        a.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        #a.yaxis.set_ticks_position('left')
        a.xaxis.set_ticks_position('bottom')
    f.set_tight_layout(True)

gamma = 1.4
P0_Pt = 0.1
Pe_P0 = 1.

Me = np.linspace(1, 2.8)

Ae_Ac = (((gamma + 1.) / 2.)**((gamma + 1)/-2./(gamma - 1)) / Me *
            (1. + (gamma - 1) / 2. * Me**2)**((gamma + 1)/2./(gamma - 1)))

Pe_Pt = (1. + (gamma - 1.)/2. * Me**2)**(-gamma / (gamma - 1))

Cf_mom = (gamma * Me / np.sqrt(1 + (gamma - 1.) / 2 * Me**2) *
            ((gamma + 1) / 2)**((gamma + 1.) / 2 / (1. - gamma)))

Cf_mom = (np.sqrt(2 * gamma**2 / (gamma - 1) * (2 / (gamma + 1))**((gamma + 1)/(gamma - 1)) *
            (1. - Pe_Pt**((gamma - 1) / gamma))))

Cf_press = (Pe_Pt - P0_Pt) * Ae_Ac

P0_Pe = P0_Pt / Pe_Pt

def do_plots(figsize):
    f = plt.figure(figsize=figsize)
    plt.subplot(311)
    plt.title(r'$\frac{P_0}{P_t} = %.1f$' % P0_Pt)

    plt.plot(P0_Pe, Cf_mom, 'g--', label='Cf (momentum)')

    ax1 = plt.gca()
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax1.set_ylabel(r'$\frac{U_e}{c^*}$', color='g')
    ax1.set_yticks(np.linspace(np.min(Cf_mom), np.max(Cf_mom), 6))
    ax1.set_xticks(np.linspace(0, 2, 3))
    ax1.tick_params('y', colors='g')
    plt.axvline(1, c='r', ls=':')

    ax2 = plt.twinx()
    ax2.plot(P0_Pe, Cf_press, 'b--')
    ax2.set_yticks(np.linspace(np.min(Cf_press), np.max(Cf_press), 6))
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax2.set_ylabel(r'$\left(1 - \frac{P_0}{P_e}\right)\frac{P_e A_e}{P_t A^*}$', color='b')
    ax2.tick_params('y', colors='b')

    #f.legend()

    plt.subplot(312, sharex=ax1)
    plt.plot(P0_Pe, Cf_mom + Cf_press, label='Cf')
    plt.axvline(1, c='r', ls=':')
    plt.ylabel(r'$C_f$')

    plt.subplot(313, sharex=ax1)
    plt.plot(P0_Pe, Ae_Ac)
    plt.ylabel(r'$\frac{A_e}{A_c}$')
    plt.xlabel(r'$P_0/P_e$')
    fix_fig(f)
    f.savefig('imgs/Cf_%d_%d.pdf' % (figsize[0], figsize[1]))

do_plots(figsize=(5,7))
do_plots(figsize=(8, 10))

plt.show()
