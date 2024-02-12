# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:04:05 2023

@author: Sanchita Gunjal
"""
#31/07/2023-Monday
#List comprehension (10 out of 9 time)
#In basic format
lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#In advanced format
lst=[num for num in range(0,20)]
print(lst)
########################################################
#Capitalize methoc(do capital first letter)
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
###############################################
#list comherension with if statement(imp. for intreview)
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)] #If statement always in right side
print(lst)


def odd_num(num):
    return num%2!=0
lst=[num for num in range(10) if odd_num(num)]
print(lst)

#################################################
lst=[f"{x}{y}" for x in range(3) for y in range(3)] #it means loop inside loop 
print(lst)

lst=[f"{x}{y}" for x in range(4) for y in range(5)]
print(lst)
###################################################
#set comprehension
set={x for x in range(3)}
print(set)

##################################################
#dictionary comprehensio(10 out of 2 time )
dict={x:x*x for x in range(6)}
print(dict)

dict={x:x+x for x in range(20)}
print(dict)



































































