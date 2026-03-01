'''
[Update String]:
   .Strings are immutable,
   .Which means that the existing string cannot be changed
   .Can update an existing string by (re)assigning a variable to another string
   .The new value can be related to its previous value or to a completely different string
   .Reassigning a variable to a new string creates a new string object in memory       
'''
#example of string immutability
f = 'Hello World!'
f[0] = 'J'
# This will raise a TypeError because strings are immutable
  

#p1
#We can replace the string but cannot change it in place
# Example: Changing the first character of a string to a different character
f = 'Hello, World'
newF = 'J' + f[1:]
print(newF)

b = "Hello World"
b = "beautiful" + b[5:]
print(b)

#output: beautiful World


#p2
# Example: Changing the last character of a string to a different character
g = 'Hello, World!'
newG = g[:-1] + '!'
print(newG)  # Output: Hello, World


#p3
# Example: Changing a substring in a string
h = 'Hello, World'
newH = h.replace('World', 'Python')
print(newH)  # Output: Hello, Python    


#p4
# Example: Changing a character at a specific index in a string
i = 'Hello, World'
newI = i[:7] + 'P' + i[8:]  # Change the character at index 7 to 'P'
print(newI)  # Output: Hello, Porld   

  
#Copilot questions: 
#p5
# Example: Changing multiple characters in a string
j = 'Hello, World'
newJ = j[:7] + 'Py' + j[9:]  # Change the characters at index 7 and 8 to 'Py'
print(newJ)  # Output: Hello, Pyorld


#p6
# Example: Changing a character in a string using a loop
k = 'Hello, World'
newK = ''
for index, char in enumerate(k):
    if index == 7:  # Change the character at index 7
        newK += 'P'
    else:
        newK += char
print(newK)  # Output: Hello, Porld


#p7
# Example: Changing a character in a string using a list comprehension
l = 'Hello, World'
newL = ''.join(['P' if index == 7 else char for index, char in enumerate(l)])
print(newL)  # Output: Hello, Porld 


#p8
# Example: Changing a character in a string using the str.format() method
m = 'Hello, World'
newM = '{}{}'.format(m[:7], 'P' + m[8:])
print(newM)  # Output: Hello, Porld 


#p9
# Example: Changing a character in a string using f-strings (Python 3.6+)
n = 'Hello, World'
newN = f'{n[:7]}P{n[8:]}'
print(newN)  # Output: Hello, Porld 


#p10
# Example: Changing a character in a string using the str.join() method
o = 'Hello, World'
newO = ''.join(['P' if index == 7 else char for index, char in enumerate(o)])
print(newO)  # Output: Hello, Porld
