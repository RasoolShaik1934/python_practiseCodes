'''
[String Slicing]:
  .A segment of a string is called a slice
  .Selecting a slice is similar to selecting a character
  .Specify an index to get the character at that position in the string
  .Use the colon operator to specify a range of indices
'''

'''
 #Slicing a string:
 #.Using the colon operator, we can select a range of characters from a string
 Here's an explanation of each component:
string: The original string from which you want to extract substrings.

start: The index at which to start the substring extraction (inclusive). If not specified, it defaults to the beginning of the string.
end: The index at which to end the substring extraction (exclusive). If not specified, it defaults to the end of the string.
step: The step value or stride, indicating the interval between characters to be included in the substring. A positive stride moves forward in the string, while a negative stride moves backward. If not specified, it defaults to 1.
 '''

#str[start_index : end_index : increment]
s = "Hello, World!"
print(s[0:5])  # Output: Hello
print(s[7:12])  # Output: World


#p2
a = "Hello!"
b = a[1:4] # Output: ell
print(b)


#p3
b = "Hello!"
c = b[1:4:2]  # Output: el
              # Start at index 1, stop at index 4, and step by 2
print(c)


c = 'Hello World'
print(c[:3])  # Output: Hel

d = 'Hello World'
print(d[3:])  # Output: lo World

e = 'Hello World'
print(e[1:-1]) # Output: ello Worl

'''
The output of the program is Hello and can be explained as below -
Start index = 0, i.e. "H"
End index = 6 — 1 = 5 (End index always is one less than the mentioned index)
Increment = 1 (when not mentioned increment is 1 by default)
'''

f = "Hello World"
print(f[::2]) # Using indexing sequence
# Output: HloWrd (every second character from the string)



