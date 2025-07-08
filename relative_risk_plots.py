# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Seed for reproducibility
# np.random.seed(42)

# # Simulated data: groups, RR, lower and upper CI bounds, sample sizes
# data = pd.DataFrame({
#     'Group': ['A', 'B', 'C', 'D', 'E'],
#     'RR': [1.2, 0.8, 1.5, 0.9, 1.1],
#     'CI_lower': [1.0, 0.6, 1.2, 0.7, 0.9],
#     'CI_upper': [1.4, 1.0, 1.8, 1.1, 1.3],
#     'Sample_size': [100, 150, 80, 120, 90]
# })

# # FOREST PLOT
# plt.figure(figsize=(6, 4))
# plt.errorbar(data['RR'], data['Group'], 
#              xerr=[data['RR'] - data['CI_lower'], data['CI_upper'] - data['RR']],
#              fmt='o', color='blue', capsize=5)
# plt.axvline(x=1, color='red', linestyle='--')
# plt.xlabel('Relative Risk (RR)')
# plt.title('Forest Plot of Relative Risk by Group')
# plt.grid(axis='x')
# plt.show()

# # DOT PLOT
# plt.figure(figsize=(6, 4))
# sns.scatterplot(x='RR', y='Group', data=data, s=100, color='green')
# plt.axvline(x=1, color='red', linestyle='--')
# plt.xlabel('Relative Risk (RR)')
# plt.title('Dot Plot of Relative Risk by Group')
# plt.grid(axis='x')
# plt.show()

# # LOLLIPOP PLOT
# plt.figure(figsize=(6, 4))
# plt.hlines(y=data['Group'], xmin=1, xmax=data['RR'], color='purple')
# plt.scatter(data['RR'], data['Group'], color='purple', s=100)
# plt.axvline(x=1, color='red', linestyle='--')
# plt.xlabel('Relative Risk (RR)')
# plt.title('Lollipop Plot of Relative Risk by Group')
# plt.grid(axis='x')
# plt.show()

# # BUBBLE PLOT
# plt.figure(figsize=(6, 4))
# sizes = data['Sample_size'] * 5  # scale for visibility
# plt.scatter(data['RR'], data['Group'], s=sizes, alpha=0.6, color='orange', edgecolor='k')
# plt.axvline(x=1, color='red', linestyle='--')
# plt.xlabel('Relative Risk (RR)')
# plt.title('Bubble Plot of Relative Risk by Group (size = sample size)')
# plt.grid(axis='x')
# plt.show()



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(24)

# Categories
categories = ['All cases', 'PD only', 'MSA only', 'PSP only']

# Simulated Relative Risks of misdiagnosis (Control vs AI-assisted)
# Here RR > 1 means Control has higher risk than AI-assisted
rr_values = [1.3, 1.5, 1.2, 1.4]
ci_lower = [1.1, 1.2, 1.0, 1.1]
ci_upper = [1.5, 1.8, 1.4, 1.7]
sample_sizes = [150, 80, 50, 40]

data = pd.DataFrame({
    'Category': categories,
    'RR': rr_values,
    'CI_lower': ci_lower,
    'CI_upper': ci_upper,
    'Sample_size': sample_sizes
})

plt.figure(figsize=(7, 4))
plt.errorbar(data['RR'], data['Category'],
             xerr=[data['RR'] - data['CI_lower'], data['CI_upper'] - data['RR']],
             fmt='o', color='darkblue', capsize=5)
plt.axvline(1, color='red', linestyle='--')
plt.xlabel('Relative Risk of Misdiagnosis (Control vs AI-assisted)')
plt.title('Forest Plot of Relative Risk by Diagnostic Category')
plt.grid(axis='x')
plt.show()

plt.figure(figsize=(7, 4))
sns.scatterplot(x='RR', y='Category', data=data, s=120, color='darkgreen')
plt.axvline(1, color='red', linestyle='--')
plt.xlabel('Relative Risk of Misdiagnosis (Control vs AI-assisted)')
plt.title('Dot Plot of Relative Risk by Diagnostic Category')
plt.grid(axis='x')
plt.show()

plt.figure(figsize=(7, 4))
plt.hlines(y=data['Category'], xmin=1, xmax=data['RR'], color='purple', linewidth=2)
plt.scatter(data['RR'], data['Category'], color='purple', s=120)
plt.axvline(1, color='red', linestyle='--')
plt.xlabel('Relative Risk of Misdiagnosis (Control vs AI-assisted)')
plt.title('Lollipop Plot of Relative Risk by Diagnostic Category')
plt.grid(axis='x')
plt.show()

plt.figure(figsize=(7, 4))
sizes = data['Sample_size'] * 10  # scale for visibility
plt.scatter(data['RR'], data['Category'], s=sizes, alpha=0.6, color='orange', edgecolor='black')
plt.axvline(1, color='red', linestyle='--')
plt.xlabel('Relative Risk of Misdiagnosis (Control vs AI-assisted)')
plt.title('Bubble Plot of Relative Risk by Diagnostic Category\n(Size proportional to sample size)')
plt.grid(axis='x')
plt.show()
