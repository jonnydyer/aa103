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

ml_mi_v = np.arange(0.1, 0.7, 10)

alpha = 1000.
eta = 0.5
tb = 100000.
vc = np.sqrt(2 * alpha * eta * tb)
C = np.linspace(0.5, 2) * vc
print(vc)

for i, ml_mi in enumerate(ml_mi_v):

