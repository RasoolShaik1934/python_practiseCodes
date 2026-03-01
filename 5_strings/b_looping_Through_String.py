'''
[Looping through strings]:
 .Strings can be looped through using a while loop or a for loop.
 
'''

#p1
 # While loop:
  #.Using a while statement, an iteration variable, and the len() function, 
  #.We can construct a loop to look at each of the letters in a string individually
 
a = "Hello!"         
index = 0
while index < len(a):
  print(index, a[index])
  index = index + 1
  
'''
0 H
1 e
2 l
3 l
4 o
5 !
'''
  
#p2
  #For loop:
  #.Using a for loop, we can iterate through each character in the string directly without using an index variable.

#approach 1
b = "Good Morning"
for greet in b:
  print(greet)


# approach 2
for greet in "Greetings!":
  print(greet)
  

#p3 
  #Looping through a string with enumerate():
  #.Using the enumerate() function, we can loop through a string and get both the index and the character at that index in a single loop.
c = "Python"
for index, char in enumerate(c):
  print(index, char)
  
  
#p4
 #Looping and Counting:
 #.Counts the number of times the letter/character appears in a string
 
d = "Hello, World!"
count = 0
for char in d:
  if char == 'o':
    count += 1
print("The letter 'o' appears", count, "times in the string.")

#output: The letter 'o' appears 2 times in the string.


#p5
 #Looping through a string and counting occurrences of a specific character:
 #.Counts the number of times the letter 'l' appears in the string "Hello world!"
 
a = "Hello world!"
count = 0
for singleLetter in a:
  if singleLetter == 'l':
    count = count + 1
    print(count)
    


  

  