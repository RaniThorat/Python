# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:22:27 2023

@author: Admin


"""

#Zero varienace and near zero variance
#If there is no variance in the feature,then ML MODEL
#will not get any intelligence so it is better to have features
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/Datasets/ethnic diversity.csv")
df.var()
#here empId and zip is nominal data
#Salaray has 4.441953e+08 is 4441953000 which is not cose to 0
#Similarly age 8.571358e+01=85.71
#Both features have considerable variance
df.var()==0
'''
EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool'''

#None of them are zero
df.var(axis=0)==0
'''
EmpID       False
Zip         False
Salaries    False
age         False
dtype: bool
'''
df.var(axis=1)==0




##########################################################
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/Datasets/modified ethnic.csv.xls")
#Check for null values
df.isna().sum()





##############################################################
#sklearn file
#Create an imputer that creates nan values
#Means and median is used for numeric data
#Mode is used for discreate data(postion,sex,Martialdes)
import numpy as np
from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
#check the dataframe
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
#Replacing null values with the mean values
df['Salaries'].isna().sum()
#0
