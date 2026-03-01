'''Exercise 01:
For the given tuple1 and tuple2, do the following:
    Concatenate tuple1 and tuple2.
    Multiply tuple1 with 2.
    Check the output for, 'a' in tuple2.
'''
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b' , 'c' ,'d' , 'e')

# Tuple Concatenation
tuple1 + tuple2
#output:
#(1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')

tuple1 * 2
#output:
#(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

'a' in tuple2
#output
#True

'''
Exercise 02:
Swap the following two tuples:
'''
tuple1 = (11, 22)
tuple2 = (99, 88)
#Expected output : tuple1 = (99, 88) , tuple2 = (11, 22)

print(id(tuple1))
print(id(tuple2))
#output
#132287678718528
#132287340750016

## YOUR CODE HERE
tuple1, tuple2 = tuple2, tuple1
print(tuple1, tuple2)
#output
#(99, 88) (11, 22)

'''Exercise 03:
Modify the first item of a list (22) inside a following tuple to 222.
'''
tuple3 = (11, [22, 33, [100,101], 21], 44, 55)
tuple3[1][0] = 222
tuple3[1][2][0] = 103
#Expected Output : (11, [222, 33], 44, 55)

#YOUR CODE HERE
tuple3[1][0] = 222
print(tuple3)
#output
#(11, [222, 33, [103, 101], 21], 44, 55)


'''Exercise 04:
Concatenate two tuples in the following order:
'''
tuple4 = (0, 1, 2, 3) 
tuple5 = ('Teacher', 'Student')

#Expected Output : (0, 1, 2, 3, 'Teacher', 'Student')

# YOUR CODE HERE
tuple6 = tuple4 + tuple5
tuple6
#output
# (0, 1, 2, 3, 'Teacher', 'Student')

'''Exercise 05:
For the given tuple, find the index of the sub-tuple whose elements makes a sum of 36.
'''
tuple1 = ((19,23),(20,22),(18,18),(16,20))

## YOUR CODE HERE
[tuple1.index(i) for i in tuple1 if i[0]+i[1] == 36]
#output
#[2, 3]

'''Exercise 06:
For the given tuple of numbers, do the following:
    Write a function which takes an integer 'N' as a parameter and returns the sum of multiples of 3 or 5 between 0 and N (limit). Where N is any element from the given tuple.
    Print all the sum of multiples for each element from the tuple.
    Example: If we list all the natural numbers less than 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9 and their sum is 23.
    '''
tuple2 = (10, 20, 30, 40, 50)

## YOUR CODE HERE
def getMultiples(N):
  sum = 0
  for i in range(1,N):
    if i%3==0 or i%5==0:
      sum += i
  return sum

[getMultiples(each) for each in tuple2]

#output
#[23, 78, 195, 368, 543]

#Sets
'''Exercise 07:
    Declare a set using curly brackets.
    Store it in a variable.
    Check the type of the object created.
    '''
# Declaring `set`, style1
myset1 = {"unordered", "collection", "of", "data"}
type(myset1)
#output
#set


'''Exercise 08:
    Declare a set using set() method.
    Store it in a variable.
    Print the results.
    '''
# Declaring `set`, style2
myset2 = set(["unordered", "collection", "of", "data"])
print(myset2)

#output
{'collection', 'of', 'unordered', 'data'}


'''Exercise 09:
    Declare a set.
    Add an element to set by using .add() over the object of set.
    Print the results.
'''
myset3 = {"unordered", "collection", "of", "data"}
myset3.add("allows")
print(myset3)
#output
#{'of', 'unordered', 'data', 'collection', 'allows'}