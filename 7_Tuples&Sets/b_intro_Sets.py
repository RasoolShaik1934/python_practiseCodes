'''
  Introduction to Sets: {,,,,}

    .A set is an object that stores a collection of data in the same way as mathematical sets. 
    .It is an unordered collections of object, unlike sequence objects such as lists and tuples.
    .Sets are defined by values separated by commas and enclosed in curly braces {}.
    .For example, a set of integers can be defined as {1, 2, 3}.    
    
    from copilot:
    .Sets are mutable, meaning that you can add or remove items from them.
    .However, the elements in a set must be immutable, i.e., they cannot be changed after they are created.
    .This means that you cannot have a set of lists or sets, but you can have a set of tuples or strings.
    
    from video:
    .All elements in the set must be unique, this are unordered, i.e. its elements are not stored in any particular order.
    .The elements that are stored in a set can be of different data types.
    .However, the set itself is mutable. i,e. we can add or remove items from it.
    .Sets can be used to perform mathematical set operations like union, intersection, symmetric differences, etc.
'''

#A set is created by placing all the elements inside curly braces {},separated by comma or by using the built-in function set{}


# Creating a set
numberSet = {1, 2, 3, 4, 3, 2}
print(numberSet)
#output
#{1, 2, 3, 4}
#As we can see the duplicate values are automatically removed


numberAndIntegersAndFlots = {2,8,6,3.5,5.6,7.4,"ra","rams"}
print(numberAndIntegersAndFlots)
#output
#{2, 3.5, 5.6, 6, 7.4, 8, 'ra', 'rams'}
#As we can see a set can contain elements of different data types


# Creating an empty set
emptySet = {} # This creates a Dictionary
print(type(emptySet))

  #output
  #<class 'dict'>
  
  
 #But a set cannot have a mutable element, like list or dictionary 
emptySet = set() # this creates an empty set
print(type(emptySet))


#A set can contain elements of different types

# A set of mixed data types
my_set = (1.0, 'Hello', (1, 2, 3))
print(my_set)

#output
#{1.0, 'Hello', (1, 2, 3)}


#A Set cannot contain lists
# Creating an empty set
set_with_lists = {[1, 2, 3]}
  #we will get a TypeError: unhashable type: 'list' a sets cannot contain mutable elements like lists or dictionaries


#We can convert a list to set using set function
set_with_lists = set([1, 2, 3])
print(type(set_with_lists))
print(set_with_lists)
#output
#{1, 2, 3}  


newList= [5,4,3,6,]
print(newList)

newList1=set(newList)
print(type(newList1))
print(newList1)

#output
#[5, 4, 3, 6]
#<class 'set'>
#{3, 4, 5, 6}

'''
  Adding elements to set:
    .Sets are mutable. but since they are unordered, indexing has no meaning
    .We cannot access or change an element of a set using indexing or slicing
'''

my_set = set()
my_set.update([9, 12])
my_set.update((3, 5))
my_set.update('SIKANDER')
print(my_set)

#output
#{3, 5, 9, 12, 'S', 'I', 'K', 'A', 'N', 'D', 'E', 'R'}


'''
    We can add single element using the add() method and multiple elements using the update() method
    The update() method can take tuples, lists, strings or other sets as its arguments.
    In all cases, duplicates are avoided
'''

my_set.update(('INDIA', 'BHARAT'))
print(my_set)

my_set.update(4, 5)

#output
#{3, 4, 5, 9, 12, 'S', 'I', 'K', 'A', 'N', 'D', 'E', 'R', 'INDIA', 'BHARAT'}



'''
Remove elements from a Set:
    #A particular item can be removed from set using methods, disard() and remove().
'''

print(my_set)

#Using discard(), if the item does not exit in the set, it remains unchanged.
my_set.discard(12)
print(my_set)
#output
#{3, 4, 5, 9, 'S', 'I', 'K', 'A', 'N', 'D', 'E', 'R', 'INDIA', 'BHARAT'}
#The above output have no change as 15 is not present in the set.

my_set.discard('BHARAT')
print(my_set)
#output
#{3, 4, 5, 9, 'S', 'I', 'K', 'A', 'N', 'D', 'E', 'R', 'INDIA'}
#The above output have removed 'BHARAT' from the set.


#But using remove(), if the items does not exist in the set, it will raise an error.

my_set.remove(15)



'''
#Set Membership Test:
    #We can test if an item exists in a set or not, using the in operator.
'''

# Initialize my set
my_set = set('apple')

# check if 'a' is present
# output: True
print('a' in my_set)

# check if 'p' is present
# output: False
print('p' not in my_set)




'''
#Remove Duplicate Elements:
    .Given a list of elements, remove the duplicate elements.
    .Read a string and find the number of unique characters in it.
'''

data = 'cranes varsity bangalore'
unique = set(data)
print('Number of unique characters=', len(unique))
print('List of unique characters=', unique)

#output
#Number of unique characters= 16
#List of unique characters= {'e', 's', 'v', 'g', 't', 'a', 'l', 'c', 'r', 'b', 'n', 'y', 'i', 'o', ' ', 'A'}

#To find the repeated characters in the string
data = list(data)
for ele in unique:
    data.remove(ele)
print('Repeated character', set(data))

#output
#Repeated character {'r', 'a', 'n'}




'''
Set Operations
    Sets can be used to carry out mathematical set operations like union, intersection, difference, and symmetric difference.
    We can do this with operators or methods
'''

# Example: Set Operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print('Union          =', A|B)
print('Intersection   =', A&B)
print('Difference     =', A-B)
print('Symmetric Diff =', A^B)

#output
#Union          = {1, 2, 3, 4, 5, 6, 7, 8}
#Intersection   = {4, 5}
#Difference     = {1, 2, 3}
#Symmetric Diff = {1, 2, 3, 6, 7, 8}