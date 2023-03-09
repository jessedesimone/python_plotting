#!/usr/local/bin/python3.9

import seaborn as sns
import numpy as np
np.random.seed(12345678)
data = np.random.normal(loc=0, scale=3.0, size=10000)

import scipy.stats as stats
import pylab
stats.probplot(data, dist="norm", plot=pylab)
plt.title("Normal Q-Q Plot")
pylab.show()