
'''Declare the values of a string variable to be 'Tests, Quizzes, Individual Labs, Group Labs and Hackathons'.
Print the string.
'''

# YOUR CODE HERE
#Exercise 1:
a="Tests"
b="Quizzes"
c="Individual Labs"
print(a,"\n",
      b,"\n",
      c,"\n")

#output:
'''Tests 
 Quizzes 
 Individual Labs
 '''
 
 # YOUR CODE HERE
 #Exercise 2:
d="I need Tables, Chairs, Cupboards"
print(d)

'''Exercise 3:
Concatenate the two string variables declared in Exercise 1 and Exercise 2.
# YOUR CODE HERE
'''

print(a + " " +d)

'''Exercise 6:
Perform simple string operations for A = "Hello", B = "world!":
    Concatenate by +.
    Multiple concatenation by * (ex: 4 * A + " " * 3 + B * 2).
    Check for substring with in.
    Determine the size (number of characters) using len.
'''
# YOUR CODE HERE
A = "Hello"
B = "world!"
C = A+B

print(C)

D = ((4*A)+" " +(B*2))
print(D)

A in A

E = len(A)
print(E)

'''output:
HelloTables, Chairs, Cupboards
Hello Tables, Chairs, Cupboards
HelloTables, Chairs, Cupboards
Helloworld!
HelloHelloHelloHello world!world!
5
'''

'''
Exercise 7:
For the given variable name = 'hELLO, WORLD!', perform the following:

    Print the character '!'.
    Convert the string to lowercase.
    Print the first character in upper case.
    Print a string where all the upper case letters are lower case and vice versa.
'''

name = 'hELLO, WORLD!'
# YOUR CODE HERE
name[::-13]

name.lower()

up = name.upper()
print(up)

up[0]

lc = name.swapcase()
lc.swapcase()

#output:
'!'
'hello, world!'
'H'
'Hello, world!'

'''
Exercise 8:
For a given string, perform the following:
    Using for to iterate over a string in Python.
    Print the number of times the letter/character ‘s’ appears in a string.
'''

# YOUR CODE HERE
name = 'hELLO, WORLD!'
count=0
for wordName in name:
  if wordName=='L':
   count=count+1
print(count)

#output:3

'''For a given list, perform the following:
    Print the list in reverse order.
    Print the following my_list[-1].
    Print the following output [2, 33, 222, 14] using slice method.
    '''

my_list = [2, 33, 222, 14, 25]
# YOUR CODE HERE
my_list.reverse()
print(my_list)
 
# output: [25, 14, 222, 33, 2]


my_list = [2, 33, 222, 14, 25]
# YOUR CODE HERE
my_list[-1]

# output: 25

my_list = [2, 33, 222, 14, 25]
# YOUR CODE HERE

my_list[0:4]
# output: [2, 33, 222, 14]


'''Exercise 10:
For the given string, perform following methods:
    Split the string by using 'word.split' and print the result.
    Replace MachineLearning by Python using .replace().
'''

# YOUR CODE HERE

name = 'hELLO, WORLD!'
name.split()

#output:
#['hELLO,', 'WORLD!']

word="MachineLearning career"
print(word.split(' '))

x = word.replace("MachineLearning","Python")
print([x])

#output:
#['Python career']