

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