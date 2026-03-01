

'''Introduction to Numpy
NumPy (Numerical Python) is a python library for scientific computing, 
that provides high-performance vectors,
matrices and higher-dimensional data structures for Python.
'''

import numpy as np

'''Exercise 2: Print the numpy version and the configuration.

Hint: np.version, np.show_config
'''

print(np.__version__)
#output: 1.24.3



'''Exercise 3: Create an array of 10 zeros and 20 ones.
Hint: np.zeros, np.ones
'''

# YOUR CODE HERE
a = np.zeros(10)
print(a)

#output: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

a = np.ones(20)
print(a)
#output: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

'''Exercise 4: Create a vector with values ranging from 10 to 49.
Hint: np.arange
'''
a = np.arange(10, 50)
print(a)
#output: [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
# 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49] 

'''Exercise 5: Create a 3x3 matrix with values ranging from 0 to 8
Hint: np.arange, np.reshape
'''
a = np.arange(0, 9).reshape(3, 3)
print(a)
#output:
'''[[0 1 2]     
 [3 4 5]
 [6 7 8]]'''        
 
 
 # YOUR CODE HERE
z = np.arange(10,49)
print(z)

#output: [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
# 35 36 37 38 39 40 41 42 43 44 45 46 47 48]    
 
 
'''Exercise 5: Reverse a vector (first element becomes last).

Hint: np.array[::-1]
'''

a = np.arange(10)
print(a[::-1])
#output: [9 8 7 6 5 4 3 2 1 0]

# YOUR CODE HERE
z = np.arange(10,49)
z[::-1]

print(z[::-1])  
#output: [48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24
# 23 22 21 20 19 18 17 16 15 14 13 12 11 10]    


'''Exercise 6: Find the indices of the non-zero elements from [1, 2, 0, 0, 4, 0].

Hint: np.nonzero
'''

# YOUR CODE HERE
nz = np.nonzero([1,2,0,0,4,0])# Return the indices of the elements that are non-zero.
print(nz)

#output: (array([0, 1, 4]),)        


'''Exercise 7: Create a 3x3 identity matrix.

Hint: np.eye
'''

# YOUR CODE HERE
i = np.eye(3)
print(i)                
#output:
'''[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]''' 
 
 
'''
 Exercise 7: Generate a random number between 0 and 1 using numpy.
Hint: np.random.rand()
'''
 
r = np.random.rand(1)
print(r)

#output: 0.5488135039273248  (output will vary each time)


'''Exercise 8: Create a 10x10 array with random values, find the minimum and the maximum values.

Hint: min, max
'''

# YOUR CODE HERE
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

#output: 0.0038827878239602554 0.9945301228016671  (output will vary each time)


'''Exercise 9: Create a numpy array from the given List.

Hint: np.array
'''

# YOUR CODE HERE
list = [[1, 2], [3, 4]]
array = np.array(list)
print(array)
#array[::-1]

#output:
'''[[1 2]
 [3 4]]'''  


'''Exercise 10: Matrix multiplication for 1-D array.

To multiply the matrix a and b.

Hint: np.dot'''


a = np.array([9, 5, 7, 4])
b = np.array([9, 5, 4, 3])

# YOUR CODE HERE
np.dot(a,b)

#output: 158


matrix1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
matrix2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])

print(np.dot(matrix1,matrix2))

#output:
'''[[  64  322  107]
 [  81  500  113]
 [  87  316  111]]'''
 
 
'''Exercise 11: Transpose the given array [ [ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9], [10, 11, 12] ].
Hint: np.transpose( )
'''

# YOUR CODE HERE
np.transpose([[ 1, 2, 3],[ 4, 5, 6],[ 7, 8, 9],[10, 11, 12]])  

#output:
'''[[ 1  4  7 10]
 [ 2  5  8 11]
 [ 3  6  9 12]]'''
 
'''Exercise 12: Given an array A, calculate the square root of the elements in it.
Hint: np.sqrt( )
'''

A = np.arange(1,20)
print(A)
# YOUR CODE HERE
np.sqrt(A)

#output:
'''[1.         1.41421356 1.73205081 2.         2.23606798 2.44948974
 2.64575131 2.82842712 3.         3.16227766 3.31662479 3.46410162
 3.60555128 3.74165739 3.87298335 4.         4.12310563 4.24264069
 4.35889894]'''
 
 
'''Exercise 13: Concatenate two numpy arrays columnwise by specifying axis = 1.

Hint: np.concatenate( )
'''

# YOUR CODE HERE

c =np.array([[1,2],[3,4]])
d =np.array([[5,6],[7,8]])
# YOUR CODE HERE
print(c)
print(d)
np.concatenate((c,d))
q =np.concatenate((c,d), axis = 1)
print(q)

#output:
'''[[1 2]
 [3 4]]
[[5 6]
 [7 8]]
[[1 2 5 6]
 [3 4 7 8]]'''
 
'''Exercise 14: Print the second and the third column for the given multidimensional array.
'''

a = np.array([[2, 4, 6, 8, 10], 
              [3, 6, 9, 12, 15], 
              [4, 8, 12, 16, 20]]) 
# YOUR CODE HERE
print(a[:,1], a[:,2])

#output:
'''[4 6 8] [ 6  9 12]'''    

 
'''Exercise 15: For the given multidimensional array:

    Calculate the mean row wise by specifying axis = 0 and column wise by specifying axis =1.
    What is the average value of an array?
'''

# 2D array  
array = np.array([[[2, 4, 6, 8, 10], 
              [3, 6, 9, 12, 15], 
              [4, 8, 12, 16, 20]]]) 
#YOUR CODE HERE
print(array.mean())
print(array.mean(axis =1))
print(np.mean(array, axis=2))

#output:
'''10.0
[[3.         6.         9.        12.        15.        ]]
[[ 6.  9. 12. 16. 20.]]'''



'''Exercise 16: Create an array of all the even numbers from 30 to 70.

#YOUR CODE HERE
np.arange(30, 70, 2)

#output:
[30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68]'''


'''Exercise 17: For the given array, get the slice of the first row and print them.
'''

a3 = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
               [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
               [[30, 31, 32], [33, 34, 35], [36, 37, 38]]])

a3[0][0]

#output:
'''array([10, 11, 12])'''

a4 = np.array([[2,4,6],[1,2,3],[5,6,9]])
a4[0]

#output:
'''array([2, 4, 6])'''
