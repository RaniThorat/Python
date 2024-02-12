#10/08/2023-Thursday

#Indexing In Numpy 
import numpy as np
multi_arr = np.array ([[10,20,10,40],
                 [40,50,70,90],
                 [60,10,70,80],
                 [30,90,40,30]])
multi_arr

#slicing 
#for multidimentional Numpy array ,u can access the element as below 

multi_arr [1,2] #to access the value at rows 1 & column 2
multi_arr[1,:] #to get the value at rows 2 and all colunm 
multi_arr[:,1] #to access the value at all rows and column 1

 
x=multi_arr[:3,::2] 
print(x)


#Integer array indexing 
arr =np.arange(35).reshape(5,7)
print(arr)

####################################################################

#Boolean Array Indexing 
#This advanced indexing occurs when an object is an array of boolen types,
#such as may be returned from comparsion operators
#use dthis method when we want to pick the element
#from the array which satisfy the some condition 

#Boolean Array Indexing 
arr=np.arange(12).reshape(3,4)
print(arr)

rows=np.array([False,True,True])
wanted_rows=arr[rows,:]
print(wanted_rows)

#convert Numpy to python List
#using tolist() method ,we may have a list of Data element that have been converted from the array using this method

#converting one dimentional array to list 

#create array 
array = np.array([10,20,30,40])
print("Array:",array)
print(type(array))


#convert List 
lst=array.tolist()
print("list:",lst)
print(type(lst))

###################################################################

#converting mul-dimentional Array to list
#create Array 
array =([[10,20,30,40],[50,60,70,80],[60,40,20,10]])
print("Array:",array)

#convert list 
lst = array.tolist()
print("list:",lst)
##################################################################
#convert list to Array 

list = [20,40,50,80]

#convert into Array 

array = np.array(list)
print("Array:",array)

#used asarray()
list=[20,40,50,80]
array=np.asarray(list)
print("Array:",array)
print(type(array))


#shape 
array=np.array([[1,2,3],[4,5,6]])
print(array.shape)

#Resize the Araay 
array = np.array([[10,20,30,],[40,50,60]])
array.shape=(3,2)
print(array)

#oprtaion using Numpy 
#Numpy operation are divide into 3 main type
#1-fourier transform and shape manipulation 
#2-mathematical and logical operation 
#3-Linear Algebra and Random Number Generation 


















































































































































































