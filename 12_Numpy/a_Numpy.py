

'''Numpy:

Numpy stands for numerical python

.it is used to perform computation and processing on multidimensional and single dimensional arrays.
.it is an open source python library used for arrays

Advantages of Numpy:

.it is used for array oriented computing
    high efficiency in a multidimensional array
    used for scientific computation
    number provides the inbuilt functions for linear algebra and random number generation

Numpy environment setup:

!pip install numpy - for IDE or Local setup

import numpy as np - in collaborator as it is already installed

    '''
import numpy as np

'''Numpy Ndarray:

.Ndarray is an object to store similar kinds of elements
.we can create a collection of elements of the same data type
.the array index starts from 0

To create Ndarray first import the numpy module and use the array() function
'''

import numpy as np

a = np.array
print(a)
#output: <built-in function array>

#Creating 1-D array
array_1d = np.array([1,2,3,4,5])
print("1-D array: \n", array_1d)    

array_0 = np.zeros((2,5), dtype = int)
print("zero's array: \n", array_0)

array_1 = np.ones(shape = (3,2))
print("ones array\n", array_1)

array_emp = np.empty(shape = (1,3), dtype = int)
print("empty array:\n", array_emp)

#output:
'''1-D array: 
 [1 2 3 4 5]
zero's array:
 [[0 0 0 0 0]
 [0 0 0 0 0]]
ones array
 [[1. 1.]
 [1. 1.]
 [1. 1.]]
empty array:
 [[0 0 0]]'''       
 
 
 # array from existing data
import numpy
numpy.array(object, dtype = None, copy = True, order = None, subok = False)

# object : array_like
# dtype : data type
# copy : boolean
# order : {'K', 'C', 'F', 'A'}
# subok : boolean   

#output:
#array(<class 'object'>, dtype=object)


'''Parameters:
    Object - it can be a set, tuple, dictionary Etc.
    dtype - it represents the type of the object, by default the type is none
    Copy - it means object is copied. By default value is true. It is an optional attribute
    Order - we can arrange arrays in 3 possible ways c(column order), R(row order), A(any)
    SUBOK - by default the base class is array, by making this attribute true we can make subclasses
    ndim - to define the minimum dimension of the array
'''

#array from list data
ar = np.array({1, 2, 3}) #or

ar = np.array([1, 2, 3], float) #or

ar = np.array((1, 2, 3), complex)



list = [[5, 6, 7], [1, 2, 3], [8,9,7]]

array_from_list = np.asarray(list)

print("array from list: \n", array_from_list)

print(ar)

print(type(ar))

#output:
'''array from list:
 [[5 6 7]
 [1 2 3]
 [8 9 7]]
[1.+0.j 2.+0.j 3.+0.j]
<class 'numpy.ndarray'>'''  



# array from tuple

tuple = ((2, 2, 3), (1, 2,3))

A = np.asarray(tuple, dtype = float)
print("array from tuple:\n", A)

B = np.array(((1, 2, 3), (4, 5, 6)))
print("array from tuple:\n", B)

c = (1, 2,3, 4, 5)
c = np.asarray(c)
print("array from tuple:\n", c)

#output:
'''array from tuple:
 [[2. 2. 3.]
 [1. 2. 3.]]
 '''
 
 
 
'''Ndarray object attributes

• ndim - to define the minimum dimension of the array
• D type - is used to get the type of the elements of the array
• Shape - hey it is used to get the shape of the given array. Means number of rows and columns in array
• size is used to get the number of elements of the array of the size of the array
• itemsize - to find the size of each element in the array.

'''

# array attributes
a = np.array([[1, 2, 3 ], [2, 3, 4], [4, 5, 6]])
print(a)
print("dimension: ", a.ndim)
print("data type: ", a.dtype)
print("size of array: ", a.size)
print("shape of array: ", a.shape)
print("size of elements: ", a.itemsize)


#output:
'''
[[1 2 3]
 [2 3 4]
 [4 5 6]]
dimension:  2
data type:  int64
size of array:  9
shape of array:  (3, 3)
size of elements:  8
'''

from IPython.utils.text import string

lt= ([[1, 2,3 ], [2, 3, 4], [4, 5, 6]])

a = np.array(lt, dtype = float)
print("array from:",lt )

#output:
'''array from: [[1, 2, 3], [2, 3, 4], [4, 5, 6]]'''
print(a)
#output:
'''[[1. 2. 3.]
 [2. 3. 4.]
 [4. 5. 6.]]''' 
 
 
 # restructing the shape of the ndarray

a = np.array([[1,2], 
              [2,3], 
              [5,6]])
print("original array")
print(a.shape)

reshaped_array  = a.reshape(2,3)
print("reshaped array:\n", reshaped_array.shape)

#output:
'''original array
(3, 2)
reshaped array:
 (2, 3)'''
 
 
 #slicing the array
# to extract the range of elements from an array we can use slicing
# it is same as we have used in the list

a = np.array([1, 2, 3, 4, 5, 6])
print(a[0:4])

#output:
'''[1 2 3 4]''' 

#slicing with step
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11 ])
print(a[0:11:2])

#output:
'''[ 1  3  5  7  9 11]'''




