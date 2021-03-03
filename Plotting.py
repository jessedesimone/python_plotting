#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:51:38 2019

@author: jessedesimone
"""

#plotting with seaborn and matplotlib

#%%
#load packages
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%
#change working directory
os.chdir()
#list working directory
os.listdir()
#%%
#plotting parameters
#load plotting style
#see style gallery (https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html)
plt.style.use('seaborn-colorblind') 
sns.set(style="whitegrid") #grid color
#set plot context to paper, notebook, talk, poster
sns.set_context("paper", font_scale=1)
#adjust figure size
plt.figure(figsize=(20,5))
#remove grid lines from plot
sns.set_style("whitegrid", {'axes.grid' : False})

#%%
#load dataset from seaborn package
df = sns.load_dataset('iris')
#df.head(10)
#tips = sns.load_dataset("tips")
#tips.head(10)

#%%
#read data from mac using pandas
df = pd.read_csv('/Users/jessedesimone/Documents/Python/DeSimone_Py_scripts/Datasets/IRIS.csv')
df.head(10)   #header data


#%%
#check if any missing values
df.info()

#%%
#get counts of variables
print(df['species'].value_counts())

#%%
#get data summary for variables and figure
descript=df.describe()
print(descript)

#%%
df.describe().plot(kind = "area",fontsize=10, figsize=(10,5), table = True ,colormap="rainbow")
#plt.xlabel('Statistics',)
plt.ylabel('Value')
plt.title("General Statistics of Iris Dataset")
plt.savefig("descript.png")


#%%
#count plot and pie chart
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
sns.countplot('species',data=df)
#pie chart
plt.subplot(1,2,2)
df['species'].value_counts().plot.pie(explode=[0.03,0.03,0.03],autopct='%1.1f%%',shadow=True)

#%%
#pie chart
#f,ax=plt.subplots(1,2,figsize=(18,8))
df['species'].value_counts().plot.pie(explode=[0.03,0.03,0.03],autopct='%1.1f%%',shadow=True,figsize=(8,6))
#df['species'].value_counts().plot.pie(explode=[0.1,0.1,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
#ax[0].set_title('Iris Species Count')
#ax[0].set_ylabel('Count')
#sns.countplot('Species',data=df,ax=ax[1])
#ax[1].set_title('Iris Species Count')
plt.show()

#%%
#basic histogram 1 variable
plt.figure(figsize=(5,5))
sns.distplot( df["sepal_length"] ,kde=False, color="skyblue", label="Sepal Length", rug=True)

#%%
#all variables
df.hist(edgecolor='black', linewidth=1, color='red')
fig=plt.gcf()
fig.set_size_inches(12,6)
#%%
#basic histogram 2 variables
plt.figure(figsize=(8,5))
sns.set_style("whitegrid", {'axes.grid' : False})
sns.axes_style("whitegrid")
sns.distplot( df["sepal_length"] ,kde=False, color="skyblue", label="Sepal Length")
sns.distplot( df["sepal_width"] ,kde=False, color="red", label="Sepal Width")

#%%
#joint scatter and histogram

sns.jointplot("sepal_length", "sepal_width", data=df, kind="reg", color='black')
sns.jointplot("sepal_length", "sepal_width", data=df, kind="kde")
g = (sns.jointplot("sepal_length", "sepal_width",data=df, color="k").plot_joint(sns.kdeplot, zorder=0, n_levels=6))
#%%
#facet grid

sns.FacetGrid(df,hue='species',size=5)\
.map(plt.scatter,'sepal_length','sepal_width')\
.add_legend()

#%%
#boxplot or whisker plot
#one variable
fig=plt.gcf()
fig.set_size_inches(10,5)
fig=sns.boxplot(x='species',y='petal_length',
                data=df,order=['Iris-virginica','Iris-versicolor','Iris-setosa'],
                linewidth=2.5,orient='v',dodge=False)
#all variables
df.boxplot(by="species", figsize=(12, 6))   #all
#%%
#boxplot plus facet grid histogram
sns.boxplot(x = tips["sex"], y = tips["tip"]).set_title("Male/Female Tips")
g = sns.FacetGrid(tips, row = "sex")   #first parameter = function
#g.map allows for groups to be plotted on separate axes
g = g.map(plt.hist, "tip")  #second parameter = plotting variable
plt.show()

#%%
#scatterplot with matplot

df.plot(kind='scatter',x="sepal_length",y="sepal_width",color='red',label='flower', linewidth=3, alpha=0.9, 
grid=True, linestyle='-.', figsize=(10,8))

plt.legend(loc='upper right')    
plt.xlabel('Length (mm)')
plt.ylabel('Width (mm)')
plt.title('Speal length vs width')
plt.show()

#%%
#scatterplot with seaborn
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

#%%
#two-factor scatterplot
plt.figure(figsize=(10,8))
ax = sns.scatterplot(x="total_bill", y="tip", 
                     data=tips)

#%%
#three-factor scatterplot

tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", hue="time", 
                     data=tips)
#%%
#alter size of grouping variable
sns.scatterplot(x="total_bill", y="tip", size="sex", data=tips)
#%%
#alter size and color of grouping variable
sns.scatterplot(x="total_bill", y="tip", hue="sex", size="sex", data=tips)
#%%
#change the min and max  point sizes and colors in legend
cmap = sns.cubehelix_palette(dark=0, light=1, as_cmap=True)
sns.scatterplot(x="total_bill", y="tip", hue="day", size="day", 
                cmap=cmap, sizes=(20,200), data=tips)

#%%
sns.relplot(x="total_bill", y="tip", hue="day", size="day", 
                palette="muted", sizes=(30,300), data=tips)
#%%
sns.relplot(x="total_bill", y="tip", hue="day", col="time", data=tips)

#%%
g = sns.relplot(x="total_bill", y="tip", hue="day",row="sex", col="time", data=tips)
#%%
#four-factor scatterplot
tips = sns.load_dataset("tips")
plt.style.use('seaborn-colorblind') 
ax = sns.scatterplot(x="total_bill", y="tip", hue="day", style="time", 
                     data=tips)
#%%
#use specific set of markers
markers = {"Lunch": "s", "Dinner": "X"}
sns.scatterplot(x="total_bill", y="tip", style="time", markers=markers, data=tips)

#%%
#strip plot
fig=plt.gcf()
fig.set_size_inches(8,7)
fig=sns.stripplot(x='species',y='sepal_length',data=df,jitter=True,
                  edgecolor='gray',size=8,palette='winter',orient='v')

#%%
#combined box and strip plot
fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.boxplot(x='species',y='sepal_length',data=df)
fig=sns.stripplot(x='species',y='sepal_length',data=df,jitter=True, size=8,edgecolor='', color='black')

#%%

ax= sns.boxplot(x="species", y="petal_length", data=df)
ax= sns.stripplot(x="species", y="petal_length", data=df, size=4, jitter=True, edgecolor="gray")

boxtwo = ax.artists[2]
boxtwo.set_facecolor('yellow')
boxtwo.set_edgecolor('black')
boxthree=ax.artists[1]
boxthree.set_facecolor('red')
boxthree.set_edgecolor('black')
boxthree=ax.artists[0]
boxthree.set_facecolor('green')
boxthree.set_edgecolor('black')

plt.show()

#%%
#violin plot
fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.violinplot(x='species',y='sepal_length',data=df)

#%%
plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
sns.violinplot(x='species',y='petal_length',data=df)
plt.subplot(2,2,2)
sns.violinplot(x='species',y='petal_width',data=df)
plt.subplot(2,2,3)
sns.violinplot(x='species',y='sepal_length',data=df)
plt.subplot(2,2,4)
sns.violinplot(x='species',y='sepal_width',data=df)
#%%
#pair plots
sns.pairplot(data=df,kind='scatter')

sns.pairplot(df,hue='species')

#%%
#correlation & heat map
df.corr()   #correlation values to dataframe
fig=plt.gcf()
fig.set_size_inches(10,7)
fig=sns.heatmap(df.corr(),annot=True,cmap='YlGnBu',
                linewidths=1,linecolor='k',square=True,mask=False, 
                vmin=-1, vmax=1,cbar_kws={"orientation": "vertical"},cbar=True)

#%%
#correlation & heat map
df.corr()   #correlation values to dataframe
f, ax= plt.subplots(figsize=(10,10))
sns.heatmap(df.corr(),annot=True, linewidths=1.5,fmt=".1f",ax=ax )
plt.show()
#%%
#swarm plot
sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
fig = sns.swarmplot(x="species", y="petal_length", data=df)

#%%
#box and swarm plot combines
sns.set(style="darkgrid")
fig=plt.gcf()
fig.set_size_inches(8,5)
fig= sns.boxplot(x="species", y="petal_length", data=df)
fig= sns.swarmplot(x="species", y="petal_length", data=df, color=".2")

#%%
#combined swarm and violin plot
sns.set(style="whitegrid")
fig=plt.gcf()
fig.set_size_inches(10,7)
ax = sns.violinplot(x="species", y="petal_length", data=df, inner=None)
ax = sns.swarmplot(x="species", y="petal_length", data=df,color="white", edgecolor="black")

#%%
#LM plot
sns.set(style="whitegrid")
fig=sns.lmplot(x="petal_length", y="petal_width", hue="species",data=df)
plt.xlabel('petal width (cm)')
#%%
#LM plot facet grid
g = sns.lmplot(x="size", y="total_bill", hue="day", col="day", data=tips, height=6, aspect=.4, x_jitter=.1)



#%%
#https://seaborn.pydata.org/generated/seaborn.lineplot.html
#fMRI time series plot
import seaborn as sns
sns.set(style="darkgrid")
#%%
#load data
fmri = sns.load_dataset("fmri")
#%%
#extract data for a single subject
fmri1 = fmri[fmri['subject'].str.contains("s0")]
#print(fmri1)
#create dataframe with only the years between 2010-2015
fmri1=fmri1[["timepoint","event","region","signal"]]
#print(fmri1)

# Plot the responses for different events and regions for one subject
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri1)

#%%
#alternate option for single subject

fmris0=fmri[fmri.subject == 's0']
fmris0
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmris0)
plt.title('s0 fMRI signal')

#%%
# Plot the signal grouped by region and styled by event
sns.lineplot(x="timepoint", y="signal",
             hue="region", style="event",
             data=fmri)
#%%
#Plot the signal grouped by event and styled by region 
sns.lineplot(x="timepoint", y="signal",
             hue="event", style="region",
             data=fmri)

#%%
#plot separate facet grids for each subject
g = sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=4,height=4, aspect=0.7, kind="line", data=fmri)

#%%
#plot individual data for all subs frontal signal
sns.lineplot(x="timepoint", y="signal", hue="event",
             units='subject', estimator=None, lw=1.5,
             data=fmri.query("region == 'frontal'"))
plt.xlabel('Time (ms)')
plt.ylabel('BOLD signal')
#%%
