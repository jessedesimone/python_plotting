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
labels = ['Large Cap', 'Mid Cap', 'Small Cap', 'Bond']
sizes = np.array([60, 20, 10, 10])

# Plot Pie Chart Option 1
fig, ax1 = plt.subplots(figsize=(5,5))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=False, startangle=90)
ax1.set_title('Investment Weight Targets', fontdict=fontdict, bbox=bbox)
plt.tight_layout()
#plt.legend()
plt.show()
