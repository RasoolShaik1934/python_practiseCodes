'''
[String Comparison]:
    .Strings can be compared using comparison operators
    .The comparison is based on the lexicographical order of the characters in the strings
    .The comparison is case-sensitive, meaning uppercase letters are considered less than lowercase letters
    .The comparison is done character by character until a difference is found or one string ends
    .If one string is a prefix of another, the shorter string is considered less than the longer one
    .If both strings are equal, they are considered equal
    .The comparison operators include ==, !=, <, <=, >, and >=
'''

# example 1:
word = 'banana'
if word == 'banana':
  print('All right, bananas.')
  
  
 # example 2:
word = 'apple'
if word < 'banana':
  print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
  print('Your word,' + word + ', comes after banana.')
else:
  print('All right, bananas.')
  

# Copilot Examples:
#p1
# Example: Comparing two strings for equality
string1 = "Hello"
string2 = "Hello"
are_equal = string1 == string2  # Returns True if both strings are equal
print(are_equal)  # Output: True

#p2
# Example: Comparing two strings for inequality
string3 = "Hello"
string4 = "World"
are_not_equal = string3 != string4  # Returns True if both strings are not equal
print(are_not_equal)  # Output: True

#p3
# Example: Comparing two strings lexicographically
string5 = "Apple"
string6 = "Banana"
is_less_than = string5 < string6  # Returns True if string5 is lexicographically less than string6
print(is_less_than)  # Output: True

#p4
# Example: Comparing two strings lexicographically with case sensitivity
string7 = "apple"
string8 = "Apple"
is_greater_than = string7 > string8  # Returns True if string7 is lexicographically greater than string8
print(is_greater_than)  # Output: True

#p5
# Example: Comparing two strings with different lengths
string9 = "Hello"
string10 = "Hello, World"
is_less_than_or_equal = string9 <= string10  # Returns True if string9 is less than or equal to string10
print(is_less_than_or_equal)  # Output: True

#p6
# Example: Comparing two strings with different lengths and characters
string11 = "Hello, World"
string12 = "Hello, World!"
is_greater_than_or_equal = string11 >= string12  # Returns True if string11 is greater than or equal to string12
print(is_greater_than_or_equal)  # Output: False
