import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/path/to/csv')

'''this will plit multiple regression lines for each hue'''
plt.style.use('seaborn-colorblind') 
sns.lmplot(data=df, x='', y='', hue='', ci=95, height=7)
plt.axvline(x=0.9, color='black', linestyle = 'dashed')
plt.suptitle('', fontweight='bold')
plt.xlabel('')
plt.ylabel('')
#plt.tight_layout()
plt.show()

'''this will plot a single regression line for multiple hues'''
g = sns.lmplot(x='', y='', hue='', data=df, fit_reg=False, legend=False)
sns.regplot(xx='', y='', data=df, scatter=False, ax=g.axes[0, 0])
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
plt.show()