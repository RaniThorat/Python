# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:15:19 2023

@author: Sanchita Gunjal
"""

#1/August/2023-Tuesday
#Use of Zip function 
#interagate tha list
#zip used in NLP web Application
#IMP. for intview (10 outoff 5 time)
name=['dada','mama','kaka']
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)


#Use of zip function with mis match list
name=['dada','mama','kaka','baba']  #It will not display mismatch item in name(i.e.baba)
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

#Zip_longest (It will give the value that are not in list(i.e.baba, & Those baba give the None value name ))
from itertools import zip_longest  
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)


#Use of fill value insted None
from itertools import zip_longest  
name=['dada','mama','kaka','baba']
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

#Use of all(), if all the value are true then it will produce output
# If we are having zero value the output will be useless
lst=[2,3,6,8,9] #the value must ne non zero,+ve,-ve
if all(lst):
    print('all value are true')
else:
    print('Useless')

#Here the output will must be 'Useless' Because the the list having the zero value
lst=[2,3,-6,8,9,0] 
if all(lst):
    print('all value are true')
else:
    print('Useless')

#Use of any if any is positive
lst=[0,0,0,8,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')
    
#Use of any if any is Negative
lst=[0,0,0,0,0,-8]
if any(lst):
    print('It has some value')
else:
    print('Useless')

#use of any
lst=[0,0,0,0,0,0]
if any(lst):
    print('It has some value')
else:
    print('Useless')

#Count()
#Used in IOT apllication
#It is going to create object 
#like generator function
#used in AI
#used count for curnces notes
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

#now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#cycle()
#suppose u have repeated tasks to be done,then u can use this method

import itertools
instructions=("Eat","code","sleep",1)
for instructions in itertools.cycle(instructions):
    print(instructions)

#repeat()
#it is itertool
from itertools import repeat
for mesg in repeat("keep patience",times=10):
    print(mesg)
    
    
#Combination
#combination()-> it is a way of selecting item from a collection,such that (unlike premutation) that order of selection does not matter
#(it is selection technq.)

from itertools import combinations
players =['john','jani','hanardhan']
for i in combinations(players, 2):
    print(i)

#premutation-> it is related to the act of arranging all the memebers of set into same sequence or order

from itertools import permutations
players=['john','GG','rr']
for seat in permutations(players,2):
    print(seat)

#Product()
from itertools import product
team_a=['Rohit','pandya','bumrah']
team_b=['virat','manisha','sami']
for pair in product(team_a,team_b):
    print(pair)

#filter 
age=[27,17,21,19]
adults=filter (lambda age:age>=18,age)
print([age for age in adults]) #list comprehension

#10 outoff 10 time
#shollow copy and deeps copy
#assignment operation
#This will only create a new variable with the same referance. modify
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)

#shallow copy(IMP)
#one level deep,it going to create one level instance 
#create separate  instances 
#shollow is are going to create data object one level deep copy.
#modifing on level one does not affect the other list 
#in order to create shollow copy functionof copy module is used

import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#not affected the other list
list_b[0]=-10
print(list_a)
print(list_b) 


#But with nested object ,modifying  on level  2 or deeper does affect
#in shollow copy with nested object modify level on 2 or deepr does affect the other 
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#affect the other!
list_a[0][0]=-10
print(list_a)
print(list_b) 

#Deep copy 
#Full independent clones are created to create deep copy u need to  use copy.deepcopy() function of copy module.
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
#no affect the other 
list_a[0][0]=-10
print(list_a)
print(list_b)

#write prog. to create an iterator from several iterables in a sequences and display the type and element of the new iterator

#chain operator -used in AI & NLP

from  itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#list
result=chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print("Type of the new iterator:")
print(type(result))
print("Element of the new iterator:")
for i in result:
    print(i)

#Tuple
from  itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)

result=chain_func((10,20,30),('A','B','C','D'),(40,50,60,70,80,90))
print("Type of the new iterator:")
print(type(result))
print("Element of the new iterator:")
for i in result:
     print(i)   
    
#write prog. that generates the running  product of element in an iterable.
#mul is function it is an multipliction of function

from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)
#list
result=running_product([1,2,3,4,5,6])
print("Running product of list is:")
for i in result:
    print(i)

#itertool.accumalate does this ierator take 2 argument iterble targest & function which will be follow and each iteration of value in target
#If no function is passed then by default addition take place   

from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)

#Tuple
result=running_product((1,2,3,4,5,6))
print("Running product of tuple is:")
for i in result:
    print(i)

#Write  prog. to construct an infinite iterator that returns evenly spaced values sgtarting with a specified number and step.
import itertools as it 
start=10
step=1
print("The starting point is ",start,"and step is",step)
my_counter=it.count(start,step)
#following loop will sun for ever
print("The said function print never-ending item:")
for i in my_counter:
    print(i)

#write prog. to generate an infinite cycle of element from an iterable
import itertools as it
def cycle_data(iter): #iter means it having list, tuple,set
    return it.cycle(iter)
#following loop will run for ever
#List
result=cycle_data(['A','B','C','D'])
print("The said function print nevr-ending item:")
for i in result:
    print(i)


#String
import itertools as it
def cycle_data(iter): #iter means it having list, tuple,set
    return it.cycle(iter) 
result=cycle_data("python itertools")
print("The said function print never-ending item:")
for i in result:
    print(i)

#write prog. to make an iterator that drops elements from the iterable as soon element is positive number 

import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x: x<0,nums)
nums=[-1,-2,-3,4,-10,2,0,5,12]
print("Original list:",nums)
result=drop_while(nums)
print("Drop elements from the iterable when a positive \n",list(result))
for i in result:
    print(i)




