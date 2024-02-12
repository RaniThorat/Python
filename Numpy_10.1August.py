#10/08/2023-Thursday

#What is Numpy
#The Numpy is popular open-Source python library used for scientific computing application,and it stand for Numerical Pyhton ,Which is consisting of Multidimensional array object and a collection of routins for processing 

#Instal python Numpy library 
#1-Go to base terminal and on ptompt
#2-pip install numpy 
#3-Install Numpy using conda
#4-conda Install numpy 


import numpy as np
arr=np.array ([10,20,30])
print(arr)
#output-[10 20 30]

##############################################################################
#create a multi-dimentional Array
arr=np.array([[10,20,30],[40,50,60]])
print(arr)

##############################################################################

#Reperesent the Minimum Dimension 
#used ndmin param to specify how many 
arr=np.array([10,20,30,40],ndmin=3)
print(arr)

##############################################################################
#To change the Data Type
#dtype parameter 
arr=np.array([10,20,30,40],dtype=complex)
print(arr)

###########################################################################
#Get the Dimention of array 
arr=np.array([[1,2,3,4],[7,8,6,7],[9,10,11,12]])
print(arr.ndim)
print(arr)

###############################################################################
#find out the size of each item in the arry
arr=np.array([10,20,30])
print("each item contain in bytes:",arr.itemsize)

#############################################################################
#Get the Data type of each array item 
#finding the Data type of each array item
arr=np.array([10,20,30])
print("each item contain in bytes:",arr.dtype)
 
#############################################################################
#Get the shape and size of Array 
arr=np.array([[10,20,30,40],[60,70,80,90]])
print("Array sixe:",arr.size)
print("shape:",arr.shape)

##############################################################################

#create a squence of integers using arange()
#from 0 to 20 with step of 3
arr=np.array(0,20,3)
print("A squence of array with step of 3:\n",arr)
#output-A squence of array with step of 3:
# [[10 20 30 40]
# [60 70 80 90]]

############################################################################
#Accessing single element using index   
arr=np.arange(11)
print(arr)

print(arr[2])

print(arr[-2])

############################################################################

#Multidimentional Array Indexing 
#using array indexing 
arr=np.array([[10,20,30,40,50],[20,30,50,10,30]])
print(arr)

print(arr.shape)
#output-(2, 5) now,x is 2-dimentional 

print(arr.size)

print(arr[1,1])
#output-30

print(arr[0,4])
#output-50

print(arr[1,-1])
##output-30 we need 1st row and last column 

######################################################################

#Access array alements using slicing 
arr=np.array([0,1,2,3,4,5,6,7,8,9])
x=arr[1:8:2] #stat:end:in  step of 2
print(x)

x=arr[-2:3:-1]
print(x) #start last but one (-2) upto 3 but in step of -1

x=arr[-2:10]
print(x)#start last but one (-2) upto 10 but not 10









