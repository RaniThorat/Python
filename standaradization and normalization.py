# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:23:04 2023

@author: Admin
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/Datasets/mtcars_dup.csv.xls")
d.describe()
a=d.describe()

#Initalize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()