
#import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/jessedesimone/Desktop/df_final_fcm6_bxcx.csv')
sns.lmplot(x ='cdr_bxcx', y ='Occipital_Inf_L_4', data = df, 
           hue ='grp', markers =['o', 'v'])
plt.tight_layout()
plt.show()

sns.lmplot(x ='moca_bxcx', y ='Occipital_Inf_L_1', data = df)
plt.tight_layout()
plt.show()