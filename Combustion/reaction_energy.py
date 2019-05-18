from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate
from matplotlib import rc

rc('figure', figsize=(6,3))
rc('legend', fontsize='small')
rc('font', family='serif')

def fix_fig(f):
    for a in f.get_axes():
        a.spines['right'].set_visible(False)
        a.spines['top'].set_visible(False)
        # Only show ticks on the left and bottom spines
        #a.yaxis.set_ticks_position('left')
        a.xaxis.set_ticks_position('bottom')
    f.set_tight_layout(True)

phi = [-3., 3., 4., 6., 13.]
E =   [6., 6., 10., 2., 2.]

nn = interpolate.interp1d(phi, E, kind='linear')

phi_i = np.linspace(-3, 13, 1000)
sigma = 0.5
conv_i = np.exp(-(phi_i-5.)**2 / sigma**2)
conv_i /= np.sum(conv_i)
E_i = nn(phi_i)
E_i = np.convolve(E_i, conv_i, mode='same')

f = plt.figure()
#plt.plot(phi, E, 'x')
plt.plot(phi_i/10, E_i, 'r')
plt.xlim(0,1)
fix_fig(f)

plt.show()
