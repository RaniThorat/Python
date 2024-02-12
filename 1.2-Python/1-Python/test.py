# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:56:38 2023

@author: Admin
"""

'''Write a Pandas program to replace the 'qualify' column contains 
the values 'yes' and 'no' with True and False. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 
                      'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']'''


import pandas as pd
import numpy as np
exam_data = {'name': ['Ram', 'Sham', 'Krishna', 'Ramkrishna', 'Shubhendu', 
                      'Mahesh', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data,index=labels)
print("original rows: ")
print(df)
print("\n To replace the 'qualify ' column conatains the values 'yes' and 'no' with True and false : ")
df['qualify']=df['qualify'].map({'yes':True, 'no': False})
print(df)




'''Q2Write a Python program to plot two or more lines  
with different styles. '''
import matplotlib.pyplot as plt
x=range(1,10)
plt.plot(x,[xi*1.8 for xi in x])
plt.plot(x,[xi*4.0 for xi in x])
plt.plot(x,[xi/7.0 for xi in x])
plt.show()

'''Q.3 Create an array[1,2,3] write L1 and L2 norm value for it'''
 





'''Q.4 Write a NumPy program create [[1, 0], [1, 2]] square array 
and  compute the determinant of a given square array.'''
import pandas as pd
import numpy as np
arr=np.array([[1,0],[1,2]])
print(arr)
print(arr.ndim)



'''Q.5 Write a Python function to find the kth smallest element in a list.'''

def smallest(lst,k):
    return sorted(lst)[k-1]
m_list=[5,7,8,3,5,7,8,5,3,2]
kth=2
res=smallest(m_list,kth)
print(res)
