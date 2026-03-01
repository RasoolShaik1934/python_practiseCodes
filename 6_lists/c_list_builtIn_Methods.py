# List Built-in methods

x = list()
type(x) 
      # we get list datatype as output
#output: list

dir(x)
      # we get all the list builtin methods
#output:

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
 '__getstate__',
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

      
# Finding a value in list with index() method:

# List values have an index() method that can be passed a value, 
# and if that value exits in the list, the index of the value is returned

#p1
friends = ['Joseph', 'Glenn', 'Sally']
friends.index('Glenn')
#output: 1

friends.index('Sally')
#output: 2

friends.index('book')
#output: ValueError: 'book' is not in the list 




# Building a List from Scratch:
    # We can create an empty list and then add elements using the append() method

#p2
f = list()
f.append('Stale')
f.append(99)

print(f)
#output: ['Stale', 99]

#p3
f.append('book')
print(f)

# The insert() method:
# .Can insert a value at any index in the list

#p4
f.insert(1,'dog')
print(f)
#output: ['Stale', 'dog', 99, 'book']



'''Is something in a list?
    .Python provides two operations that let you check if an item is in a list
    .These are logical operators that return True or False
    .They do not modify the list
    '''
    
#p5
p = [1,9,21,10,16]
9 in p #output: True
15 in p
20 not in p #output: True




# Lists are in Order
    #.Lists of numbers values or lists of strings can be sorted with the sort() method

#P6
friends = ['Joseph', 'Glenn', 'Sally']

friends.sort() # returns string according to alphabetical order
print(friends)
#output: ['Glenn', 'Joseph', 'Sally']


order=['r','t','w','t','s','a','d', 'g','s','d','g','a']
order.sort()
print(order)
#output: ['a', 'a', 'd', 'd', 'g', 'g', 'r', 's', 's', 't', 't', 'w']



#P7
# Can also pass True for the reverse keywords arguments to have sort(), 
# sort the values in reverse order

friends.sort(reverse=True)
print(friends)
#output: ['Sally', 'Joseph', 'Glenn']


# The remove() method
# .Removes the first occurrence of the element with the specified value

friends.remove('Joseph')
print(friends)
#output: ['Sally', 'Glenn']

