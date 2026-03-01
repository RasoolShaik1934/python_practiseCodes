'''
[String Striding]:
  .The stride, which refers to how many characters to move forward after the first character is retrieved from the string
  .The value of stride is set to 1 by default
  .To specify a stride, use the colon operator with a third value after the second colon
  .The syntax for striding is: string[start:end:stride]

Copilot:
  .If the stride is negative, the string is traversed in reverse order
  .If the stride is positive, the string is traversed in forward order
  .If the start index is omitted, it defaults to the beginning of the string
  .If the end index is omitted, it defaults to the end of the string
  .If the stride is omitted, it defaults to 1
  .If the start index is greater than the end index, an empty string is returned
  .If the start index is less than the end index, the string is traversed in forward order
  .If the start index is greater than the length of the string, an empty string is returned
  .If the end index is greater than the length of the string, the end index is set to the length of the string
  .If the stride is negative, the start index must be greater than the end index
  .If the stride is positive, the start index must be less than the end index
  .If the stride is zero, a ValueError      
'''

#p1
 #Striding a string:
 #.Using the colon operator, we can select characters from a string with a specified step (stride)
 
f = 'Hello World'
print(f[1::2])   # Output: el ol

'''
f[start:stop:step]
  start = 1 → Start from index 1 ('e')
   stop = (empty) → Go till the end of the string
   step = 2 → Take every second character

   Index:  0 1 2 3 4 5 6 7 8 9 10
  String:  H e l l o   W o r l d
     Start from index 1 (which is 'e') and take every second character:
     'e', 'l', ' ', 'o', 'l'
'''

f = 'Hello World'
print(f[::2])  # Output: Hlo ol

f = 'Hello World'
print(f[::-1]) # Output: dlroW olleH

f = 'Hello World'
print(f[0::1])  # Output: Hello World
print(f[0::2])  # Output: Hlo ol
print(f[0::3])  # Output: Hl r      