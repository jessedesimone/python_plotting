#!/usr/local/bin/python3.9
"""
Copyright (C) 2021 Jesse DeSimone, Ph.D.

Change Log
=============
0.0.1 (2021-10-04)
-------------
Initial commit

"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/jessedesimone/DeSimone_Github/python_stats/Datasets/diabetes.csv")

sns.set_palette(sns.color_palette("Set1", 8))
plt.figure(figsize=(15,7))
plt.title('Feature Correlation Matrix', weight='bold', fontsize=16)
sns.heatmap(df.corr(),annot=True,vmin=-1,vmax=1,cmap='viridis')
plt.show()
plt.tight_layout()

sns.set_context('paper')
f, ax = plt.subplots(figsize=(10, 7))
cor = df.corr()
plt.title('Feature Correlation Matrix', weight='bold', fontsize=20)
ax = sns.heatmap(cor, vmax=1, annot=True, cmap=sns.color_palette("coolwarm", 20))
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right')
plt.show()
plt.tight_layout()