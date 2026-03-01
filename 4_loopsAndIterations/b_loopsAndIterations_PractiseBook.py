#Exercise 1: Write a while loop to print numbers from 0 to 10

print('Exercise 1')
l=0
while l<=10:
  l=l+1
  print(l-1)
  

'''output:
0
1
2
3
4
5
6
7
8
9
10
'''

#Exercise 2: Print the first number greater than 100 that is divisible by 17

#YOUR CODE HERE
ListOfNum=[24,35,45,100,120,150,17,34,85,102,138,119,136]
for num in ListOfNum:
 if num>=100 and num%17==0:
  print(num, 'Is the number greater than 100 and divided by 17')
  break

'''output:
102 Is the number greater than 100 and divided by 17
'''

#Exercise 3: Using for loop print out the characters of 'Portland'

#YOUR CODE HERE
name='Portland'
for countryName in name:
  print(countryName)
  
'''output:
P
o
r
t
l
a
n
d
'''

'''
Exercise 4: Do the following:

    .Use a lower bound of 1 and an upper bound of 10 with range to print 1-9
    .Use range with one bound only, the number 10, to print the first ten numbers
    .Use a step increment to count the even numbers through 10
'''
#YOUR CODE HERE

for num in range(1,10):
 print(num)
 
'''output:
1
2
3
4
5
6
7
8
9
'''
 
 #YOUR CODE HERE
for num in range(10):
  print(num)
 
'''output:
0
1
2
3
4
5
6
7
8
9
'''

#YOUR CODE HERE
for num in range(1,20,2):
 print(num)
 
 '''
1
3
5
7
9
11
13
15
17
19
'''

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
'''     
3
6
9
'''


start = 5
end = 25

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)
'''      
6
8
10
12
14
16
18
20
22
24
'''     

for i in range(1, 11):
    if i % 2 != 0:
        print(i)
'''      
1
3
5
7
9
'''      

#Exercise 5: print each letter on python in each line
#YOUR CODE HERE

word="Python"
for pythonWord in word:
  print(pythonWord *3 )
'''
PPP
yyy
ttt
hhh
ooo
nnn
'''

#print each letter of "Python" three times
word="Python"
for i in range(3):
  for pythonWord in word:
    print(pythonWord)
'''
P
y
t
h
o
n
P
y
t
h
o
n
P
y
t
h
o
n
'''
'''
Exercise 6: Write a for loop for the following
    .print the squares of numbers from 1 to 10.
    .iterate over a list of names and print each name
    .calculate the sum of numbers in a given list.
'''
#YOUR CODE HERE
for i in range(1,10):
 print(i**2)

'''
1
4
9
16
25
36
49
64
81
'''

##YOUR CODE HERE
nameList=['ram','lak','ramu','laxmi','radha']
for eachName in nameList:
 print(eachName)
 
'''
ram
lak
ramu
laxmi
radha
'''

#print the numbers in a given list.

num=[2,3,5,7,8,100,344]
for sumNum in num:
  print(sumNum)

'''
2
3
5
7
8
100
344
'''

#YOUR CODE HERE
#calculate the sum of numbers in a given list.

num=[2,3,5,7,8,100,344]
TotalSum=0
for sumNum in num:
  TotalSum=TotalSum + sumNum
  print(TotalSum)

'''
2
5
10
17
25
125
469
'''
 
 
#Exercise 7: Write a nested loop to generate multiplication tables for numbers from 1 to 10

#YOUR CODE HERE
for i in range(1,10):
  for j in range(1,10):
    print(i * j, end= '\t')
  print()

'''
1	2	3	4	5	6	7	8	9	
2	4	6	8	10	12	14	16	18	
3	6	9	12	15	18	21	24	27	
4	8	12	16	20	24	28	32	36	
5	10	15	20	25	30	35	40	45	
6	12	18	24	30	36	42	48	54	
7	14	21	28	35	42	49	56	63	
8	16	24	32	40	48	56	64	72	
9	18	27	36	45	54	63	72	81	
'''

for i in range(1,10):
  for j in range(1,10):
    print(i * j, end= '\n')
  print()
  
  '''
1
2
3
4
5
6
7
8
9

2
4
6
8
10
12
14
16
18

3
6
9
12
15
18
21
24
27

4
8
12
16
20
24
28
32
36

5
10
15
20
25
30
35
40
45

6
12
18
24
30
36
42
48
54

7
14
21
28
35
42
49
56
63

8
16
24
32
40
48
56
64
72

9
18
27
36
45
54
63
72
81
  '''
  
  
  