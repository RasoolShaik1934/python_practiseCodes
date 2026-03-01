
'''Introduction to Tuples:
    .Tuples is a collection which is ordered and unchangeable.
    .It is much like a list, 
    .Main difference between tuple and list is that tuples are immutable.
    .Tuple-Represented as ( ) ex: (4,5,6) or ('devin', 'clark', 'Mont')
    .List-Represented as []
    .The values of tuples are syntactically separated by commas.
    
    Tuples are more efficient:
    .Python does not have a build tuple structure to be modified
    .They are simpler and more efficient in terms of memory use and performance than lists.
    
    .SO,in our program when we are making "temporary variables" we prefer tuples over lists
    
    .Tuples are like lists
    .Tuples are another kind of sequence that functions much like a list - they have elements that are indexed starting at 0
    '''
    
#p1
x = ('Glen', 'Sally', 'Joseph')
print(x[2])

#p2
y = (1, 9, 2)
print(y)

#p3
print(max(y))

#p4
for values in y:
    print(values)
    
   
    
# Tuples are 'immutable'
    # Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string.

#p5
# Lists are mutable
x = [9, 8, 7]
x[2] = 6
print(x)

#p5
 #Strings are immutable
'''
ex:1
y = 'ABC'
y[2] = 'D'

ex:2
z = (5, 4, 3)
z[2] = 0
'''

# Tuples are immutable
  
z = (5, 4, 3)
z[2] = 0   



# Things not to do with Tuples:

x = (3, 2, 1)
# x.sort() 
        #output:AttributeError: 'tuple' object has no attribute 'sort'
        
# x.append(5)
        #AttributeError: 'tuple' object has no attribute 'append'
        
# x.reverse()
        #AttributeError: 'tuple' object has no attribute 'reverse'
      
        

# A Tale of Two Sequences:
'''
    .Methods available for lists.
    .Since lists are mutable, these methods help to alter the lists.
        ex: we can do the following for lists:
        ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']      
'''
# example:1
l = list()
dir(l)

'''
['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
'''

'''
    .Methods available for tuples.
    .Since tuples are immutable, there are no such methods to alter it.
    ex: we can do following for tuples:
        ['count', 'index']
'''
# example:2
t = tuple()
dir(t)

['__add__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'count',
 'index']


# Tuples and Assignment:
'''
    .We can also put a tuple on the left-hand side of an assignment statement
    .We can even omit the parentheses
'''

#p6
(x,y) = (123,456)
print(y)
print(x,y)


(x,y) = (123,'Fred')
print(y)
print(x,y)

              # We can even omit the parentheses
x,y = (456,'Angelica')
print(y)
print(x,y)

x,y = 789,'Anne'
print(y)
print(x,y)




'''
   Tuples and Dictionaries:
      .The items() method in dictionaries returns a list of (key, value) tuples
'''
#Example for list of key values tuples:
#p1
d = dict()
 
d['mark'] = 2
d['steve'] = 4
for (k,v) in d.items(): # k,v denotes the key&value of the items
   print(k,v)
   
   #output:
    #mark 2
    #steve 4
   
   #To know the values which are hidden, can simply use the below code to know
tups = d.items()
print(tups)

   #output:
    #dict_items([('mark', 2), ('steve', 4)])
    
    
    
    
#Tuples are Comparable
    #The comparison operators work with tuples and other sequences.
    #If the first item is equal, Python goes on to the next element, and so on, until it finds element that differ.
    #Tuples 
#p2
(0, 1, 2) < (5, 1, 2)
(0, 1, 2000000) < (0, 3, 4)

ans = ('Jones', 'Sally') < ('Jones', 'Sam')
print(ans)
 #output
  #True
  
ans1 = ('Jones', 'Sally') < ('Adams', 'Sam')
print(ans1)
 #output
  #False
  
  
  
'''
Sorting Lists of Tuples:
    .We can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionary.
    .First we sort the dictionary by the key using the items() method and sorted() function.
'''

d = {'a' : 10, 'b' : 1, 'c' : 22}

d.items()
sorted(d.items())


#Using sorted():
   #we can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns sorted sequence.

d = {'a' : 10, 'b' : 1, 'c' : 22}
t = sorted(d.items())
t

#using a for loop to print the sorted key value pairs:
for k, v in sorted(d.items()):
    print(k, v)


 #Sort by values instead of key:
    #.If we could construct a list of tuples of the form(values, keys) we could sort by value
    #.We do this with a for loop that creates a list of tuples

c = {'a' : 10, 'b' : 1, 'c' : 22}

tmp = list()
for k, v in c.items():
    tmp.append((v, k))

print(tmp)

#output
#[(10, 'a'), (1, 'b'), (22, 'c')

tmp = sorted(tmp, reverse = True)
print(tmp)
#output
#[(22, 'c'), (10, 'a'), (1, 'b')



#Another example on Sort by values instead of key:

fhand = open('romeo.txt') # pass the text file
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
        '''        # Here we are using the get method of the dictionary to retrieve the current count of the word.
        If the word is not present in the dictionary, it returns 0 as the default value
        and then we add 1 to it.
        This way, we can count the occurrences of each word in the file.
        '''
        
# After the loop, we have a dictionary with words as keys and their counts as values.
# Now we can sort the dictionary by values:
c = {'a' : 10, 'b' : 1, 'c' : 22}
lst = list()
for key, val in c.items():
    lst.append((val, key))      
lst = sorted(lst, reverse=True) 
for val, key in lst:
    print(key, val)
    # This will print the words in descending order of their counts.
    
    #output
    '''c 22
       a 10
       b 1
    '''
    
 #example2:
c = {'a' : 10, 'b' : 1, 'c' : 22}
lst = [] #empty list
for key, val in c.items():
    newtup = (val, key)
    print(newtup)
    
    lst.append(newtup)
    print(lst)

lst = sorted(lst, reverse = True)

for val, key in lst[:10]:
    print(key, val)
    
#output
    #(10, 'a')
    #[(10, 'a')]
    #(1, 'b')
    #[(10, 'a'), (1, 'b')]
    #(22, 'c')
    #[(10, 'a'), (1, 'b'), (22, 'c')]
    #c 22
    #a 10
    #b 1 
    
    
    

#Even shorted version
    #We can also use list comprehension to dynamically create a list of reversed tuples and then sort it.

c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v, k) for k, v in c.items()]))

#output
#[(1, 'b'), (10, 'a'), (22, 'c')]