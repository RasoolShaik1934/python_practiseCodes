'''
[Variables:]
.One of the most powerful features of programming language is the ability to manipulate variables. 
.A variable is a name that refers to a value.
.An assignment statement creates a new variables and gives them values.
.Can start with letters but not numbers
'''
'''#[What are variables?]:
     A memory location that holds a data unit or a value
     Value:- A unit of data such as number, float, set of characters etc..
             Container to store values that can be accessed and changed
            Specify the variable name, and assign a value to it
            Call up value through variable name
            Eg:-  X=12.2
                  X is a Variable name
                  = is the Assignment operator
                  12.2 is the value assigned to the variable X
'''
'''
#[Variable "Data Types"]:
Numeric:- Integer,Float,Complex Numbers
Sequence:- Strings,Lists,Tuple
Others:- Boolean, Set, Dictionary
'''
#Variable Data Types Based on the data type of the variable, python allocates memory and decides what can be stored
'''
    NUMERIC:
        Int X = 10
        float X = 10.5
        complex X = 10+0j
    SEQUENCE:
        strings x = "hi my name is" or x = 'hi my name is'
        List
        Tuple
    Others:
        Boolean
        set
        Dictionaries
'''

#p1
message = "Welcome to Python programming"
message

#p2
'''1message = "Welcome to Python programming"
   1message
'''
        #above program shows error because variable should always start with letter not with number
#p3
n = 17
print(n)

#p4
pi = 3.5578585878
print(pi)

#p5
'''more@ = "1000"
 # more@
 '''
        #error shows: variable name should not contain special characters like @, $, %, etc.
    
#p6
'''class = "Advanced Theoretical"
'''
       #Class is a keyword you cannot use as a variable
        
''' Python has 35 keywords which cannot be used as a Variables
    False      class      finally    is         return
    None       continue   for        lambda     try
    True       def        from       nonlocal   while
    and        del        global     not        with
    as         elif       if         or         yield
    assert     else       import     pass
    break      except     in         raise
'''
               
'''
[Mnemonic Variable Names]:

Constants:- A constant is a type of variable whose value cannot be changed
            A constant is an identifier whose value cannot be changed throughout the
            execution of a program where as the variable value keeps on changing
            Python does not have built in constant types
            By conversion, Python uses a variable whose names contains all capital letters to define a constant
         Eg:- FILE_SIZE_LIMIT = 2000
'''
#[Mnemonic Variable Names]:

# first example
x1q329acd = 35.0
x1q3z9afd = 12.50
x1q3pq9afd = x1q329acd * x1q3z9afd
print(x1q3pq9afd)

# second example
a = 35.0
b = 12.50
c = a*b
print(c)

#third example
hrs = 35.0  # this has the clear understanding of why we used those variables
rate = 12.50
pay = hrs*rate
print(pay)


'''
Constant:
Constant is a types of variable whose value cannot be changed
    python doesn't have built in constant types, but by convention, the variable name with all capital letters used to define a constant.

eg: FILE_SIZE_LIMIT = 2000, PI = 3.14

'''
