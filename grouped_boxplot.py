#!/usr/bin/env python3
'''boxplot subplots for specified columns in dataframe'''

#import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read data
df=pd.read_csv('<path/to/infile')


# melt dataframe for plotting
df_melt=pd.melt(df,id_vars=['id_subj','grp'],var_name='roi', value_name='zscore')
df_melt=df_melt.drop(['id_subj'], axis=1)     # drop covariates for better viewing

# grouped boxplot
fig, ax = plt.subplots(1, figsize=(10,5))
sns.boxplot(data=df_melt, x='roi', y='zscore', hue='grp', palette='dark').set(title="Functional Connectivity", xlabel="", ylabel="Mean Z-score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()