
'''
[Collections]:
.In python collections are containers that are used to store collections of data.
For example: 
   List, Dict, Set, Tuple etc,.

Lists:
.It is a sequence of datatype which is used to store the collections of data. 
.It contains multiple values in an ordered sequence.
.Lists are enclosed in [ ] brackets
.Standard heterogenous collection
'''

# List of Strings
         # values inside a list are items, are separated by comma delimited
friendsNames = ['Joseph', 'Glenn', 'Sally']
print(friendsNames)

# List of Integers
friendsAges = [20,22,24,25]
print(friendsAges)

# List of Integers and Strings
friendsAndAges = ['Joseph',22,24,25]
print(friendsAndAges)

# A list element can be any python object,even another list
print([1, True, 4-7j, [5, 6], 7, "Joseph"])

# A list can be empty
print([])


# Access the elements insides a List
# .It is a sequence of data items
# . we can index them just like in strings, index specified in square brackets[]

# List Indexing:


# list element starts from 0 which means zero as its index
friendsNames1 = ['Joseph', 'Glenn', 'Sally']
print([friendsNames1[1]])

# .Negative indexing for accessing elements in a list. 
# .The index of -1 refers to the last item, -2 refers to second last.
ages = [20, 22, 24, 25]
print(ages[-2])

# .List can also contain other list values. 
# .The values in these list of list can be accessed using multiple indexes
 
a = [['Joseph', 'Glenn', 'Sally'],[20, 22, 24, 25]]
a = [['Joseph', 'Glenn', 'Sally'],[20, 22, 24, 25]]
print(a[0][2]) 
    # The first indicates which list values to use, and second indicates values within the list.
    
print(a[1][2])
    # Here a[1] indicated the 1st position inside the multiple list and
    # [2] indicate the 2nd position inside the list
    
#    
# print(a[1,2][2,3])  

    # In the above example list should indicates integers or slices, not tuples
    
 #example:1
    
a = [['Joseph', 'Glenn', 'Sally'],[20, 22, 24]]
print(a[0][1],a[1][2])
# The first indicates which list values to use, and second indicates values within the list.
 #To print the Glenn and 24 from the above list of lists
 
 
    
# List slicing:


# As index can get single values from a list, slice can get several values from a list in the form of new list(sublists), it is similar like an index, but it has two integers seperated by a colon
    
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[0:3])

print(friends[1:2])

print(friends[0:-1])

print(friends[1:])  


# prints list in reverse order
print(friends[::-1])
#output: ['Sally', 'Glenn', 'Joseph']



# Getting list's length:


# The len() function will return the number of values that are in a list value passed to it, just like it count number of characters in a string value
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))


a = [1, 2, 'joe', 99]
print(len(a))

b = [[1, 2, 'joe', 99],[1,'fsdafasdf',333.5]]
print(len(b))
#output: 2


# Change/ Update the values inside the list with indexes:


# Strings are 'immutable'
# Cannot change the contents of a string
# must create a new string to make any changes

# a = 'Hello World'
# a[0] = 'J'

a = 'Hello World'
a = 'J' + a[1:]
print(a)  # Output: Jello World


# Lists are 'mutable'
# we can change an element of a list using the index operator

ages = [20, 22, 24, 25]
print(ages)
        #output is [20, 22, 24, 25]
ages[2] = 28
print(ages)
        # output is [20, 22, 28, 25]
        

# List concatenation and repetition:

# List can be concatenated and replicated just like strings
# The + operator combines two lists to create a new list value

friends = ['Joseph', 'Glenn', 'Sally']
a = friends + [20, 22, 24]
print(a)
#output: ['Joseph', 'Glenn', 'Sally', 20, 22, 24]

# The x operator can be used with a list and an integer value to replicate the list
print([20, 22, 24] * 3)
#output: [20, 22, 24, 20, 22, 24, 20, 22, 24]



# Range function:


# returns a list of numbers that range from zero to one less than the parameter
print(range(9))
    #output: range(0, 9)
    
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends)) # the output when we print len of friends

friends = ['Joseph', 'Glenn', 'Sally']
print(range(len(friends))) # the output will be range of values/elements in a list

frineds = ['Joseph', 'Glenn', 'Sally','asdfasdfa','sdfasdfasdfg','sdfaagagfalhabfka']
print(range(len(friends))) # the output will be range of values/elements in a list
#output: range(0, 6)