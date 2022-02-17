#!/usr/local/bin/python3.9

'''
Change Log
=========
0.0.1 (2022-02-08)
Initial Commit
'''

import matplotlib.pyplot as plt
import numpy as np

# Set Parameters
fontdict= {'fontsize': 14, 'fontweight': 'bold'}
bbox={'facecolor':'0.8', 'pad':5}
#colors = ['yellow', 'cyan', 'blue', 'red', 'teal']
plt.style.use('fivethirtyeight')

# Define Labels and Sizes
labels = ['HHS','DOD','DOE','NSF','NASA','DHS','USDA','DOT','DOC','ED','EPA']
sizes = np.array([1.02,1.571,0.267,0.188,0.162,0.021,0.021,0.011,0.010,0.010,0.005])

# Plot Pie Chart Option 1
fig, ax1 = plt.subplots(figsize=(5,5))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
ax1.set_title('Investment Weight Targets', fontdict=fontdict, bbox=bbox)
plt.tight_layout()
plt.legend()
plt.show()
