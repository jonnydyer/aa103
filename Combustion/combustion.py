import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
from matplotlib.ticker import FormatStrFormatter
rc('figure', figsize=(4,2.5))
rc('legend', fontsize='small')
rc('font', family='serif')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

C_SSME = 4400.
T_SSME = 2279e3
M_SSME = 3527.
mdot_SSME = T_SSME / C_SSME

C_NERVA = 8.3e3
tb_NERVA = 1200.
T_NERVA = 333.6e3
M_NERVA = 34000.
M0_NERVA = 178000.
mdot_NERVA = T_NERVA / C_NERVA

print 'SSME power density: %.3f MW/kg' % (C_SSME * T_SSME / M_SSME / 1e6)
print 'SSME energy density: %.3f MW/kg' % (C_SSME * T_SSME / mdot_SSME / 1e6)

print 'NERVA power density: %.3f MW/kg' % (C_NERVA * T_NERVA / M_NERVA / 1e6)
print 'NERVA energy density: %.3f MW/kg' % (C_NERVA * T_NERVA / mdot_NERVA / 1e6)
