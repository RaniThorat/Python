# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:42:09 2023

@author: Sanchita Gunjal
"""

#write python code to add a key to a dictionary 
#sampled dictionary:{0:10,1:20}
#Excepted result:{0:10,1:20,2:30}

d={0:10,1:20}
print(d)
d.update({2:30})
print(d)

d={0:10,1:20}
print(d)
d[2]=30
print(d)

#write python code to concantenate the following dictionaries
#to creat a new one
#sample dictionary :
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4={}
for d in (dict1,dict2,dict3):dict4.update(d)
print(dict4)

#write python code to check whether a given key already
#exists in a dictionary 

d={1:10,2:20,3:30,4:40,5:50,6:60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary ')
is_key_present(5)
is_key_present(9)

#write python code to iterate over dictionaries using for loops.

d={'x':10,'y':20,'z':30}
for dict_key,dict_value in d.items():
    print(dict_key,':',dict_value)

















