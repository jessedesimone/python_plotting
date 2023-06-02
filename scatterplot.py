import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/path/to/csv')

plt.style.use('seaborn-colorblind') 
sns.scatterplot(data=df, x='', y='', hue='', ci=95, height=5, legend=False)
plt.axvline(x=0.16, color='black', linestyle = 'dashed')
plt.suptitle('', fontweight='bold')
plt.xlabel('')
plt.ylabel('')
plt.tight_layout()
plt.show()
