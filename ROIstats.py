#!/usr/bin/env python3
"""
Created on Mon Aug 26 10:31:23 2019
@author: jessedesimone

Module for Plotting ROI stats (3dROIstats - afni)
"""
#%%
import os
import pandas as pd
import numpy as np
import matplotlib
import pylab
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
from scipy.stats import shapiro
from scipy.stats import wilcoxon
import statsmodels.stats.multitest as multi

#load dataset
pd.set_option('display.max_columns', 100) #show max of 100 columns
df=pd.read_csv('/Users/jessedesimone/Documents/Input_post.csv')
df = df.astype({"grp":'category'})  #set grouping variable at categorical factor
df["grp"]= df["grp"].replace(0, "YTC")
df["grp"]= df["grp"].replace(1, "YT")
df.info()

#rename columns
df=df.rename(columns={'A': 'ACC+L_SFG','B': 'PCC', 'C': 'L_IPL', 'D': 'L_MTG', 'E': 'R_IPL', 'F': 'R_MTG', 'G': 'R_SFG', 'H': 'R_PHF', 'I': 'L_PHF', 'J': 'R_MFG', 'K': 'L_IFG', 'L': 'L_PHF2', 'M': 'DMN'})
df.info()

#df.columns=['']     #set column names if needed
#drop unwanted columns
col_names=df.columns
col_names=col_names.drop(['age','scantime','bmi'])
df=df[col_names]
df.info()

#basic df boxplot; single plot for each variable separated by group
#df.boxplot(by="grp", figsize=(12, 6))

#convert data from wide to long for plotting
df2=pd.melt(df,id_vars=['grp'],var_name='region', value_name='values')
df2 = df2.astype({"region":'category'})  #set grouping variable at categorical factor
df2.info()
df2.head(40)

#grouped bar plot using seaborn

current_palette = sns.color_palette("Paired")   #set the desired palette
#sns.palplot(current_palette)    #view selected palette
sns.set_context('notebook', font_scale=2)
sns.set(style="whitegrid")
g = sns.catplot(x="region", y="values", hue="grp", data=df2,
                height=6, kind="bar", palette=current_palette)
g.despine(left=False)
g.set_xticklabels(rotation=45)
g.set_ylabels("Mean Z-score")
g.set_xlabels('')
plt.title('Postseason DMN Z-scores by Region', weight='bold')
plt.savefig("/Users/jessedesimone/Documents/DMNpost.png")




######






