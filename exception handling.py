# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 15:11:17 2023

@author: Sanchita Gunjal
"""

#exception are handled with try-except blocks
#handling the zerodivisionerror exception

print(5/0)

#using try-except block
a=5
b=6
c=a=b
print(5/0)    

############################# using exception to prevent crashes
a=5
b=6
c=a=b
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
print(c)

#Handling the filenotfounderror exception 
filename='alice.txt'
with open (filename,encoding='utf-8') as f:
    contents=f.read()

##############################################################
filename='alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print(f"sorry,the file{filename} does not exist.")
        
#jason file handling the file 
#jason stand for java script object nation

import json
number=[2,3,5,7,11,13]
filename='number.jason'
with open(filename,'w') as f:
    json.dump(number,f)

#saving data with json is useful
import json
username = input("what is your name?")
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f"we'll remember you when you come back,{username}!")


#now let write a new prog. that greet
#a user whose name has already been stored

import json
filename='username.json'
with open(filename,'w') as f:
    json.dump(username,f)
print(f"welcome back,{username}!")






















