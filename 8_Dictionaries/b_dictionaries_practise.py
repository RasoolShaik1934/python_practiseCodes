'''Exercise 1:
From The dictionary created below, do the following:
    Return a list of all the keys, using list() or .keys().
    Return the values of the dictionary using .values().
    '''
    
dict1 = {"Delhi" : "New Delhi", "Uttar Pradesh" : "Lucknow","Madhya Pradesh" : "Bhopal","Karnataka" : "Bengaluru","Assam" : "Dispur","Gujarat" : "Gandhinagar"}

# YOUR CODE HERE
dict1.keys()
#outPut
#dict_keys(['Delhi', 'Uttar Pradesh', 'Madhya Pradesh', 'Karnataka', 'Assam', 'Gujarat'])


dict_list=list(dict1.keys())
print(dict_list)
#output
#['Delhi', 'Uttar Pradesh', 'Madhya Pradesh', 'Karnataka', 'Assam', 'Gujarat']

# YOUR CODE HERE
dict1.values()
#dict_values(['New Delhi', 'Lucknow', 'Bhopal', 'Bengaluru', 'Dispur', 'Gandhinagar'])


'''Exercise 2:
From the dictionary created in Exercise 1-
    Display the capital of Karnataka by retrieving the corresponding value for the key.
'''

dict1 = {"Delhi" : "New Delhi", "Uttar Pradesh" : "Lucknow","Madhya Pradesh" : "Bhopal","Karnataka" : "Bengaluru","Assam" : "Dispur","Gujarat" : "Gandhinagar"}
# YOUR CODE HERE
print(dict1["Karnataka"])
#output: Bengaluru


'''Exercise 3:
Add (and print) a new element in the dictionary.
'''
# YOUR CODE HERE
dict1["Delhi"]="OngoleRavipriyaMall"
print(dict1["Delhi"])
#output:OngoleRavipriyaMall


'''Exercise 4:
    Return the length of the dictionary using len().
'''
# YOUR CODE HERE
len(dict1)
#output: 6

'''
Exercise 5:
    Remove a key value pair from the dictionary.
    Add the same key value pair again in the dictionary.
    Display all the key-value pairs using items().
'''
dict1 = {"Delhi" : "New Delhi", "Uttar Pradesh" : "Lucknow","Madhya Pradesh" : "Bhopal","Karnataka" : "Bengaluru","Assam" : "Dispur","Gujarat" : "Gandhinagar"}

print(dict1)
dict1.popitem()
dict1["Telangana"] = "Hyderabad"


dict1.items()
#output
dict_items([('Delhi', 'New Delhi'), ('Uttar Pradesh', 'Lucknow'), ('Madhya Pradesh', 'Bhopal'), ('Karnataka', 'Bengaluru'), ('Assam', 'Dispur')])


del dict1["Assam"]
dict1.items()
#output:
dict_items([('Delhi', 'New Delhi'), ('Uttar Pradesh', 'Lucknow'), ('Telangana', 'Hyderabad')])


'''Exercise 6:
Iterate over the keys of the dictionary using for and .keys() and print all the state capitals
'''
for key in dict1.keys():
    print(dict1[key])
    
#output
'''
New Delhi
Lucknow
Bhopal
Bengaluru
Dispur
Gandhinagar
'''


'''Exercise 7:
    Initialize an empty dictionary ‘sen_map’.
    Make the sentences all lower case.
    Iterate over each word in the sentences.
    Check if a word exists in the sen_map.
    If not then add the word with a value of 1.
    Otherwise, update the value of that word by 1.
'''
sents = "TalentSprint is a digital platform designed to transform the lives of professionals in the new economy. Its blended bootcamps offer deeptech skills."

sen_map = {}  
sents = sents.lower() 
for i in sents.split(): 
    if i not in sen_map:   
        sen_map[i] = 1  
    sen_map[i] += 1  
sen_map

#outPut:
'''
{'talentsprint': 2,
 'is': 2,
 'a': 2,
 'digital': 2,
 'platform': 2,
 'designed': 2,
 'to': 2,
 'transform': 2,
 'the': 3,
 'lives': 2,
 'of': 2,
 'professionals': 2,
 'in': 2,
 'new': 2,
 'economy.': 2,
 'its': 2,
 'blended': 2,
 'bootcamps': 2,
 'offer': 2,
 'deeptech': 2,
 'skills.': 2}
 '''
 
 
'''Exercies 8:
    Initialize an empty dictionary ‘counts’.
    Define the following list, names = ['Jack', 'John', 'Jill', 'John'].
    Print the frequency count of elements in a list using a dictionary.
    Using get method print the value of john.
    Print a list of tuples containing the key-value pairs in ‘counts’.
 '''
counts = dict()
names = ['Jack', 'John', 'Jill', 'John']
for name in names :
    if name not in counts: 
       counts[name] = 1
    else :
       counts[name] = counts[name] + 1
print(counts)
#output:
#{'Jack': 1, 'John': 2, 'Jill': 1}



print(counts.get('John')) # The Python dictionary .get() method provides a convenient way of getting the value of a key from a dictionary
#output
#2

list(counts.items())
#output:
 #[('Jack', 1), ('John', 2), ('Jill', 1)]