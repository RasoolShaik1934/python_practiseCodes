'''
[Expressions]:

An Expression is a combination of values,variables and operators.
.An expression may consists of one or more operands,and zero or more operators to produce a value
.Symbols that represent some actions are called Operators eg: +, -, *
   Example: result= X+2
      HERE: .result is variable to store expression value ,X is Operand/value ,+ is Operator
            .Arithmetic Expressions: +plus,-minus,*start and % percentage
            .Different operators: /slash for floating division //double slash for truncating division ** double star for exponential
            .Relational Operators: <less than, >greater than, <=less than or equal to, >=greater than or equal to, ==equal to, !=not equal to
            .Logical Operators: and, or, not
            .Bitwise Operators: &, |, ^, ~, <<, >>
            .Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=
      Copilot Prompt:
            .Unary Operators: +, -, ~
            .Binary Operators: +, -, *, /, //, %, **, &, |, ^, <<, >>
            .Comparison Operators: <, >, <=, >=, ==, !=
            .Logical Operators: and, or, not
            .Bitwise Operators: &, |, ^, ~, <<, >>
            .Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>= 
            .Augmented Assignment Operators: +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>= 
            .Membership Operators: in, not in 
                        
            .Identity Operators: is, is not
            .Membership Operators: in, not in
            .Conditional Expressions: if, else, elif
            .Ternary Operator: x if condition else y
            .Lambda Expressions: lambda arguments: expression
            .List Comprehensions: [expression for item in iterable if condition]
            .Set Comprehensions: {expression for item in iterable if condition}
            .Dictionary Comprehensions: {key: value for item in iterable if condition}
            .Generator Expressions: (expression for item in iterable if condition)
            .Function Calls: function_name(arguments)
            .Method Calls: object.method(arguments)
            .Indexing: list[index], string[index], tuple[index]
            .Slicing: list[start:end], string[start:end], tuple[start:end]
            .Attribute Access: object.attribute
            .Subscript Notation: list[index], dictionary[key]
            .Call Notation: function_name(arguments)
            .Conditional Statements: if condition: statement, elif condition: statement, else: statement
            .Loops: for item in iterable: statement, while condition: statement
            .Comprehensions: [expression for item in iterable if condition], {key: value for item in iterable if condition}, (expression for item in iterable if condition)
            .Decorators: @decorator_name
            .Context Managers: with open('file.txt') as file:
            .Assertions: assert condition, assert condition, "message"
            .Exceptions: try: statement, except Exception as e: statement, finally: statement
            .Generators: yield expression, yield from iterable
            .Coroutines: async def function_name(arguments), await expression
            .Async Iterators: async for item in iterable: statement
            .Async Comprehensions: [expression async for item in iterable if condition], {key: value async for item in iterable if condition}, (expression async for item in iterable if condition)
            .Type Hints: variable_name: type, function_name(arguments: type) -> return_type
            .Annotations: variable_name: "annotation", function_name: "annotation"
            .Docstring:docstring,docstring
            .Comments:#comment,comment,comment
            
            
  [Order of Operations(Precedence)]:
  
    Q)Does the order of operations or the precedence matter ? while evaluating the expression? YES.
  Ans): In any programming language an expression is evaluated from the precedence of the operators so that
        if there is more then one operator expression the precedence decide which operation should perform first
        This is called Operator precedence rules.

   Example:
        x=1+2*3-4/5**6
        Highest precedence rule to lowest precedence rule
It follows like below:
  1. Parenthesis ()
  2. Exponent           **   2**3 is 8
  3. Modulus/remainder  %    22%8 is 6
  3. Division           /    22//8 is 2
  3. Multiplication     *    3*5 is 15
  4. Addition           +    3+5 is 8
  4. Subtraction       -    5-3 is 2
  5. Expression will be evaluated from Left to right.
            
'''

#p1
# # Example for: Order of Operations(Precedence)
x = 1+2**3/4*5
print(x)
     # Output: 6.5 (because 2**3 is evaluated first, then division, then multiplication, and finally addition)
     
     
