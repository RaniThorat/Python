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


