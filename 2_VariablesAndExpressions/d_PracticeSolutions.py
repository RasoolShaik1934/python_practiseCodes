# Exercise 1: Check the type for the following

'''a = 6
    b = 6.4
    c = "Hello"
    d = "17"
    print e = a + b and check the type of e
'''
print("#Exercise 1:")
a = 6
b = 6.4
c = "Hello"
d = "17"
e = a + b
print("type of a is",type(a))
print("type of b is", type(b))
print("type of c is", type(c))
print("type of d is", type(d))
print("type of e is", type(e))


'''Exercise 2: The goal of this exercise is to determine types and then change those types.Perform the following

    convert 7.999999999 to an int
    Convert 6 to a float
    '''
print("#Exercise 2:")
print(int(7.999999999))
print(float(6))


'''Exercise 3: The goal of this exercise is to assign values to variables. Variables can be assigned any value.
    Assign value 2 to the x variable and print x
    Add 1 to the variable x check the output
    Change x to 3.0 and add 1 to x
'''

print("#Exercise 3:")
x = 2
print(x)
x =  x + 1
print(x)
x = 3.0
print(x + 1)

'''
Exercise 4: The goal of this exercise is to learn standard ways to name variables by considering good and bad practices
    Create a variable called 1st_number and assign it a value of 1. Then check the output
'''
print("#Exercise 4:")
st_number = 1
print(st_number)

'''
Exercise 5 : Perform mathematical operations using more than one variable.

    Assign 5 to x and 2 to y
    Add x to x and subtract y to the second power than assign to the variable z. print the z
    Assign 8 to x and 5 to y in one line
    Find the integer division of x and y check the output.
'''
print("#Exercise 5:")
x = 5
y = 2

z = x + x - y ** 2
print(z)

x, y = 8, 5
print(x//y)

'''Exercise6: For given a and b values perform the following:

    Perform addition on a and b using the '+' operator
    Perform subtraction on a and b using the '-' operator
    Use the '*' multiplication operator to multiply the a and b
    Use the '/' division operator and observe the output
'''
print("#Exercise 6:")

a = 5
b = 2

print("addition of a + b = ", a + b)
print("subraction of a - b =", a - b)
print("multiplication of a * b is ", a * b)
print("a divided by b is", a // b)

'''
Exercise 7: Perform the following:
    Add '5' and '7' by converting them to int
    Determine the type of '5'
    Add '5' and '7
'''
print("#Exercise 7:")
a = int('5') + int('7')
print(a)

print(type(5))

print('5' + '7')