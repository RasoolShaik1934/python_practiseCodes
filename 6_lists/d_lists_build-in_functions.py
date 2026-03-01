
# Built-in Functions and Lists
    # .There are a number of functions built-in into python that take list as parameters
    # .Remember the loops we built? these are much simpler
    
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
#output: 6

print(max(nums))
#output: 74

print(min(nums))
#output: 3

print(sum(nums))
#output: 154

print(sum(nums)/len(nums))
#output: 25.666666666666668



#p1
# Working with lists
# The below code is used with out using list
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)

#output:
# Enter a number: 10
# Enter a number: 20
# Enter a number: 30
# Enter a number: done
# Average: 20.0



#p2
# Rewrite the above code using lists
numList = list()

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numList.append(value)

average = sum(numList)/ len(numList)
print(average)
#output:
# Enter a number: 10
# Enter a number: 20
# Enter a number: 30
# Enter a number: done
# 20.0



#p3
# Split Method:
# Best Friends: strings and Lists


a = 'with three words'
b = a.split()
print(b)
#output: ['with', 'three', 'words']

print(len(b))
#output: 3

print(b[0])
#output: with



# split breaks a string into parts and produces a list of strings. 
# we think of there as words. we can access a particular word or loop through all the words.

print(b)
for w in b:
    print(w)
'''#output:
['with', 'three', 'words', 'always']
with
three
words
always
'''


# Use of Delimiter:

# .when you do not specify a delimiter, multiple spaces are treated like one delimiter
# .You can specify what delimiter character to use in the splitting

#p4
line = 'A lot of spaces'
a = line.split()
print(a)
#output: ['A', 'lot', 'of', 'spaces']


line = 'first;second;third'
b = line.split()
print(b)
#output: ['first;second;third']

print(len(b))
#output: 1

b = line.split(';')
print(b)
#output: ['first', 'second', 'third']

print(len(b))
#output: 3

'''
Summary:
.Concepts of a collection
.Lists and definite loops
.indexing and lookup
.List mutability
Function: len, min,max, sum
Slicing lists
List methods:append,Remove
Sorting lists
Splitting strings into lists of words
Using split to parse strings
'''



 
    