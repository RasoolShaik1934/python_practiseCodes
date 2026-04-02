

'''We use functions to manipulate and pass data between different components of the program. 
It takes one or more functions as arguments and/or products a function as a result.

Combine simpler functions into new functions to express complex functions, 
can be found within the functools module, and a few others are built-ins. Example: map(), filter(), functools.reduce(), zip() etc.
'''

'''
Map() function
    The map() function takes another function and a sequence iterables as parameters and provide output after executing the function to each item in the sequence.
Using map()
Syntax : map(function, iterable)
    map : Applies the function to all elements of the iterable
    function parameter : A function
    iterable parameter : e.g. list, set, dictionary, tuple, string.
'''
def outer():
    def inner():
        return "Hello"
    return inner

f = outer()
print(f())

#output: Hello


# Using loop
result = []
nums = [1, 2, 3, 4, 5]

def square_fn(x):
    return x * x

for n in nums:
    result.append(square_fn(n))

print(result)

#output: [1, 4, 9, 16, 25]



# Equivalent to:
nums = [1, 2, 3, 4, 5]

def square_fn(x):
    return x * x

result = list(map(square_fn, nums))
print(result)

#output: [1, 4, 9, 16, 25]


'''
filter() function
    Python filter() function provides filtered elements. This function also takes another function and a sequence of iterables as parameters. The filter function returns a sequence for which function returns True
Using filter()
Syntax: filter(function, iterable)
    filter : Returns all the elements of the iterable for which the function returns True
    function parameter : A function that returns a boolean value
'''
# Using Loop
result = []
nums = [1, 2, 3, 4, 5]
def less_than_four(x):
    return x < 4

for n in nums:
    if less_than_four(n):
        result.append(n)

print(result)

#output: [1, 2, 3]

# Equivalent to
nums = [1, 2, 3, 4, 5]
def less_than_four(x):
    return x < 4

result = filter(less_than_four, nums)
print(list(result))

#output: [1, 2, 3]


'''
reduce() function
    Python reduce( ) function provides a single value on execution. This function also takes another function and a sequence of iterables as parameters. 
    The function tools module must be used to import this function
Using reduce()
Syntax : reduce(function, iterable
    reduce : It takes successive items of an iterable, and combines them in a way defined by the function
    function parameter : A function with two arguments and returns a single value
'''
# Example
result = 1
nums = [1, 2, 3, 4, 5]

def product(x, y):
    return x * y

for n in nums:
    result = product(result, n)
print(result)
#output: 120


'''
zip() function
    The zip( ) function take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples
    Just similar to unpack tuple, add the * to the object that we want to unpack
Syntax : zip(iterator1, iterator2 ..)
'''
name = ['Joseph', 'Glenn', 'Sally']

roll_number = [4, 1, 3]
marks = [40, 50, 60]

mapped = zip(name, roll_number, marks)

print(list(mapped))
#output: [('Joseph', 4, 40), ('Glenn', 1, 50), ('Sally', 3, 60)]


'''
Lambda function
    The lambda keyword is used to create inline functions
    Its quick declaration makes lambda functions ideal for use in callbacks, and when functions are to be passed as arguments to other functions
Syntax: lambda var1,var2,…: expression
'''

# Using Function
def square_fn(x):
    return x ** 2

def less_than_four(x):
    return x < 4

def product(x, y):
    return x * y

# Equivalent to
square_fn = lambda x: x ** 2

less_than_four = lambda x: x < 4

product = lambda x, y: x * y


'''
Lambda, map, filter, reduce, zip
    Lambda functions are especially useful when used in conjunction with functions like map, filter, reduce, zip
'''

# Example map
nums = [1, 2, 3, 4, 5]

def square_fn(x):
    return x * x

result = map(square_fn, nums)

print(list(result))
#output: [1, 4, 9, 16, 25]


# Equivalent to
nums = [1, 2, 3, 4, 5]

def square_fn(x):
    return x * x
    #the above step is not needed 

result = map(lambda x: x * x, nums)

print(list(result))
#output: [1, 4, 9, 16, 25]

# Example filter
nums = [1, 2, 3, 4, 5]

def less_than_four(x):
    return x < 4
    
result = filter(less_than_four, nums)
print(list(result))

#output: [1, 2, 3]

# Equivalent to
nums = [1, 2, 3, 4, 5]

result = filter(lambda x: x < 4, nums)

print(list(result))
#output: [1, 2, 3]

# Example reduce
from functools import reduce
nums = [1, 2, 3, 4, 5]

def product(x, y):
    return x * y

result = reduce(product,nums,1)
print(result)
#output: 120

# Equivalent to
from functools import reduce
nums = [1, 2, 3, 4, 5]

result = reduce(lambda x,y:x*y, nums, 1)
print(result)
#output: 120