'''Numpy array using numerical range

• arange - the arrange() function is used to create an array of evenly spaced elements over the given range

• linspace – the linspace() function is used to get evenly spaced elements over the given interval range

• logspace – the logspace() function is used to create an array of evenly spaced values according to log scale

np.arange(start, stop, step)

np.arange(6) - stop

np.arange(2,6) - start, stop

np.arange(1,6,2) - start, stop, step

np.linspace(sart, stop, num)

np.linspace(0,0.5,6)

'''

a = np.linspace(1, 20, 5)
print(a)

a = np.arange(0, 10, 2, float)
print("ranged array: \n", a)

l = np.logspace(2,10,5)
print("logspaced array: \n", l)

#output:
'''[ 1.    5.75 10.5  15.25 20.  ]
ranged array: 
 [0. 2. 4. 6. 8.]
logspaced array: 
 [1.00000000e+02 1.77827941e+04 3.16227766e+06 5.62341325e+08
 1.00000000e+11]'''     
 
 
'''Aggregate operations on array
.we can perform aggregate function on the array such as: sum(), max(), min() etc.
'''

a = np.array([1, 2, 3, 4, 5])
print(type(a))
print("sum: ", np.sum(a))
print("max: ", np.max(a))
print("min: ", np.min(a))
print("std: ", np.std(a))
print("square root: ", np.sqrt(a))

#output:
'''<class 'numpy.ndarray'> 
sum:  15
max:  5
min:  1
std:  1.4142135623730951
square root:  [1.         1.41421356 1.73205081 2.         2.23606798]'''       



#To perform arithmetic operations the shape of the arrays must be the same.

import numpy as np
a = np.array([[1, 2, 3], [2,4,5]])
b = np.array([[2,4,6], [4,6,8]])
print("addition: ", a+b)
print("subtraction: ", a-b)
print("multiplication:", a*b)
print("division: ", a/b)

#output:
'''addition:  [[ 3  6  9]
 [ 6 10 13]]
subtraction:  [[-1 -2 -3]
    [-2 -2 -3]]
multiplication: [[ 2  8 18]
 [ 8 24 40]]
division:  [[0.5        0.5        0.5       ]
 [0.5        0.66666667 0.625     ]]'''     
 
 

'''Ndarray axis
we can perform operations row and column wise on array
'''


print(a)
print("max: ", a.max(axis = 1))
print("min: ", a.min(axis = 1))
print("sum: ", a.sum(axis = 1))

#output:
'''[[1 2 3]
 [2 4 5]]
max:  [3 5]
min:  [1 2]
sum:  [ 6 11]'''


# for array concatination we use np.concatenate()
# we can concatenate multidimensional arrays vertically and horizontally

a = np.array([[1,2,3], [1,3,4]])
b = np.array([[5,6,7], [8,9,10]])

print("vertically concat: \n", np.vstack((a,b)))
print("horizontally concat: \n", np.hstack((a,b)))

#output:
'''vertically concat:
    [[ 1  2  3]
    [ 1  3  4]
    [ 5  6  7]
    [ 8  9 10]] 
    
horizontally concat:
    [[ 1  2  3  5  6  7]
    [ 1  3  4  8  9 10]]
    '''

'''iteration over the array
nditer() function is used to iterate through arrays
'''

na = np.array([[1,2,3],[5,6,7]])
print("array: \n", na)

for x in np.nditer(na):
  print(x, end = " ")
  
  
#output:
'''array:
 [[1 2 3]
 [5 6 7]]
1 2 3 5 6 7 '''


'''Numpy string functions

• add() - it is used to add string type element to array
• multiply() - it is used to obtain the multiplied copy of the string element
• center() - it is used to make a centre aligned string filled with specified number of character
• capitalize() - it returns to copy of a string with the first letter capitalized
• title() - it returns to title case string
• lower() - it returns a string with lower case letters
• upper() - it returns a string with uppercase letters
• split() - it returns the words from string
• splitlines() - it breaks the list of lines
• strip() - it removes the left and right spaces
• join() - it joins the given sequence of strings
• replace() - it replaces all the occurring words of the substring in a string
• decode() - it is used to decode the string in a specified format
• encode() - it is used to encode a string into a specified code
'''

'''Numpy data types

numpy provides a wide range of data types. We can create the dtype objectives follows:
numpy.dtype(object, align, copy)
'''

d = np.dtype([('salary', float)])
arr = np.array([(10000.12,), (20000.50,)], dtype = d)
print(arr['salary'])

#output:
'''[10000.12 20000.5 ]'''

#--------------------->>

ar/r = np.array(([1,2,3],[4,5,6]))
arr
#output:
'''array([[1, 2, 3],
       [4, 5, 6]])'''   


arr = np.zeros(5)
arr
#output:'''array([0., 0., 0., 0., 0.])'''


arr = np.zeros((3,5))
arr
#output:
'''
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
'''


arr = np.zeros((3,5,2))  # 3 elements with 5x2 matrix
arr

#output:


'''array([[[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]],

       [[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]]])
        '''


arr = np.ones((2,3,5))*5    # broadcasting happens
arr

#output:
'''array([[[5., 5., 5., 5., 5.],
        [5., 5., 5., 5., 5.],
        [5., 5., 5., 5., 5.]],

       [[5., 5., 5., 5., 5.],
        [5., 5., 5., 5., 5.],
        [5., 5., 5., 5., 5.]]])
        '''     

 # np.arange(start,stop,step)

 # linspace():-   np.linspace(start, stop, num)

 # linspace():-   np.linspace(start, stop, num)

 # linspace():-   np.linspace(start, stop, num)