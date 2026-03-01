
'''
Exercise 01:
Reverse the order of the given list.
'''
a = [100, 200, 300, 400, 500]
a.reverse()
print(a)


'''
Exercise 02:
Concatenate two lists using .extend().
'''
list1 = ["Hello ", "Students "]
list2 = ("Dear", "Sir")

list1.extend(list2)
print(list1)


'''Exercise 03: 
For given list, perform the following:

    Print the last element from the list.
    Print index of element 4.
'''
numbers = [1, 2, 3, 4, 5, 6, 7]

list4 = [1, 2, 3, 4, 5, 6, 7]
list4[-1]

list5 = [1, 2, 3, 4, 5, 6, 7]
list5.index(4)


'''
Exercise 04:
Print the sublist from the given list.
Expected output : [9,8,7]
'''

list5 = [1, 2, 3, [9, 8, 7]]
list5[3]

'''
Exercise 05:
For given list, find the following:
    Check the type of the list elements.
    Check whether the element 'name' is present in the list.
    Find the length of the list.
'''
list6= [1,'name',0.7,"this is a sentence"]
for lists in list6:
  print(type(lists))
  
  
list6= [1,'name',0.7,"this is a sentence"]
'name' in list6


list6= [1,'name',0.7,"this is a sentence"]
print(len(list6))


'''
Exercise 6:
For the given list, find the following:
    Find the count of the apples.
    Insert the 'Watermelon' at the last position.
'''

basket=['apple','apple','orange','mango','grape','orange','apple']
# YOUR CODE HERE
count=0
for totalBasket in basket:
  if totalBasket=='apple':
    count=count+1
print(count)


basket=['apple','apple','orange','mango','grape','orange','apple']
# YOUR CODE HERE
print(basket.count('apple'))
# basket.append('Watermelon')
basket


basket=['apple','apple','orange','mango','grape','orange','apple']
basket.insert(6, 'Watermelon')
print(basket)

'''
Exercise 07:
Print the squares of the numbers in the given list.

Expected output :
36
49
64
'''
list1 = [6, 7, 8]

squares = map(lambda n: n ** 2, list1)
print(list(squares))


'''Exercise 08:
For the given list, print only the positive elements.
'''

## YOUR CODE HERE
list2 = [-1, 2, -3, 4, -5, 6, -7]

positives = list(filter(lambda n: n >0, list2))
print(positives)


list3 = [-1, 2, -3, 4, -5, 6, -7]

negatives = list(filter(lambda n: n<0, list3))
print(negatives)



'''Exercise 09:
For the given list, print numbers which are multiples of 5.
'''
## YOUR CODE HERE
list4 = [10, 12, 20, 22, 30, 32, 40]

newList = list(filter(lambda n:n%5 ==0, list4))
print(newList)


'''Exercise 10:

For the given list, print if the element is an one digit or a two-digit number.
'''

## YOUR CODE HERE
list4 = [5, 15, 20]

for digit in list4:
  if len(str(digit))>1:
    print(digit,"is a two digit number")
  else:
    print(digit,"is a one digit number")
    
'''
Exercise 11:
For the given String, find the following:
    Split the string into a list of words and print them.
    Print the length of the list.
'''

## YOUR CODE HERE
string1 = "The quick brown fox jumps over the lazy dog"
listed=list(string1.split())
print(listed)

'''Exercise 12:

For the given List, find the following:

    list items from 2nd to 3rd.
    list items from beginning to 3rd.
    list items from 4th to the end of the list.
'''

#YOUR CODE HERE
list5 = [1, 2, 3, 4, 5, 6, 7]
list5[1:3]
list5[0:3]
list5[3:]

'''Exercise 13:
For the given list, print the numbers which are greater than or equal to 10.
'''

# YOUR CODE HERE
list6 = [0, 1, 2, 3, 10, 11, 12, 13]

greaterValues = list(filter(lambda n: n>=10, list6))
print(greaterValues)


list6 = [0, 1, 2, 3, 10, 11, 12, 13]
for newG in list6:
  if newG>=10:
    print(newG)

