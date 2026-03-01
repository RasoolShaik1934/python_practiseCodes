'''Loops and Iterations

Agenda(TOPICS TO BE COVERED)
    Loops and Iterations
    Break and continue statements
    Indefinite Loops
    Definite loops
    Making smart loops
'''
#program:
n = 5
while n>0:
  print('n is positive and value is:', n)
  n=n-1
print('n is negative')
print(n)


#p1
 #program Infinite loop:
n=0
while n>0:
  print('Wash')
  print('Rinse')
print('Dry off')


#p2
  #Breaking out of loop:
  #.Break statement ends the current loop and jumps to the statement immediately following the loop
  #.Break statement is like a loop test that can happen anywhere in the body of the loop

while True:
  line = input('--->')
  if line == 'done':
    break
  print(line)
print('Done!')


'''Below code:
The code uses a while True loop to repeatedly prompt the user for input.
If the input starts with a '#', the loop skips to the next iteration using continue.
If the input is 'done', the loop breaks and the program exits the loop. Otherwise, the input is printed.
The loop continues until the user enters 'done'.
After the loop, the program prints 'Done!' to indicate completion.
'''   

#p3
 #Finishing an iteration with continue:
while True:
  line = input('type name with #')
  if line[0] == '#' :
    continue
  if line == 'done' :
    break
  print(line)
print('Done!')    
       


#p4
  #Indefinite loops:
  #.while loops are called "indefinite loops" because they keep going until a logical condition v=becomes false:
  #example:program

while True:
    line = input('--->')
    if line == 'done':
      break
    print(line)
print('Done!')



#p5
 #Definite loops:
 #.These loops are definite loops because they execute an exact number of times and comes out of the loop


  #example1: program
  #Definite loop with strings:
list_of_friends = ['Joseph','Glenn','Sally']
for friend in list_of_friends:
  print('Happy New Year:',friend)
print('Done!')


 #example2: program
 #Definite loop with integer:
list_values=[1,2,3,4,5]
for value in list_values:
  print(value)
print('Done!')


#example3: program
'''
The code finds the largest number in a given list. 
It initializes the largest number as -1. 
It iterates over each number in the list. 
If a number is greater than the current largest number, it updates the largest number. 
It prints each number and the current largest number as it iterates. Finally, it prints the largest number found.
'''
#print all number:
listOfNumbers=[2,3,41,12,9,74,15]
for largestNumber in listOfNumbers:
  if largestNumber>3:
    print('largestNumber is:',largestNumber)
print('Done')


listOfNumbers=[3,2,-1,-0,-9]
for largestNumber in listOfNumbers:
  if largestNumber>2:
    print('largestNumber is:',largestNumber)
print('Done')


#p6
 #Print the largest numbers in the list:
largest_so_far=-1
listOfLargesNumbers =[9,12,41,85,72,75]
for i in listOfLargesNumbers:
  if i>largest_so_far:
    largest_so_far=i
    print('largestNumber so far is:',largest_so_far)
print('Done')


#p7
 #Print the counting in a loop:
'''
The code initializes a variable zork with a value of 0. It prints the initial value of zork as "Before 0".
The code then enters a for loop that iterates over each number in the list [9, 41, 12, 3, 74, 15].
In each iteration, it increments the zork variable by 1.
It then prints the updated value of zork along with the current number from the list.
After all the iterations are completed, it prints the final value of zork as "After" followed by the total number of iterations.
'''
zork = 0
listOfAddingNumbers =[9,12,41,85,72,75]
for i in listOfAddingNumbers:
    zork = zork + 1
    print(zork, i)
print('Done')


#p8
 #Summing in a loop
zork1=0
listNumbers=[3,4,6,65,67,68]
for i in listNumbers:
  zork1 = zork1+i
  print(i,zork1)
print('Done!')


#p9
 #Finding the average in a loop
count = 0
sum = 0
print('Before',count,sum)
for value in [9,41,12,3,74,15]:
  count = count + 1
  sum = sum + value
print('After',count,sum,sum/count)


#p10
 #Filtering in a loop
print('Before')
for value in [9,41,12,3,74,15]:
  if value>20:
    print('Large number',value)
print('After')

#p11
 #Search using a boolean variable
found = False
print('Before',found)
for value in [9,41,12,3,74,15]:
  if value == 3:
    found = True
  print(found,value)
print('After', found)
                    #.In the below result as we observe after 3 is found as true for the next iterations also we are getting true only
                    #.Reason is as we are not updating the found variable as true it is still printing true only 
                    #.In the next p12 program we will resolve
 
 #p11.1  
 #How to find the smallest value    
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num > largest_so_far :
      largest_so_far = the_num
   print(largest_so_far, the_num)

print('After', largest_so_far)  
                    
#p12
 #How to find the smallest value

smallest_so_far = -1
print('Before',smallest_so_far)
for value in [9,41,12,3,74,15]:
  if value > smallest_so_far:
    smallest_so_far = value
print('After',smallest_so_far,value)

#p13
# Finding the smallest value
smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
  if smallest is None:
    smallest = value
  elif value < smallest:
    smallest = value
  print(smallest,value)
print('After', smallest)



'''belongs to below:
[The 'is' and 'is not' operators:]
-.Is operator can be used logical expression 
-.Is and is not operators are used when comparing object identity ie. 
-.whether two variables points to same memory address

'''
#p13
a = [5,8]
b = [5,8]
c=a
if a is not b:
  print ('a and b are not same')
else:
  print('a and b are same')
if a is c:
  print('a and c are same')
else:
  print('a and c are not same')
  
  '''
  
SUMMARY::
->WHILE LOOPS (INDEFINITE)
->INFINITE LOOPS
->USING BREAK
->USING CONTINUE
->FOR LOOPS (DEFINITE)
->ITERATION VARIABLES
->LARGEST OR SMALLEST
->NONE CONSTANTS AND VARIABLES
'''



# ------------------------------>>>>>>>>>>>>>
# Trupti Colabs:

country = 'japan'

for i in country:
    print(i, end='')
    
#output:
#japan

'''prints each character on a new line.
But here:
print(i, end='')
end='' means do not move to a new line after printing.
It removes the default newline (\n).
'''


# count the occurance of 'a','b'and 'c' in country

country = 'japan'
count = 0
for i in country:
    if i in ['a','b','c']:
        count += 1
print(count)
#output: 2


print(range(10))
#output: range(0, 10)

for i in range(10):    # range(0,10,1)
    print(i)
#output:
#0
#1
#2
#3
#4
#5
#6
#7  
#8
#9

#10 is not included in the output because range generates numbers up to, but not including, the specified stop value (10 in this case).


for i in range(1,11):
    print(i)
    
#output:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

for i in range(10,101,10):
    print(i)
#output:
#10
#20
#30
#40
#50
#60
#70
#80
#90
#100


# find largest number from the list
mylist = [65,32,10,89,736,20,4]
big = mylist[0]     # big = 65
for i in mylist:
    if big<i:
        big = i
print(f"Largest number: {big}")
#output: Largest number: 736





 


