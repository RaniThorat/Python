#10/08/2023-Thursday

#Write a Numpy prog. to get the Numpy version and show the Numpy  
import numpy as np
print(np.__version__)
#output-1.23.5

#write a Numpy prog. to test whether none of the element of a given array are zero .
import numpy as np 
x=np.array([1,2,3,4])
print("original array:")
print(x)
print("test if none of the element of a said array is zero:")
print(np.all(x))

#OR
import numpy as np
x=np.array([0,1,2,3])
print("original array:")
print(x)
print("test if none of the element of a said  array are zero:")
print(np.all(x))

#write numpy prog. to Test if any of the element of  a given array ara non-zero
import numpy as np 
x=np.array([1,0,0,0])
print("original array:")
print("test whether any of the element if a given array is non-zero:")
print(np.any(x))

#OR

import numpy as np 
x=np.array([0,0,0,0])
print("original array:")
print("test whether any of the element if a given array is non-zero:")
print(np.any(x))

#write numpy prog. to Test a given array element-wise for finitenese (no infinity or not no.)
import numpy as np
x=np.array([1,0,np.nan,np.inf]) #inf stand for infinite
print("original array:")
print(x)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(x))

#write numpy prog. to Test element-wise for NaN of a given array 
import numpy as np
a=np.array([1,0,np.nan,np.inf]) #inf stand for infinite
print("original array:")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isnan(a))

#write numpy prog. to create element-wise comparison (greater,greater_eqaul,less and less_equal ) of two given array
import numpy as np
x=np.array([3,5])
y=np.array([2,5])
print("original array:")
print(x)
print(y)
print("comparison-greater:")
print(np.greater(x,y))
print("comparison-greater_equal :")
print(np.greater_equal(x,y))
print("comparison-less:")
print(np.less(x,y))
print("comparison-less_equal:")
print(np.less_equal(x,y))

#write numpy prog. to create a 3x3 identity matrix (it having diagonal element 1)
import numpy as np
array_2D=np.identity(3)
print("3x3 matrix")
print(array_2D)

#write numpy prog. to generate a random no. between 0 and 1
import numpy as np 
rand_num=np.random.normal(0,1,1)
print("Random no.between 0 & 1")
print(rand_num)

#OR

import numpy as np 
rand_num=np.random.normal(0,1,2) #here we take the 2 in last it means that the output will be in 2 random no.
print("Random no.between 0 & 1")
print(rand_num)

#OR

import numpy as np 
rand_num=np.random.normal(0,1,9)
print("Random no.between 0 & 1")
print(rand_num)

#write numpy prog.to create  3x4 array and iterate over it 
import numpy as np 
a=np.arange(10,22 ).reshape((3,4))
print("original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
    print(x,end="")
    print()

#write numpy prog. to create a vector of length 10 with value of evenly distributed between 10 and 50
import numpy as np 
v= np.linspace(10,49,5)
print(" length 10 with evenly distributed between 10 & 50")
print(v)

#write numpy prog. to create a 3x3 matrix with values ranging from 2 to 10 
import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x) 

#write numpy prog. reverse an array (the first element become the last ) 
import numpy as np 
x=np.arange(12,38)
print("origial array")
print(x)
print("Reverse array")
x=x[::-1]
print(x)

#write numpy prog. to compute the multiplication of given two matrix
import numpy as np 
p = [[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix:")
print(p)
print(q)
result1=np.dot(p,q)
print("Result of the matrix multiplication :")
print(result1) 

#write numpy pro. to compute the cross product of given two matrix
import numpy as np 
p = [[1,0],[0,1]]
q=[[1,2],[3,4]]
print("original matrix:")
print(p)
print(q) 
result1=np.cross(p,q)
result2=np.cross(q,p)
print("cross product of given two matrix:(p,q )")
print(result1)
print("cross product of given two matrix:(q,p )")
print(result2)


#write numpy prog. to compute the determinate of given square array 
#imp.
import numpy as np 
from numpy import linalg as LA 
a = np.array([[1,0],[1,2]])
print("original array:")
print(a)
print("Determinat of the said 2-D array:")
print(np.linalg.det(a))

#write numpy prog. to compute the eigenvalues and of a square array 
import numpy as np 
m =np.mat("3,-2;1 0")
print("orginal matrix:") 
print("a\n",m)
w,v=np.linalg.eig(m)
print("Eigenvalues of the said matrix:",w)
print("Eigenvalues of the said matrix",v)

#write numpy prog. to compute the inverse of give matrix
import numpy as np 
m=np.array ([[1,2],[3,4]])
print("original marix:")
print(m)
result=np.linalg.inv(m)
print("Inverse of the said marix:")
print(result)

#write a numpy prog. to add, subtract ,multiply ,division 
import numpy as np 
print("add")


































































































