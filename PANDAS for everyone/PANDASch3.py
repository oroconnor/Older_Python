#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:51:14 2020

@author: owenoconnor
"""


import seaborn as sns
anscombe = sns.load_dataset("anscombe")

print(anscombe)

#%%

import matplotlib.pyplot as plt

data1 = anscombe[anscombe["dataset"]=="I"]

plt.plot(data1["x"],data1["y"])

#%%

plt.plot(data1["x"],data1["y"],'o')

data2 = anscombe[anscombe["dataset"]=="II"]
data3 = anscombe[anscombe["dataset"]=="III"]
data4 = anscombe[anscombe["dataset"]=="IV"]

#%%
fig = plt.figure()

axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)

axes1.plot(data1["x"], data1["y"], "o")
axes2.plot(data2["x"], data2["y"], "o")
axes3.plot(data3["x"], data3["y"], "o")
axes4.plot(data4["x"], data4["y"], "o")

axes1.set_title("dataset 1")
axes2.set_title("dataset 2")
axes3.set_title("dataset 3")
axes4.set_title("dataset 4")

fig.suptitle("Anscombe Data")
fig.tight_layout()

#%%

tips = sns.load_dataset("tips")
print(tips.head())

fig = plt.figure()
axes1 = fig.add_subplot(1,1,1)
axes1.hist(tips["total_bill"], bins=10)
axes1.set_title("Histogram of Total Bill")

axes1.set_xlabel("Frequency")
axes1.set_ylabel("Total Bill")
fig.show()

#%%

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)
axes1.scatter(tips["total_bill"],tips["tip"])
axes1.set_title("Scatterplot of Total Bill vs Tips")
axes1.set_xlabel("Total Bill")
axes1.set_ylabel("Tip")

#%%
boxplot = plt.figure()
axes1 = boxplot.add_subplot(1,1,1)
axes1.boxplot([tips[tips["sex"] == "Female"]["tip"],
               tips[tips["sex"] == "Male"]["tip"]],
              labels = ["Female","Male"])
axes1.set_xlabel("Sex")
axes1.set_ylabel("Tips")
axes1.set_title("Boxplot of Tips by Sex")
boxplot.show()
#%%
print(tips.head())
#%%
def recode_sex(sex):
    if sex == "Female":
        return 0
    else:
        return 1
    
tips["sex_color"] = tips["sex"].apply(recode_sex)
scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1,1,1)
axes1.scatter(
    x=tips["total_bill"],
    y=tips["tip"],
    s=tips["size"]*10,
    c=tips["sex_color"],
    alpha=.5)

#%%
hist, ax = plt.subplots()
ax = sns.distplot(tips["total_bill"])
ax.set_title("Total Bill Histogram with Density Plot")
plt.show()
#%%

hist,ax = plt.subplots()
ax= sns.distplot(tips["total_bill"], kde = False)
ax.set_title("Total Bill Histogram")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Frequency")
plt.show()
#%%
den, ax = plt.subplots()
ax= sns.distplot(tips["total_bill"], hist = False)
ax.set_title("Total Bill Histogram")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Frequency")
plt.show()

#%%
hist, ax = plt.subplots()
ax = sns.distplot(tips["total_bill"],rug = True, color = "red", )
ax.set_title("Total Bill Histogram with Density Plot and Rug Plot")
plt.show()

#%%

count, ax = plt.subplots()
ax = sns.countplot("day", data = tips)
ax.set_title("Count of Days")
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Frequency")

#%%
scatter, ax = plt.subplots()
ax = sns.regplot(x='total_bill', y = "tip", data = tips)
ax.set_title("Scatterplot of Total Bill and Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

#%%
hexbin = sns.jointplot(x = "total_bill", y = "tip", data = tips, kind = "hex")
hexbin.set_axis_labels(xlabel="Total Bill",ylabel = "Tip")
hexbin.fig.suptitle("Hexbin Joint Plot of Total Bill and Tip", fontsize = 20,y=1.03,)

#%%
kde, ax = plt.subplots()
ax = sns.kdeplot(data=tips["total_bill"],data2=tips["tip"],shade=True)
ax.set_title("Kernel Density Plot of Total Bill and Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

kde_joint = sns.jointplot(x ="total_bill",y="tip", data = tips,kind = "kde")

#%%

bar, ax = plt.subplots()
ax=sns.barplot(x="time",y="total_bill",data = tips)
ax.set_title("Bar plot of average total bill for time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Average total bill")

#%%
violin, ax = plt.subplots()
ax=sns.violinplot(x="time",y="total_bill",data = tips)
ax.set_title("Violin plot of average total bill for time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Average total bill")

#%%

fig = sns.pairplot(tips)

#%%
violin, ax = plt.subplots()
ax=sns.violinplot(x="time",y="total_bill",hue="sex", data = tips, split = True)
ax.set_title("Violin plot of average total bill for time of day")
ax.set_xlabel("Time of day")
ax.set_ylabel("Average total bill")

#%%

scatter = sns.lmplot(x="total_bill",y='tip',data=tips,hue="sex", ci =None)

