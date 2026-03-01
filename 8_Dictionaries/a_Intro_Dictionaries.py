'''
#Dictionaries:
 .Dictionaries are used to store data values in Key:Value pairs. 
 .A dictionary is a collection which is ordered*, changeable, and doesn't allow duplicates. 
 .It allows us to do fast database like operations in python.
 
 .Lists index their entries based on the position in the list, while dictionaries index their entries based on keys.
 .Dictionaries we index the entries with a "lookup tag"
 
 
 copilot info:---------------------------------------->
 Lists are ordered collections of items, but dictionaries are unordered collections of key-value pairs.
 .Dictionaries are defined using curly braces `{}` with key-value pairs separated by a colon `:`.
 .Keys must be unique and immutable (strings, numbers, or tuples), while values can be of any type.
 .Dictionaries are mutable, meaning you can change their content without changing their identity.   
'''
# Introduction to Dictionaries in Python

# Example of a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30    
print(my_dict["city"])  # Output: New York

# Modifying a value in a dictionary
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'} 

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)
# Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}   

# Checking if a key exists
if "age" in my_dict:
    print("Age is present in the dictionary.")  
    
else:
    print("Age is not present in the dictionary.")
# Output: Age is present in the dictionary.
  
# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 31
# job: Engineer 

#------------------------------------------------->

#from video:  
dict1 = dict()
dict1['money'] = 12
dict1['candy'] = 3
dict1['tissue'] = 75

print(dict1)

print(dict1['candy'])  # Output: 3, Printing the value associated with the key 'candy'

# Adding a new key-value pair
dict1['candy'] = dict1['candy'] + 2
print(dict1)# Output: {'money': 12, 'candy': 5, 'tissue': 75}, Updated value for 'candy'


#Comparing Lists and Dictionaries
    #Dictionaries are like lists except that they use keys instead of numbers to look up values

# Example of List
lst = list()

lst.append(21)
lst.append(183)
print(lst)

lst[0] = 23
lst[1] = 184
print(lst)

# Example of Dictionaries
dict1 = dict()

dict1['money'] = 21
dict1['candy'] = 182
print(dict1)

dict1['money'] = 23
dict1['candy'] = 184
# The keys 'money' and 'candy' are used to access and modify the values
print(dict1)

#In Simple terms:
  #A list is like a box of items where you access them by their position (index).
  # A dictionary is like a box of items where you access them by their name (key).


#Dictionary Literals (Constants)
  #Dictionary literals use curly braces and have a list of key:value pairs
  #You can make an empty dictionary using empty curly braces



# Example of a dictionary literal
dict1 = {'chuck' : 1, 'jeff' : 42, 'jan' : 100 }
print(dict1)

dict2 = { }
print(dict2)



#Many Counters with a Dictionary
    #One common use of dictionaries is counting how often we "see" something

dict1 = dict()

dict1['mark'] = 1
dict1['steve'] = 1

print(dict1)

dict1['steve'] = dict1['steve'] + 1
print(dict1)


#When we see a new name
 #When we encounter a new name, 
 #     we need to add a new entry in the dictionary and if this the second or later time we have seen the name, 
 #     we simply add one to the count in the dictionary under that name


counts = dict()

names = ['steve', 'mark', 'steve', 'zhen', 'mark']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print('#p1')
print(counts)


#The get method for dictionaries
    #The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us
    
'''
    if name in counts:
    x = counts[name]
else:
    x = 0
    Defaults value if key does not exit (and no Trace back)
'''



# Simplified Counting with get()
    # We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one
    
counts = dict()

names = ['steve', 'mark', 'steve', 'zhen', 'mark']

for name in names:
    counts[name] = counts.get(name, 0) + 1 # '0' is default
print('#p2')
print(counts)



#Counting Words in Text:
# Counting pattern
    # The general pattern to count the words in a line of text is to split the line into words, 
    # Then loop through the words and use a dictionary to track the count of the each word independently
  
 #CopilotExample
text = "This is a test. This test is only a test."
words = text.split()  # Split the text into words
counts = dict()  # Create an empty dictionary to hold word counts
for word in words:
    counts[word] = counts.get(word, 0) + 1  # Increment the count for each word 
print('#p3')
print(counts)

# Counting Words in a Line of Text

print('#p4')
counts = dict()

print('Enter a line of text:')
line = input(' ')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)



# Definite Loops and Dictionaries
    # Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values
print('#p4')
counts = {'chunk' : 1, 'jeff' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])
    
 
# Retrieving Lists of Keys and Values
    # get a list of keys, values, or items(both) from a dictionary
print('#p5')

dict1 = {'chunk' : 1, 'jeff' : 42, 'jan' : 100}

print(list(dict1))

print(list(dict1.keys()))

print(list(dict1.values()))

print(list(dict1.items()))


# Bonus: Two Iteration Variables
    # We loop through the key:value pairs in a dictionary using * two * iteration variables.
    # Each iteration, the first variable is the key and the second variable is the corresponding value for the key
print('#p5')
dict1 = {'chunk' : 1, 'jeff' : 42, 'jan' : 100}

for keys, values in dict1.items():
    print(keys, values)
    

#Till now we have learned 
 # **get method,
 # dictionary loops,
 # counting patterns,
 # retrieving list of keys and values, 

# and two iteration variables usage**.

 #In this example program we will use all the concepts we learned

# Example Program: Counting Words in a File
# This program reads a file, counts the occurrences of each word, and prints the most common word and its count.
print('#p6')
# Open the file and read its contents
name = input('Enter file:')
handle = open(name)

counts = dict()
for lin in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(words, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


'''
Topics covered:- Introduction to dictionaries
- Creating and accessing dictionary elements
- Modifying dictionary elements
- Adding and removing elements
- Checking for key existence
- Iterating through dictionaries
- Using the `get` method for safe access
- Counting occurrences of items
- Counting words in a text
- Retrieving keys, values, and items
- Using two iteration variables in loops
- Example program for counting words in a file
'''