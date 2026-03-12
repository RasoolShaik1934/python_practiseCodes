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

#Tripti code:
# Accept a number till the user wants
# FInd if the number is palindrome or not  - NITIN, 1001, 12321, 56765,...

while True:
    num = input('Number (enter 0 to STOP): ')
    if int(num) == 0:
        break
    elif num == num[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

print('End of code')

#output:
#Number (enter 0 to STOP): 1001
#It's a palindrome        

#---------------------->>

word = 'india'
word*3

#output: 'indiaindiaindia'

#---------------------->>
word = 'ID453'
word.isalnum()
#output: True


word = '453'
word.isalnum()
#output: True

word = '%^$#@'
word.isalnum()
#output: False

#---------------------->>
#ExtraCode:
# list of text tokens (common in NLP)

#         0            1        2            3     4      positive index number
tokens = ['natural','language','processing','is','fun']
#         -5          -4         -3          -2   -1      negative index number


tokens[3:1:-1]    # step is -1, reverse| start should b a bigger num & stop will b smaller

#output: ['is', 'processing']

#----------------------->>
sample_features = [[1007, 'Sales', 'f', 'Mumbai', True],
                       	[1008, 'Finance', 'm', 'Pune', False],
                       	[1009, 'IT', 'm', 'Pune', False]]

sample_features

#output: [[1007, 'Sales', 'f', 'Mumbai', True], [1008, 'Finance', 'm', 'Pune', False], [1009, 'IT', 'm', 'Pune', False]]

sample_features[0]
#output: [1007, 'Sales', 'f', 'Mumbai', True]

sample_features[0] [1]
#output: 'Sales'

sample_features[0] [1]
#output: 'Sales'

sample_features[-1]
#output: [1009, 'IT', 'm', 'Pune', False]

sample_features[-1][-1]
#output: False

#----------------------->>

data = [{"name": "Deepak", "age": 30, "exp": 10.5},
        {"name": "Gaurav", "age": 40, "exp": 8.5},
        {"name": "Gajendra", "age": 50, "exp": 0.5}]

data

data[0]
#output: {'name': 'Deepak', 'age': 30, 'exp': 10.5}

data = [{"name": "Deepak", "age": 30, "exp": 10.5},
        {"name": "Gaurav", "age": 40, "exp": 8.5},
        {"name": "Gajendra", "age": 50, "exp": 0.5}]

data[0]['name']
#output: 'Deepak'

d1.keys()
#output: dict_keys(['name', 'age', 'exp'])

#----------------------->>

sample_features = [[1007, 'Sales', 'f', 'Mumbai', True],
 [1008, 'Finance', 'm', 'Pune', False],
 [1009, 'IT', 'm', 'Pune', False]]

sample_features[0]
#output: [1007, 'Sales', 'f', 'Mumbai', True]

sample_features[0][1]
#output: 'Sales'

sample_features[0][1] = 'Marketing'
sample_features[0]
#output: [1007, 'Marketing', 'f', 'Mumbai', True]


#------------------------------>>

tokens = ['natural','language','processing','is','fun']

tokens
#output: ['natural', 'language', 'processing', 'is', 'fun']

tokens.append('awesome')
tokens
#output: ['natural', 'language', 'processing', 'is', 'fun', 'awesome']

tokens.insert(4, 'too much')
tokens
#output: ['natural', 'language', 'processing', 'is', 'too much', 'fun', 'awesome']

#------------------------------>>

sample_feature  = [36, 90,2]  # age, income_k, children

sample_feature.extend([1])  # adding a new feature - has_car
sample_feature
#output: [36, 90, 2, 1]

sample_feature.pop(-1)
sample_feature
#output: [36, 90, 2]

sample_feature.remove(90)
sample_feature
#output: [36, 2]



#------------------------------>>

sample_feature1 = [36, 90, 2, 1, 0, 1001]

try:
  sample_feature1.remove(1001)
except Exception as err:
  print(err)

#output: 1001 not found in list


#------------------------------>>

# creating list having sequence of numbers

sample_data = list(range(10))    # 0,10,1
sample_data
#output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


sample_data = list(range(1,11))
sample_data
#output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sample_data = list(range(10,0,-1))
sample_data
#output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#----------------------------->>

sample_ages = [43,89,13,54,13,43,54,22,30]

sample_ages

sorted(sample_ages)  # sorted() is a built-in function that returns a new sorted list from the items in an iterable.
#output: [13, 13, 22, 30, 43, 43, 54, 54, 89]  

#----------------------------->>

# get words longer than 3 char

long_tokens = [t  for t in tokens if len(t)>3]
long_tokens

#output: ['natural', 'language', 'processing', 'awesome']

#------------------------------>>

long_tokens = [t  for t in tokens if len(t)>3]

#is exactly equal to

long_tokens = []
for t in tokens:
  if len(t)>3:
    long_tokens.append(t)
    print(t)


#output: 
#natural
#language
#processing
#awesome

#------------------------------>>

tokens1 = ['natural', 'la   ', 'processing', 'is', 'too much', 'fun', '& amazing']

labeled_tokens = [ "Long"  if len(t)>3   else  "Short"  for t in tokens1]

labeled_tokens
#output: ['Long', 'Short', 'Long', 'Short', 'Long', 'Short', 'Short']


#------------------------------>>
data = [34.9, None, 8.2, 12.0, None, 9.8]

non_missing = [x  for x in data if x is not None]

non_missing
#output: [34.9, 8.2, 12.0, 9.8]

#------------------------------->>
average = sum(non_missing)/ len(non_missing)
average

#output: 16.2