'''
The [inOperators]:
The word 'in' is a Boolean operator that takes two strings and returns True if the first appears as a substring in the second:
'''

#p1
# Example: The following function prints all the letters from word1 that also appears in word2

'a' in 'banana'  # Returns True if 'a' is found in 'banana'
print('a' in 'banana')  # Output: True


#p2
'seed' in 'banana'  # Returns False if 'seed' is not found in 'banana'
print('seed' in 'banana')  # Output: False



#p3
def in_both_the_words(word1,word2):
  for letter in word1:
    if letter in word2:
        print(letter)
in_both_the_words('apples','oranges')




# Copilot Examples:
# Example: Checking if a substring is present in a string
string = "Hello, World!"
substring = "World"
is_present = substring in string  # Returns True if "World" is found in "Hello, World!"
print(is_present)  # Output: True


# Example: Checking if a character is present in a string
char = "H"
is_char_present = char in string  # Returns True if "H" is found in "Hello, World!"
print(is_char_present)  # Output: True 
 
 
# Example: Checking if a substring is not present in a string
not_present_substring = "Python"
is_not_present = not_present_substring in string  # Returns False if "Python" is not found in "Hello, World!"
print(is_not_present)  # Output: False


# Example: Using 'in' with a list of strings
words = ["Hello", "World", "!"]
is_word_present = "World" in words  # Returns True if "World" is found in the list of words
print(is_word_present)  # Output: True


# Example: Using 'in' with a string and a list of characters
chars = ['H', 'e', 'l', 'l', 'o']
is_char_in_list = 'H' in chars  # Returns True if 'H' is found in the list of characters
print(is_char_in_list)  # Output: True


# Example: Using 'in' with a string and a tuple of characters
chars_tuple = ('H', 'e', 'l', 'l', 'o')
is_char_in_tuple = 'H' in chars_tuple  # Returns True if 'H' is found in the tuple of characters
print(is_char_in_tuple)  # Output: True


# Example: Using 'in' with a string and a set of characters
chars_set = {'H', 'e', 'l', 'l', 'o'}
is_char_in_set = 'H' in chars_set  # Returns True if 'H' is found in the set of characters
print(is_char_in_set)  # Output: True


# Example: Using 'in' with a string and a dictionary (checking keys)
dict_example = {'H': 1, 'e': 2, 'l': 3, 'o': 4}
is_char_in_dict_keys = 'H' in dict_example  # Returns True if 'H' is found in the keys of the dictionary
print(is_char_in_dict_keys)  # Output: True


# Example: Using 'in' with a string and a dictionary (checking values)
dict_values_example = {'H': 1, 'e': 2, 'l': 3, 'o': 4}
is_value_in_dict = 1 in dict_values_example.values()  # Returns True if 1 is found in the values of the dictionary
print(is_value_in_dict)  # Output: True


# Example: Using 'in' with a string and a range of numbers
range_example = range(10)  # A range of numbers from 0 to 9
is_in_range = 5 in range_example  # Returns True if 5 is found in the range
print(is_in_range)  # Output: True


# Example: Using 'in' with a string and a string of characters
char_string = "Hello"
is_char_in_string = 'H' in char_string  # Returns True if 'H' is found in "Hello"
print(is_char_in_string)  # Output: True


# Example: Using 'in' with a string and a string of characters (case-sensitive)
case_sensitive_string = "Hello"
is_case_sensitive = 'h' in case_sensitive_string  # Returns False if 'h' is not found in "Hello"
print(is_case_sensitive)  # Output: False


# Example: Using 'in' with a string and a string of characters (case-insensitive)
case_insensitive_string = "Hello"
is_case_insensitive = 'h'.lower() in case_insensitive_string.lower()  # Returns True if 'h' is found in "Hello" (case-insensitive)
print(is_case_insensitive)  # Output: True


# Example: Using 'in' with a string and a string of characters (checking for substrings)
substring_string = "Hello, World!"
is_substring = "World" in substring_string  # Returns True if "World" is found in "Hello, World!"
print(is_substring)  # Output: True


# Example: Using 'in' with a string and a string of characters (checking for substrings with spaces)
substring_with_space = "Hello, World!"
is_substring_with_space = "Hello, " in substring_with_space  # Returns True if "Hello, " is found in "Hello, World!"
print(is_substring_with_space)  # Output: True


# Example: Using 'in' with a string and a string of characters (checking for substrings with punctuation)
substring_with_punctuation = "Hello, World!"
is_substring_with_punctuation = "World!" in substring_with_punctuation  # Returns True if "World!" is found in "Hello, World!"
print(is_substring_with_punctuation)
# Output: True


# Example: Using 'in' with a string and a string of characters (checking for substrings with special characters)
substring_with_special_chars = "Hello, World!"
is_substring_with_special_chars = "Hello, W@rld!" in substring_with_special_chars  # Returns False if "Hello, W@rld!" is not found in "Hello, World!"
print(is_substring_with_special_chars)  # Output: False


# Example: Using 'in' with a string and a string of characters (checking for substrings with numbers)
substring_with_numbers = "Hello, World 123!"
is_substring_with_numbers = "World 123" in substring_with_numbers  # Returns True if "World 123" is found in "Hello, World 123!"
print(is_substring_with_numbers)  # Output: True


# Example: Using 'in' with a string and a string of characters (checking for substrings with mixed content)
mixed_content_string = "Hello, World 123!"
is_mixed_content_substring = "Hello, World" in mixed_content_string  # Returns True if "Hello, World" is found in "Hello, World 123!"
print(is_mixed_content_substring)  # Output: True


# Example: Using 'in' with a string and a string of characters (checking for substrings with emojis)
emoji_string = "Hello, World! 😊"