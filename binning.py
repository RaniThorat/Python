# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:30:19 2023

@author: Admin
"""

import pandas as pd
df=pd.read_csv("C:/Datasets/ethnic diversity.csv")
#head will shows the first five records of the data will be displayed
df.head()
#Info will gives size,null values,rows,col and col data types will be shown
df.info()
#dascribe will give the five number summary
df.describe()
#Coverting data or cut data in terms of bin called binning 
df['Salaries_new']=pd.cut(df['Salaries'],bins=[min(df.Salaries),df.Salaries.mean(),max(df.Salaries)],labels=['High','Low'])
#Counting the number of values or category of that mention field
df.Salaries_new.value_counts()
#For finding the more number of category or partition into the more number of grp
df['Salaries_new']=pd.cut(df['Salaries'],bins=[min(df.Salaries),df.Salaries.quantile(0.25),df.Salaries.mean(),df.Salaries.quantile(0.75),max(df.Salaries)],labels=['Group1','Group2','Group3','Group4'])
df.Salaries_new.value_counts()



############################################################
#Dummy variable