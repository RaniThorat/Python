# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:58:23 2023

@author: Sanchita Gunjal
"""
#31/07/2023-Monday
#Generator
gen=(x for x in range(3))#when u are going to used tuple compherension one object will be created and u can access value of that object using 'for loop'
print(gen)
for num in gen:
    print(num)

#Next method for generator(it show output step by step)
gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)

#Function which return multiple value
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

#now instead of using foe loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
next(gen)

#chaging of generator
def lengths(itr):  #to measure length
    for ele in itr:
        yield len(ele)
def hide(itr):          #to hide 
    for ele in itr:
        yield ele*'*'

password=["not-good","give'm-pass","00100=100"]
for password in hide(lengths(password)): #chaging the generator from hide to lengths
    print(password)

#Enumerate
#printing list with index
lst=["milk","Egg","Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
 
#same code can be implemented using enumerated
lst=["milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
  
###########################################






































