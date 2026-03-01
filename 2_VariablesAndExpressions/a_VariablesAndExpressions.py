  
#Dynamically typed and Strongly typed Statements

'''
.Strongly typed: the variables do have a type and that matters while doing the operations on variables
.dynamically typed: type is determined only during run time
.here some of the operations are prohibited for performing for example, performing addition on int and string datatypes
'''

a = 17
b = 'hello'
# c = a+b # here it should perform concatenation not addition hence it throws error


'''
Statements: 
these are unit of code in python interpreter
a = 2     Assignment statement
a = a+2   assignment with expression
print(a)  print statement

There are two types of statements in python:
    Single line statement - Assign a value to a variable
    Multi line statement - A statement may span over several lines - Preferred style to handle multi-line expressions is to break a long statement over multiple lines, wrap the expression inside parentheses, braces, & brackets - Another way to wrap multiple lines is by using a backslash () at the end of every line to indicate line continuation

'''
#Variables, Statements, Expressions Examples:
#p1
print("Welcome to Python")

#p2     
print(4)

#p3
type3 = type("Welcome to Python")
print(type3)

type4 = type(4)
print(type3)

type4 = type(3.2)
print(type3)
           #always consider the last code here and no space at the starting of the code
  
type6 = type('3.2')
print(type6)  # This will print the type of the string '3.2', which is <class 'str'>.
  #  Keeping code in single or double quote will always be consider as string
  
#p4
print(3 + 4)

print(3 - 4)

print(3 * 4)


'''
#Expressions:

These are the combination of values, variables and operators
.it may consist of one or more operands and 0 or more operators to produce a value
.operators are +,-,*,%...etc
order of operators(precedence): should know which operatior should perform first
. python follows PEMDAS rule i.e., paranthisis,exponential,multiplication,division,reminder,addition and subtraction and performs Left to right

'''
final = a+5 #here final is the variable, a&5 are operands, + is operator combining called as expression

# Arithmetic expressions
print("Arithmetic operations:")
a = 5
b = 10
x1 = a+b #addition
x2 = a-b # subtraction
x3 = a*b # multiplication
x4 = a/b # floating division
x5 = a//b # truncating division
x6 = a%b  # modulo
x7 = a**b # exponential
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)


#order of operation example
x = 1+2**3/4*5  # here first parenthesis is done followed by exponential followed by multiplication and division
print(x)
                #Here 2**3 is evaluated first, then division, then multiplication, and finally addition
                #Here the python follows PEMDAS rule i.e., paranthisis,exponential,multiplication,division,reminder,addition and subtraction and performs Left to right

x= 30
y= 8
q= x/y
# q= float(x)/float(y)
print(q)  # Here result value of int is converted to float
#output: 3.75


#--------------------------------------------------------------->>>>>>>>>>>>>>>>


#From COLAB Trupti:


print("apple \nmango \ncherry")
#output:
#apple
#mango
#cherry

# \n is an escape sentence

print("apple \tmango \tcherry")
#output:
#apple   mango   cherry   


# RAW String - string literals prefixed with 'r' or 'R'

'''🎯 When Should You Use Raw Strings?
File paths (Windows)
Regular expressions
When working with many backslashes
'''

print(r"c:\newoffice\office\file2025.txt")
#output: c:\newoffice\office\file2025.txt

print(R"c:\newoffice\office\file2025.txt")
#output: c:\newoffice\office\file2025.txt


# Swap numbers
a,b = 50, 100
print(a,b)
a,b = b,a        # a,b = 100, 50
print(a,b)

#output:
#50 100
#100 50



# id() - use to display memory address of the variable
a,b,c = 50,50,100
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))

#output:
#50 50 100
#140703203644432
#140703203644432
#140703203644496


# keywords in Python - keyword module

import keyword
print(keyword.kwlist)

#output:
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']  

len(keyword.kwlist)
#output: 35

# Type conversion in Python
str1 = "109870"
print(type(str1))
num1 = int(str1)     # explicit type conversion
print(type(num1))


str1 = "John5.6"
print(type(str1))
num1 = int(str1)    # not compatible
print(type(num1))
#output:
#<class 'str'>
#ValueError: invalid literal for int() with base 10: 'John5.6'  

#Here we are trying to convert a string that contains non-numeric characters to an integer, 
#which is not possible. Hence, it raises a ValueError indicating that the string cannot be converted to an integer.


str1 = "1098.70"
print(type(str1))
num1 = float(str1)     # explicit type conversion
print(type(num1))
#output:
#<class 'str'>
#<class 'float'>  


s1 = '78,700'
s1 = s1.replace(',', '')
print(s1)
#output: 78700

name = "Amit Rakesh Sharma"
name.split()
#output: ['Amit', 'Rakesh', 'Sharma']


n1,n2,n3 = input('Enter 3 values: ').split()
print(n1,n2,n3)
#output:
#Enter 3 values: 10 20 30
#10 20 30


n1,n2,n3 = input('Enter 3 values: ').split()
print(n1+n2+n3)
#output:
#Enter 3 values: 10 20 30
#102030
#Here the input values are treated as strings, so when we use the + operator, it concatenates the strings instead of performing addition.

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))

print(n1+n2+n3)
#output:
#Enter a number: 10
#Enter a number: 20
#Enter a number: 30
#60
#Here we are converting the input values to integers using int() function, 
# so when we use the + operator, it performs addition instead of concatenation.



n1,n2,n3 = map( int, input('Enter 3 numbers: ').split())
print(n1+n2+n3)
#output:
#Enter 3 numbers: 10 20 30
#60
#Here we are using the map() function to apply the int() function to each of the input values, 
# converting them to integers before performing the addition.


nums = input('Enter values: ').split()
print(type(nums))
#output:
#Enter values: 10 20 30
#<class 'list'>
#Here the input values are split into a list of strings, so the type of nums is <class 'list'>. 
# Each element in the list is a string representing one of the input values


name = 'John'
code = 'A303'
doj = '10-03-2023'
exp = 5
#print('My name is',name, 'and I joined on', doj)
print(f'My name is {name}. My code is {code}. \nI joined on {doj}.\nI have {exp} yrs of exp')
#output:
#My name is John. My code is A303.
#I joined on 10-03-2023.
#I have 5 yrs of exp  


'Jap' in "Japan"
#output: True

10 in [4,2,3,10,89,76]
#output
#True


