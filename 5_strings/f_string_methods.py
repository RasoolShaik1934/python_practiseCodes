'''
[String built-in Methods]:
    .A method is a function that is associated with an object
    .Methods are called on objects and can modify the object or return a new object
    .Methods are defined within a class and can access the object's data
    .Methods are called using the dot notation: object.method(arguments)
    .Methods can take arguments and return values, similar to functions
    .Common string methods include upper(), lower(), replace(), find(), and split()
    
 .A Method is similar to a function-it takes arguments and returns a value- but the syntax is different
 .Instead of the function syntax upper(word),it uses the method syntax word.upper()
'''

#p1
# Example: Converting a string to uppercase
word = "hello"
upper_word = word.upper()  # Output: "HELLO"
print(upper_word)


#p2
# Example: Converting a string to lowercase
lower_word = word.lower()  # Output: "hello"
print(lower_word)


a = "Hello World"
a.find('r')  #output: 8

word = "HelloWorld"
print(word.title()) # Output: HelloWorld


# capitalize()
word = 'helloworld'
word.capitalize() # Output: 'Helloworld' 

# swapcase()
word = 'Hello World'
word.swapcase() # Output: 'hELLO wORLD'






#Copilot:Questions

# index()
a = 'Python Programming'
print(a.index('g')) # Output: 10

# count()
a = 'Pyhton    Programming'
print(a.count(" "))  # Output: 4
print(a.count("P"))  # Output: 2
                  #it is counting the total spaces in between the word
                  #it is counting the total 'P' in the word

# encode()
#  converts a string value into a collection of bytes using an encoding scheme(utf-8) specified by the user
a = "My name is Ståle"
print(a.encode()) # Output: b'My name is St\xc3\xa5le'

# center()
#  String method centers the text
'Hello'.center(20) # Output: '       Hello        '

# format()
#  format method formats the specified value(s) and insert them inside the string's placeholder
a= 'Hello'.center(20,'+')
print(a)           # Output: +++++++Hello++++++++

b= 'Hello'.center(20,'=')
print(b)          # Output: =======Hello========

c= 'Hello'.center(20,'*')
print(c)          # Output: *******Hello********


# placeholder:
#   This is defined using curly brackets:{}
print("The sum of 1 + 2 is {0}".format(1+2)) # Output: The sum of 1 + 2 is 3


# join():
#  join method is useful when you have a list of strings that need to be joined together into a single string value
#  join method is called on string gets passed a list of strings, and returns a string
a = "Hello World!"
b = '_'.join(a)
print(b)
' '.join(['My', 'name', 'is', 'Ståle'])

#output
#H_e_l_l_o_ _W_o_r_l_d_!
#My name is Ståle

## split():
'My name is Ståle'.split()

#split() methods:
#  this method is called on a string value and returns a list of string
a = "Hello World!"
b = a.split(" ")
print(b)

# Removing whiteSpaces with strip() method
#  This strip() string method will return a new string without any whitespace characters at the beginning or end
a = "    HelloWorld!  "
b = a.strip(" ")
print(b) 
  #  Inside the string where word starts from there the  strip starts
  
# lstrip() method:
#  This Will remove the whitespace characters from the left side of the string
a = "HelloWorld!   "
a.lstrip()

# rstrip() method:
#  This Will remove the whitespace characters from the right side of the string
a = "    HelloWorld!   "
a.rstrip()



# Copilot:
#p3
# Example: Replacing a substring in a string
replaced_word = word.replace("l", "x")  # Output: "hexxo"
print(replaced_word)


#p4
# Example: Finding the index of a substring in a string
index = word.find("l")  # Output: 2 (the index of the first occurrence of "l")
print(index)



#p5
# Example: Splitting a string into a list of substrings
sentence = "Hello, World!"
words = sentence.split(", ")  # Output: ["Hello", "World!"]
print(words)


#p6
# Example: Joining a list of strings into a single string
joined_sentence = " ".join(words)  # Output: "Hello World!"
print(joined_sentence)



#p7
# Example: Checking if a string starts with a specific substring
starts_with_hello = sentence.startswith("Hello")  # Output: True
print(starts_with_hello)


#p8
# Example: Checking if a string ends with a specific substring
ends_with_exclamation = sentence.endswith("!")  # Output: True
print(ends_with_exclamation)


#p9
# Example: Stripping whitespace from a string
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()  # Output: "Hello, World!"
print(stripped_string)


#p10
# Example: Checking if a string contains only alphabetic characters
is_alpha = word.isalpha()  # Output: True (since "hello" contains only alphabetic characters)
print(is_alpha)


#p11
# Example: Checking if a string contains only numeric characters
is_numeric = "12345".isnumeric()  # Output: True (since "12345" contains only numeric characters)
print(is_numeric)


#p12
# Example: Checking if a string contains only alphanumeric characters
is_alphanumeric = "Hello123".isalnum()  # Output: True (since "Hello123" contains only alphanumeric characters)
print(is_alphanumeric)


#p13
# Example: Checking if a string contains only whitespace characters
is_space = "   ".isspace()  # Output: True (since the string contains only whitespace characters)
print(is_space)


#p14
# Example: Checking if a string is a valid identifier
is_identifier = "my_variable".isidentifier()  # Output: True (since "my_variable" is a valid identifier)
print(is_identifier)


#p15
# Example: Converting the first character of a string to uppercase
title_case = "hello world".title()  # Output: "Hello World"
print(title_case)


#p16
# Example: Converting the first character of each word in a string to uppercase
capitalized_string = "hello world".capitalize()  # Output: "Hello world"
print(capitalized_string)


#p17
# Example: Checking if a string is in title case
is_title_case = "Hello World".istitle()  # Output: True (since "Hello World" is in title case)
print(is_title_case)


#p18
# Example: Checking if a string is printable
is_printable = "Hello, World!".isprintable()  # Output: True (since "Hello, World!" is printable)
print(is_printable)


#p19
# Example: Checking if a string is a valid decimal number
is_decimal = "123.45".isdecimal()  # Output: False (since "123.45" is not a valid decimal number)
print(is_decimal)


#p20
# Example: Checking if a string is a valid hexadecimal number
is_hexadecimal = "1A3F".ishexadecimal()  # Output: False (since "1A3F" is not a valid hexadecimal number in Python)
print(is_hexadecimal)


#p21
# Example: Checking if a string is a valid binary number
is_binary = "101010".isbinary()  # Output: False (since "101010" is not a valid binary number in Python)
print(is_binary)


#p22
# Example: Checking if a string is a valid octal number
is_octal = "755".isoctal()  # Output: False (since "755" is not a valid octal number in Python)
print(is_octal)


#p23
# Example: Checking if a string is a valid URL
is_url = "https://www.example.com".isurl()  # Output: False (since "https://www.example.com" is not a valid URL in Python)
print(is_url)

'''
Other String Methods are:
.The replace() method is like a "search and replace" operation in a word processor
.isalnum() isalpha() isascii() isdecimal() isdigit(). etc,.
.Rfind() rindex() rjust() rpartition() rsplit() translate()
we can find more methods from the below link
https://docs.python.org/3/library/stadtypes.html#string-methods
'''