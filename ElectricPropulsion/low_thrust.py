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

mu = 3.986e14             #m^3/s^2
r_e = 6.3781e6            #m
g0 = 9.81                 # m/s^2

alt = 500e3
P = 250.
eta_p = 0.4
Isp = 1000.
C = g0 * Isp

r0 = alt + r_e

r_r0 = np.logspace(-1, 3)
# SEe https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-522-space-propulsion-spring-2015/lecture-notes/MIT16_522S15_Lecture6.pdf
delV_delV_hohm = (np.sqrt(2 * (1 + 2. * np.sqrt(r_r0)/(r_r0 + 1))) - 1)**(-1)

plt.semilogx(r_r0, delV_delV_hohm)
plt.xlabel(r'$\frac{r}{r_0}$')
plt.ylabel(r'$\frac{\Delta V}{\Delta V_{H}}$')
plt.tight_layout(True)
plt.gcf().savefig('../imgs/low_thrust_climb.pdf')

plt.show()