'''
 a)[Type conversion]:
 
 .Process of converting the object from one data type into another as per requirement. There are two types of conversions:
 
They are two types:
    1.[Explicit type] conversion also known as type casting (should do manually)
    2.[Implicit type] conversion also known as automatic type conversion (done by the interpreter automatically)
 
 .Explicit Type Conversion: It is done by the user using predefined functions like int(), float(), str() etc.
   Example: x = 10
            y = float(x) # Explicitly converting integer to float
            print(y) # Output: 10.0
            
 .Implicit Type Conversion: It is done by the Python interpreter automatically when it encounters mixed data types in an expression.
   Example: x = 10
            y = 3.5
            z = x + y # Implicitly converts x to float
            print(z) # Output: 13.5
            # In this case, Python automatically converts the integer x to a float before performing the addition
            # This is done to avoid loss of precision in the result.
            # Implicit type conversion is done automatically by the Python interpreter when it encounters mixed data types
            # in an expression. For example, if you add an integer and a float, Python will automatically convert the integer to a float before performing the addition.
            # This is done to avoid loss of precision in the result.

'''

print("Type Conversion Examples:")
# explicit type conversion
x = '30'
y = '8'
q = float(x)*float(y) # here we can converting str() to int() manually and performing operations
print("explicit value:", q)

# implicit type conversion
x = 123
y = 1.23
z = x+y
print("implicit value:", z)
type(z)        # Here the addition of float and an integer converts to float value

          
      
'''
USER INPUT:
python allows user to give input at the runtime by using input() function
converting user input: if we want to convert the string to number from the input we need to use type conversion function, as all the inputs are strings
'''
print("userInput Example:")
name = input("who are you")
print("welcome",name)

# converting user input
print("converting user input:")
x = float(input("enter number")) # it takes input as string and converts to int
y = x+1
print(y)
type(y)            
     
#p4
 #User input:
  #Reads a string from the user
  #Reads and returns an entire line of input

#example:
name =input("Who are you?")
print('Welcome',name)


#p5
# Convert User input:
  # Reads a number from the user
  # We must convert string to number using type conversation
  
# example:
x=input('Enter Number?')
y=float(x)+1       
            # took input from the user as float
print('Added Number',y)


# Comments in Python:

# Symbol'#':
  # used to explain the code
  # using # symbol can be used as comment
  
# Multiline comment"
"""
     """
     
     
'''b)[Operators and operands]

  .Operators and special symbols that represent computations like additions and multiplications. 
  .The values the operator is applied to are called operands.
  .The operators +,-,,/ and * are the following examples.
'''

#p1
print(20+32)

#p2
hour=10
minute=60
print(hour-1)

#p3
print(minute/60)

#p4
print(hour*60+minute)

#p5
print(minute/60)

#p6
print(5**2)

#p7
print((5+9)*(15-7))

#p8
minute=59
minute/60

#p9
# To obtain the same in Python 3.0 use (// integer) division
minute = 59
minute//60

# In Python 3.0 integer division functions much more as you would expect if you entered the expression on a calculator

#Modulus Operator(%):
  # It is also called as remainder operator
  # It returns the remainder after division of one number by another
# example:
print(7%3)  # This will print 1 because 7 divided by 3 leaves a remainder of 1.
print(10%4) # This will print 2 because 10 divided by 4 leaves a remainder of 2.
print(15%6) # This will print 3 because 15 divided by 6 leaves a remainder of 3.

#String operations:
  # Strings can be concatenated using the + operator
  # Strings can be repeated using the * operator
# example:
str1 = "Hello"
str2 = "World"
# Concatenation
result1 = str1 + " " + str2
print(result1)  # Output: Hello World
# Repetition
result2 = str1 * 3
print(result2)  # Output: HelloHelloHello
# Combining concatenation and repetition
result3 = (str1 + " ") * 2 + str2
print(result3)  # Output: Hello Hello World 


#Input operator:  # input() function is used to take input from the user
  # It reads a line from input, converts it into a string and returns it
# example:
name = input("Enter your name: ")
print("Hello, " + name + "!")

age = input("Enter your age: ")
print("You are " + age + " years old.")


prompt = "Enter a number: "
num = input(prompt)
print("You entered: " + num)

