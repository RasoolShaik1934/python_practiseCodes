'''Manually Created Functions
Functions are very easy to write in python and all non-trivial programs have functions. Function names have the same rules as variable names.
Built in Functions
Python comes with a nice set of built-in functions The complete set can be seen at:https://docs.python.org/3.6/library/functions.html
We take a look at the most used ones here. 
'''

#Manually Created Functions
'''Exercise 01: Build a function that takes the below string as a parameter and returns the words in the given string in backward order.
Hint: Split the words and join them in the reverse order using ' '.join(iterable)
'''
#string1 = "my name is johnny"

string3 = "my name is johnny"

def rev(string3):
  splitString = string3.split(' ')
  splittedJoined = ' '.join(splitString[::-1])
                      #the above step will make the sentence reverse
  return splittedJoined

rev(string3)

#output:
#'johnny is name my'  


string4 = "my name is johnny"

def rev(string4):
  for string4rev in string4:
   splitJoin = ' '.join(string4rev[::-1])
   print(splitJoin)

rev(string4)
#output:
#y n n o h j   s i   e m a n   y m  


text = "my name is johnny"
print(" ".join(word[::-1] for word in text.split()))
#output:
#ym eman si ynnhoj  



'''Exercise 02: For the given tuple of numbers, do the following:

    Write a function which takes an integer 'N' as a parameter and returns the sum of multiples of 3 or 5 between 0 and N (limit). Where N is any element from the given tuple.
    Print all the sum of multiples for each element from the tuple.
    Example: If we list all the natural numbers less than 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9 and their sum is 23
    '''
    
tuple2 = (10, 20, 30, 40, 50)

## YOUR CODE HERE
# def tuples2Fun():
  
# tuple3 = (10, 20, 30, 40, 50, 60, 70 ,80)

# def getMultiples(tuple3):
#   sum = 0
#   for i in range(0,tuple3):
#     if i%3==0 or i%5==0:
#       sum += i
#   return sum

# [getMultiples(each) for each in tuple3]


'''
Exercise 03: Build a function to print prime numbers within the given range.
'''

primes = []

for x in range(2, limit):
    is_prime = True
    for y in range(2, x):
        if x % y == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)

print(primes)

#output:
#[2, 3, 5, 7, 11, 13, 17, 19]   


## YOUR CODE HERE
limit = 20

[x for x in range(2, limit)if all(x % y != 0 for y in range(2, x))]

#output:
#[2, 3, 5, 7, 11, 13, 17, 19]



'''Exercise 4: Rock Paper Scissors: Complete the function below that takes the given input word as a parameter and selects a random element from the words list. It then prints the random word within the function and returns a string, declaring 'win' or 'lose' or 'tie'.
Example: Random input= 'Scissors', User input= Paper, Output = 'lose'
Hint: random.choice
'''

import random
words = ['Rock','Paper','Scissors']
input  = 'Paper'

def game(input):
  for options in words:
    randomGenerator =random.choice(words)
    print('The selected random choice was:', randomGenerator)
    
    if randomGenerator == 'Rock':
      print('loser')
    if randomGenerator == 'Paper':
      print('tie')
    if randomGenerator == 'Scissors':
      print('winner')

    return ('You Lose')

game(input)

#output:
#The selected random choice was: Scissors
#winner 

# -----Another Approach----->
import random
words = ['Rock','Paper','Scissors']
input  = 'Paper'

def game(input):
  choice = random.choice(words)
  print('The random choice was:',choice)  

  if choice == input:
    print('Its a Tie')

  elif choice == words[0]:
    print('You Win')
    
  else:
    print('You Lose')
  return None

game(input)

#output:
#The random choice was: Rock
#You Win


#Built-in Functions:


'''Exercise 05: Extract maximum value of each element in the given list using the built-in max function.
Hint: max(iterable)
'''

list1 = [[1,2,4],[5,6],[8,9,12],[21,44],[121]]

## YOUR CODE HERE Using For loop
def numbers(list1):
  for i in list1:
    itMax = max(i)
    print(itMax)

numbers(list1)

#output:
#4
#6
#12
#44
#121  

## YOUR CODE HERE 2 approach Using For each loop

[max(each) for each in list1]

#output:
#[4, 6, 12, 44, 121]

'''Exercise 06: For given list a and b perform the following Aggregate Functions
    len(iterable)
    max(iterable)
    min(iterable)
    sorted(iterable, key, reverse)
    sum(iterable, start)
    '''
a = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [5,10, 15, 20, 25, 30, 35, 40, 45, 50] 

print(len(a))
#output:
#10
print(max(b))
#output:
#50
print(min(b))
#output:
#5
print(sorted(a, reverse=True))
#output:
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sum(b))
#output:
#275        

#Another Approach Using Functions

# YOUR CODE HERE
lengthA=len(a)
print(lengthA)


print('Lenght of b is:', len(a),len(b))

print("Finding len of a and b", len(a), len(b))
print("Max values of a and b", max(a), max(b))
print("Min values of a and b",(min(a), min(b)))
print("Sorted values of a and b",sorted(a), sorted(b))
print("Sorted values of a and b",sorted(a), sorted(b))
print("Sum of the values of a and b",sum(a), sum(b))

#output:
#Lenght of b is: 10 10
#Finding len of a and b 10 10
#Max values of a and b 10 50
#Min values of a and b (1, 5)
#Sorted values of a and b [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#Sorted values of a and b [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10] [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#Sum of the values of a and b 55 275  



'''Exercise 07: Print the data type of x, y and z values
'''

x = 10
# YOUR CODE HERE
print(type(x))

y = 12.6
# YOUR CODE HERE
print(type(y))

z = x + y  
# YOUR CODE HERE
print(type(z))

#output:
#<class 'int'>
#<class 'float'>
#<class 'float'>


'''
Exercise 08: Initialize the string and perform the following:
    Check the type of string
    convert string to int and check the type
'''

a = '1234'
# YOUR CODE HERE
print(type(a))

intea = int(a)
print(type(intea))

#output:
#<class 'str'>
#<class 'int'>