#!/usr/bin/env python3

'''
Module for plotting grouped boxplot as subplots
Example for 2x2 subplots
'''

#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statannotations.Annotator import Annotator

#read data
df=pd.read_csv('/path/to/data.csv')

sns.set_context("talk")
x='grp'
order = ['plasma-/PET-', 'plasma+/PET-', 'plasma+/PET+']
pairs=[('plasma-/PET-', 'plasma+/PET-'), ('plasma-/PET-', 'plasma+/PET+'),('plasma+/PET-', 'plasma+/PET+')]
my_cols = {'plasma-/PET-': 'cyan', 'plasma+/PET-': 'steelblue', 'plasma+/PET+': 'lightslategrey'}
#f, (ax1, ax2) = plt.subplots(2, 2, figsize=(15,15))
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15,15))
'''plot ax1'''
sns.boxplot(data=df, x=x, y='composite_gm_fw', order=order, notch=False,  
                 palette=my_cols, fliersize = 5,
                 flierprops={"marker": "o", 'markerfacecolor':'white', 'markeredgecolor':'black'},
                 showfliers=False, 
                 medianprops={"color": "black"}, 
                 boxprops = {'edgecolor': 'black', 'linewidth': 1},
                 whiskerprops = {"color": "black"},
                 capprops = {"color": "black"},
                 ax=ax1)
sns.stripplot(data=df, x=x, y='composite_gm_fw', order=order, palette=my_cols, 
                  size=4, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax1)
'''plot ax2'''
sns.boxplot(data=df, x=x, y='composite_wm_fw', order=order, notch=False,  
                 palette=my_cols, fliersize = 5,
                 flierprops={"marker": "o", 'markerfacecolor':'white', 'markeredgecolor':'black'},
                 showfliers=False, 
                 medianprops={"color": "black"}, 
                 boxprops = {'edgecolor': 'black', 'linewidth': 1},
                 whiskerprops = {"color": "black"},
                 capprops = {"color": "black"},
                 ax=ax2)
sns.stripplot(data=df, x=x, y='composite_wm_fw', order=order, palette=my_cols, 
                  size=4, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax2)
'''plot ax3 params'''
sns.boxplot(data=df, x=x, y='composite_gm_fat', order=order, notch=False,  
                 palette=my_cols, fliersize = 5,
                 flierprops={"marker": "o", 'markerfacecolor':'white', 'markeredgecolor':'black'},
                 showfliers=False, 
                 medianprops={"color": "black"}, 
                 boxprops = {'edgecolor': 'black', 'linewidth': 1},
                 whiskerprops = {"color": "black"},
                 capprops = {"color": "black"},
                 ax=ax3)
sns.stripplot(data=df, x=x, y='composite_gm_fat', order=order, palette=my_cols, 
                  size=4, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax3)
'''plot ax4 params'''
sns.boxplot(data=df, x=x, y='composite_wm_fat', order=order, notch=False,  
                 palette=my_cols, fliersize = 5,
                 flierprops={"marker": "o", 'markerfacecolor':'white', 'markeredgecolor':'black'},
                 showfliers=False, 
                 medianprops={"color": "black"}, 
                 boxprops = {'edgecolor': 'black', 'linewidth': 1},
                 whiskerprops = {"color": "black"},
                 capprops = {"color": "black"},
                 ax=ax4)
sns.stripplot(data=df, x=x, y='composite_wm_fat', order=order, palette=my_cols, 
                  size=4, jitter=True, edgecolor="black", linewidth=1,
                  ax=ax4)


'''set ax1 params'''
ax1.set(xlabel=None)
ax1.set_title(label='', fontsize=20, fontweight='bold')
ax1.set_ylabel('', fontsize=16, fontweight='bold')
ax1.tick_params(axis="x", labelsize=16)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
annot1 = Annotator(ax1, pairs, data=df, x=x, y='composite_gm_fw', order=order)
annot1.configure(test=None, loc='inside')
annot1.set_pvalues([0.0325, 0.0001, 0.21])
annot1.annotate()
'''set ax2 params'''
ax2.set(xlabel=None)
ax2.set_title(label='', fontsize=20, fontweight='bold')
ax2.set_ylabel('')
ax2.tick_params(axis="x", labelsize=16)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
annot2 = Annotator(ax2, pairs, data=df, x=x, y='composite_gm_fw', order=order)
annot2.configure(test=None, loc='inside')
annot2.set_pvalues([0.11, 0.0002, 0.15])
annot2.annotate()
'''set ax3 params'''
ax3.set(xlabel=None)
ax3.set_ylabel('', fontsize=16, fontweight='bold')
ax3.tick_params(axis="x", labelsize=16)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
annot3 = Annotator(ax3, pairs, data=df, x=x, y='composite_gm_fat', order=order)
annot3.configure(test=None, loc='inside')
annot3.set_pvalues([0.0056, 0.84, 0.011])
annot3.annotate()
'''set ax4 params'''
ax4.set(xlabel=None)
ax4.set_title(label='', fontsize=20, fontweight='bold')
ax4.set_ylabel('')
ax4.set_ylim([0.475,0.6])
ax4.tick_params(axis="x", labelsize=16)
ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
annot4 = Annotator(ax4, pairs, data=df, x=x, y='composite_gm_fw', order=order)
annot4.configure(test=None, loc='inside')
annot4.set_pvalues([0.0027, 0.99, 0.0254])
annot4.annotate()

plt.tight_layout()
plt.savefig('test.jpg', dpi=600)
plt.show()