# Example zip
num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
res = list(map(lambda x: sum(x), zip(num1, num2)))
print(res)
#output: [7, 9, 11, 13, 15]



'''
List Comprehensions:
    They provide a concise way to create lists
    Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable
    '''
    
 # Using loop
squares = []

for x in range(6):
    squares.append(x**2)
print(squares)

lt4 = []
for x in range(6):
    if x < 4:
        lt4.append(x**2)
print(lt4)   
#output: [0, 1, 4, 9, 16, 25]
#output: [0, 1, 4, 9]


# Example
squares = [x**2 for x in range(6)]
print(squares)

lt4 = [x**2 for x in range(6) if x < 4]
print(lt4)
#output: [0, 1, 4, 9, 16, 25]
#output: [0, 1, 4, 9]   


'''
List Vs Generators:
*Generator the 'next value' when it is asked for
    Instead of using a list to store all values, we can use a generator that generates the next value when it is asked for
    Reduces memory requirement when problem size is large
    We can make a function return a generator using the keyword yield
    If the body of a def contains yield, the function automatically becomes a generator function
'''

# Example
def generator_fn():
    yield 'Red'
    yield 'Green'
    yield 'Blue'
    yield 'yello'

print([value for value in generator_fn()])
#output: ['Red', 'Green', 'Blue', 'yellow']


# Generate Ngrams- without generator
tokens = ['i', 'want', 'to', 'go', 'to', 'school']

def ngrams(tokens, n):

    l = len(tokens)
    grams = [tokens[i:i+n] for
             i in range(l-n+1)]
    return grams

print(ngrams(tokens, 3))
#output: [['i', 'want', 'to'], ['want', 'to', 'go'], ['to', 'go', 'to'], ['go', 'to', 'school']]


# With generator
def ngrams(tokens, n):
  
    l = len(tokens)
    for i in range(l-n+1):
        yield tokens[i:i+n]

ngrams_gen = ngrams(tokens, 3)

print(ngrams_gen)
print([ng for ng in ngrams_gen])
#output: <generator object ngrams at 0x7f8e2c3d4b80>
#output: [['i', 'want', 'to'], ['want', 'to', 'go'], ['to', 'go', 'to'], ['go', 'to', 'school']] 



'''Decorator
    A Decorator takes a function as an argument, retuns a new function that is an enhancement of the original function
    '''
    
# Using function
def decorator_fn(func):
    def wrapper(*arg):
        ...

def some_fn(*arg):
    pass

some_fn = decorator_fn(some_fn)



# Syntax
def decorator_fn(func):
    def wrapper(*arg):
        output = func(*arg) + 2
        return output
    return wrapper

@decorator_fn
def some_fn(*arg):
    pass


#----------------------------------->>>>
#Trupti Class codes:

# Higher order functions - a function which accepts another function as an argument
# and returns a function as a result

def myfuncw(y):
  return y/y

myfuncw(20)
#output: 1.0


#----------------------->>>
# myApply is a higher order function

def myApply(function1, n):
  '''higher order function example'''
  print('********************')
  return function1(n)        # returning function1


# main code
myApply(myfunc, 30)     # sending myfunc as an argument

#output:
#  ********************
# 900


# lambda function
# syntax:-    lambda arguments: expression

cube = lambda x: x**3
cube(3)
#output: 27


product = lambda x,y: x*y
product(12,45)
#output: 540

#-------------------------->>

# filter, map, reduce
# syntax:-    filter(function, sequence)
# filter is a higher order function

mylist = [5,2,3,-9,7,-3,67,-12,46]
newlist = list(filter(lambda x: x>0  , mylist))
newlist
#output: [5, 2, 3, 7, 67, 46]


values = tuple(newlist)
values
#output: (5, 2, 3, 7, 67, 46)


mylist = [5,2,3,-9,7,-3,67,-12,46]
newlist = list(filter(lambda x: x>0 and x<50  , mylist))
newlist

#output: [5, 2, 3, 7, 46]

#--------------------------->>>
# map syntax:-map(function, sequence)


birds = ['parrot','crow','stork']
upperBirds = list(map(lambda b: b.upper(), birds))
upperBirds

#output: ['PARROT', 'CROW', 'STORK']

#---------------------------    

# Scale marks to a 0–1 range (important in ML preprocessing).
# Sample marks out of 100
marks = [45, 88, 72, 90, 55]
# divide each number by 100
norMarks = list(map(lambda m: m/100  , marks))
norMarks
#output: [0.45, 0.88, 0.72, 0.9, 0.55]


#---------------------------->>>
'''
Data Cleaning using map() and filter():-
Suppose you have a dataset of ages, and you want to:
Convert ages into categories (Young, Adult, Senior)
Remove invalid age entries
'''
# Sample raw age data (some invalid)
ages = [15, 25, -3, 120, 30, 70, 200]

