'''
[Strings]:
.Def:A String is a series of characters
.Strings are used to represent text data
.Strings can be created using single quotes, double quotes, or triple quotes
.Can be single quoted or double quoted
.can be triple quoted with single or double quotes
.+ for concatenation
.* for repetition
.Strings are immutable
.Strings can be indexed and sliced
.Strings can be formatted using f-strings, format() method, or % operator
.Strings can be iterated over 
.Strings can be compared using relational operators
.Strings can be checked for membership using in and not in operators 
.Strings can be converted to other data types using str(), int(), float(), etc. 
.Strings can be split into a list of substrings using split() method 
.Strings can be joined using join() method 
.Strings can be stripped of whitespace using strip(), lstrip(), rstrip() methods 
.Strings can be checked for alphanumeric characters, digits, letters, lowercase, uppercase, etc. using isalnum(), isdigit(), isalpha(), islower(), isupper() methods 
.Strings can be checked for whitespace using isspace() method 
.Strings can be checked for printable characters using isprintable() method
'''

#--------->
 #Creating a string / String Operations:
greeting = "Hello, World!"
print(greeting)

print('program-1----->')
a = "Hello World !"
print (a)

print('program-2----->')
b = " I'm happy to use Python"
print (b)

print('program-3----->')
c = 'GvR Says, "Readability counts" and Python shines here'
print (c)

# Strings can also be triple quoted (with single quotes or double quotes)
print('program-4----->')
d = '''She said, "Thank you! it's mine."'''
print (d)

# String Concatenation using '+' operator
print('program-5----->')
a = "Hello"
b = "World"
c = a + b
print (c)

# String repetition
print('program---->6')
a = "Hello"
b = "World"
addingHelloWorld= 4*a+" "+3*b
print (addingHelloWorld)


#--------->
# Accessing characters in String:
 #.Each string is stored in the computers memory as a list of character 
 #.The index value must be an integer and starts at zero
 
#p2
a = "Hello!"
b = a[1]
print(b)

#p3
a = "Hello!"
b = a[-1]
print(b)
         # Accessing the character of string "Hello!" at last index 


#A character too far:
#p4
# a = "Hello!"
# b = a[9]   # This will raise an IndexError because index 9 is out of range for the string "Hello!"
# print(b)
             #Can get an error while running if you attempt to index beyond the end of string

#---------->


#p5
 #Length of the String
a = "Hello!"
print(len(a))

'''
output:
6
'''

#Traversal through a string with looping:
a = "Hello! i am fine"
index = 0
while index < len(a):
    letter = a[index]
    print(index, letter)
    index = index + 1
    
#output
'''
0 H
1 e
2 l
3 l
4 o
5 !
6  
7 i
8  
9 a
10 m
11  
12 f
13 i
14 n
15 e
'''


#Trupti code:

# Program to demonstrate basic data types
age = 20                  # int
height = 5.9              # float
name = "Trupti"           # str
is_student = True         # bool

print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Is Student:", is_student)

#output:
#Age: 20
#Height: 5.9
#Name: Trupti
#Is Student: True

#----------------
# Program using string functions
text = "Welcome to Python Programming"

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Starts with 'Welcome':", text.startswith("Welcome"))
print("Replace 'Python' with 'Java':", text.replace("Python", "Java"))

#output:
#Length: 30
#Uppercase: WELCOME TO PYTHON PROGRAMMING
#Lowercase: welcome to python programming
#Starts with 'Welcome': True
#Replace 'Python' with 'Java': Welcome to Java Programming


# Program to calculate average marks and assign grade
print("Student Grade Calculator")

total_marks = 0
subject_count = 5

for i in range(1, subject_count + 1):
    marks = float(input(f"Enter marks for Subject {i} (out of 100): "))
    total_marks += marks

average = total_marks / subject_count
print("\nAverage Marks:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

#output:
#Student Grade Calculator
#Enter marks for Subject 1 (out of 100): 85
#Enter marks for Subject 2 (out of 100): 90 
#Enter marks for Subject 3 (out of 100): 78
#Enter marks for Subject 4 (out of 100): 92
#Enter marks for Subject 5 (out of 100): 88
#Average Marks: 86.6
#Grade: A


# Basic ATM simulator
balance = 1000

while True:
    print("\n==== ATM Menu ====")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print("Your Balance is ₹", balance)

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful. New Balance is ₹", balance)
            else:
                print("Insufficient balance.")

        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit Successful. New Balance is ₹", balance)

        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1-4.")

    except ValueError:
        print("Invalid input! Please enter a number.")
#output:
#==== ATM Menu ====
#1. Check Balance
#2. Withdraw    
#3. Deposit
#4. Exit
#Enter your choice (1-4): 1
#Your Balance is ₹ 1000

# Count how many times each word appears (without using collections)
text = input("Enter a sentence: ").lower()

words = text.split()
seen_words = []

print("\nWord Frequency:")
for word in words:
    if word not in seen_words:
        count = 0
        for w in words:
            if w == word:
                count += 1
        print(f"{word}: {count}")
        seen_words.append(word)
  
#output:
#Enter a sentence: Hello world hello
#Word Frequency:
#hello: 2
#world: 1


# Simple password strength checker
password = input("Enter your password: ")

print("\nPassword Check:")
if len(password) < 8:
    print("- Too short (minimum 8 characters required)")
else:
    print("- Length OK")

if password.islower() or password.isupper():
    print("- Add a mix of uppercase and lowercase letters")
else:
    print("- Letter case OK")

if any(char.isdigit() for char in password):
    print("- Contains digits ✅")
else:
    print("- Add at least one number")

if any(char in "!@#$%^&*()_+" for char in password):
    print("- Contains special characters ✅")
else:
    print("- Add special characters like !, @, #")

print("\nPassword Strength Check Complete.")


#output:
#Enter your password: Pass123

#Password Check:
#- Too short (minimum 8 characters required)
#- Add a mix of uppercase and lowercase letters
#- Contains digits ✅
#- Add special characters like !, @, #
#Password Strength Check Complete.

