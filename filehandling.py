# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 09:21:53 2023

@author: Sanchita Gunjal
"""

#28/07/2023

#relative path work when working directory is same
#it reads the pi_digits file
with open ('pi_digits.txt') as file_object:
    #the open () function need
    #one argument: the name of the file u want open
    contents = file_object.read()
print(contents)

#observe the extra space line at the end of output

##################################################
#To avoid this rstrip() method is used 
with open ('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
#rstrip() mathod removes ,or strips, any whitespace
#characters from the right side of  a string
################################################

#absolute path is work  even working directory is different
file_path = 'c:/1-python/pi_digits.txt'
with open(file_path) as file_object:
    contents=file_object.read()
print(contents.rstrip())

#Reading line by line
filename='pi_digits.txt'
#we assign the name of the file we're reading from to the variable
with open  (filename) as file_object:
#we again use the with syntax to 
#let python open and close
#the file properly
    for line in file_object:
        print(line)

######################################
filename='pi_digits.txt'
with open  (filename) as file_object:
    for line in file_object:
        print(line.rstrip())


#######################
#working with file's content
#after u read file into memory 
filename='pi_digits.txt'
with open (filename) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))

#Writing to a file
#simplest ways to save data is to write it
#to a file when u write text to file
filename='programming.txt'
with open (filename,'w') as file_object:
    file_object.write("I love programming.")
   
#writing multiple line
filename='programming.txt'
with open (filename,'w') as file_object:
    file_object.write("I love programming.")
    file_object.write('I love creating new games.')
   
# for new line
filename='programming.txt'
with open (filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write('I love creating new games.\n')
   
#Appending file
#If u want to content to file
#when u open a file in append mode, python does not erase the content of file before returning the file object
filename='programming.txt'
with open (filename,'a') as file_object:
#used the 'a' argument to open the file for appending 
#rather than writing over the existing file
    file_object.write("I love finding meaning in large datasets.\n")
    file_object.write('I love creating apps that can run in a browser.\n')        
        























