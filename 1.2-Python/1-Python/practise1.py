# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:43:02 2023

@author: Admin
"""
#1. Write a Pandas program to convert all the string values 
#to upper, lower cases in a given pandas series. Also find the 
#length of the string values.
import pandas as pd
import numpy as np
s = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print(s)
print("Upper case string")
print(s.str.upper())
print("Lower case string")
print(s.str.lower())
print("Length of string")
print(s.str.len())


#
import pandas as pd
import numpy as np

