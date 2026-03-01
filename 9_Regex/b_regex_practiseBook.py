import re

'''Exercise 1:
Extract all the email addresses from a string.
'''
text = "My email addresses are john.doe@example.com and jane.doe@example.net"

y = re.findall('\S+@\S+',text)
print(y)
#output:
['john.doe@example.com', 'jane.doe@example.net']


'''Exercise 2:
For given text, replace all occurrences of the word "apple" with "banana":
'''

text = "There are 100 apples and 50 bananas"
y = text.replace('apples','bananas')
print(y)

#output:
#There are 100 bananas and 50 bananas

'''Exercise 3:
Extract numbers from the given text:
'''

text = "There are 10 Jacks and 15 Queens"

y = re.findall('[0-9]+',text)
print(y)

#output:
#['10', '15']

'''Exercise 4:
Using a regular expression, extract email addresses from given string:
'''

email_string = "My email address is example@gmail.com and another one is test@yahoo.com"

y=re.findall('\S+@\S+',email_string)
print(y)

#output
# ['example@gmail.com', 'test@yahoo.com']


'''Exercise 5:
Using a regular expression, find the index of a string, 'world' from the given text.
'''
text = "Hello, World!"
word = text.find('World')
print(word)

#output
#7

'''Exercise 6:
Search for a specific pattern in a string.
'''

text = "My email address is example@example.com."

# search for an email address
match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(match)

#check if a match was found
if match:
  print("Match found:", match.group())
else:
  print("No match found.")
  
#output:
'''<re.Match object; span=(20, 39), match='example@example.com'>
Match found: example@example.com
'''