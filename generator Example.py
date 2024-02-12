# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:52:01 2023

@author: Sanchita Gunjal
"""

#write prog. that create genertaor function that yields cube of number from 1 to n.Accept n from user
def cube_generator(n):
    for i in range(1,n+1):
        yield i**3
n=int(input("Input a number:"))
cubes=cube_generator(n)
print("Cubes of numbers from 1 to ",n,":")
for num in cubes:
    print(num)


#write a python prog to implemented a generator that generates random number within a given range.
import random
def random_number_generator(start,end):
    while True:
        yield random.randint(start, end)

#Accept input from the user
start=int(input("Input the start value"))
end=int(input("Input the end value"))

#create the generator object
random_number =random_number_generator(start, end)

#generator and print 10 random number
print("Random number between",start,"and",end)
for _ in range(10):
    print(next(random_number))

#python prog. to generate a 3*4*6 3D arry whose each element(3-Rows ,4-col,6-col)
array=[[['*'for col in range(6) ]for col in range(4)] for row in range(3)]
print(array)

#Write python prog. to print the number of a specified list after removing even number from it.

num=[7,8,120,44,20,27,89,99,56]
num=[x for x in num if x%2!=0]
print(num)


