# step 1: remove invalid ages
valid_ages = list(filter(lambda age: age>0 and age < 100 , ages))
valid_ages
#output: [15, 25, 30, 70]

'''
Data Cleaning using map() and filter():-
Suppose you have a dataset of ages, and you want to:
Convert ages into categories (Young, Adult, Senior)
Remove invalid age entries
'''
# Sample raw age data (some invalid)
ages = [15, 25, -3, 120, 30, 70, 200]

# step 1: remove invalid ages
valid_ages = list(filter(lambda age: age>0 and age < 100 , ages))
valid_ages
#output: [15, 25, 30, 70]

# step 2: categorize age using map
# Convert ages into categories (Young, Adult, Senior)

categories = list(map(lambda age: "Young" if age<20 else ("Adult"  if age < 60 else "Senior"),\
                 valid_ages))
categories
#output: ['Young', 'Adult', 'Adult', 'Senior']

#------------------------------->>>
# Sample raw age data (some invalid)
ages = [15, 25, -3, 120, 30, 70, 200]

def isValidAge(age):
  return age>0 and age<100

validAges = list(filter(isValidAge, ages))

validAges
#output: [15, 25, 30, 70]


#------------------------------>>>


# reduce
# syntax:    reduce(function, iterable/sequence)
# function with 2 arguments

from functools import reduce
nums = [4,2,3,1]
result = reduce(lambda x,y: x+y , nums)
result
#output: 10

'''result = reduce(lambda x, y: x + y, nums)
```
| Part | Meaning |
|---|---|
| `lambda x, y: x + y` | A function that **adds two numbers** |
| `nums` | The list to reduce |
| `x` | Accumulated result so far |
| `y` | Next element in the list |

'''
#---------------
nums = ['a','g','eeee','t']
result = reduce(lambda x,y: x+y , nums)
result
#output: 'ageeeet'



#----------------------------->>>
'''
Generators

A Generator in Python is a function that returns an iterator using the Yield keyword.
A generator function in Python is defined like a normal function,
but whenever it needs to generate a value, it does so with the yield keyword rather than return.
If the body of a def contains yield,
the function automatically becomes a Python generator function.

Note:
Python generators allows developers to generate sequences of values on the fly.
Unlike lists or arrays, generators don't store all the values in memory at once,
which can be very useful when working with large data sets or infinite sequences.
'''
'''
A generator function looks like a normal function but uses yield instead of return.
It does not run immediately — it returns a generator object that produces values one at a time, on demand.
'''

def generatorFunc():
  for i in range(5):
    print('hello')
    yield i

# main code
genObj = generatorFunc()   # create a generator object

#type(generatorFunc)
print(next(genObj))
print(next(genObj))
print(next(genObj))
print(next(genObj))
print(next(genObj))

#output:
# hello
# 0
# hello
# 1
# hello     
# 2
# hello
# 3
# hello
# 4

#------------------------->>

def generatorFunc():
  for i in range(5):
    print('hello')
    yield i

# main code
genObj = generatorFunc()   # create a generator object

# genObj becomes an itarable (can use it with for loop)

for j in genObj:
  print(j)

  #output:
# hello
# 0
# hello
# 1
# hello
# 2
# hello
# 3
# hello
# 4 

#---------------------------------------------------------->>>>

'''Decorator
    A Decorator takes a function as an argument, retuns a new function that is an enhancement of the original function
    '''

def msgFunc():
  print('This is my function')
  return 'such an amazing day'

msgFunc()
#output: This is my function
#output: 'such an amazing day'

#----------------------------------->>>>>

# enhance the working of the function
# return the message in upper case

# creating the decorator

def uppercase_decorator(myfunction):
  def wrapperFunc():
    func = myfunction()  # the returned value from myfunction will get stored in func
    makeUppercase = func.upper()
    return makeUppercase
  return wrapperFunc

#------------------------------>>
# let's apply the decorator
# use the @ symbol to apply it on a function

@uppercase_decorator
def msgFunc():
  #print('This is my function')
  return 'such an amazing day'

'''
internally uppercase_decorator will be an outer function
and msgFunc will be send as an argument and act like an inner function
'''

msgFunc()
#output: 'SUCH AN AMAZING DAY'

#-------------------------------->>

# Timing a model training step using a decorator

# decorator to track execution time of a model training

import time

# decorator to measure time
def timer(func):
  def wrapper():
    start = time.time()
    func()
    end = time.time()
    print(f"Execution time: {end - start: .2f} seconds")
  return wrapper

@timer
def train_model():
  print('Training model...')
  time.sleep(2)   # simulate training time

train_model()


#---------------------------------->>

def decoratorFunc(func):
    def wrapper(name):
      name1 = func(name.upper())
      return name1
    return wrapper

@decoratorFunc
def greet(name):
  print(name)

greet("John")
#output: JOHN

