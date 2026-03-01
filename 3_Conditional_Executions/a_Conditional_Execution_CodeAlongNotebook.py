'''
1.Comparison operators
2.One-way decisions
3.Indentation
4.Nested decisions
5.Two-way decisions if: and else:
6.MultiWay decisions using elif
7.try/except to compensate for errors

'''

'''
Conditional steps: These are the conditions in the program which checks at the time of running the program and gives the output if the condition is satisfied.
 '''
#p1
 #1.Conditional steps
x = 5
if x<10:
  print('Smaller')
if x>20:
  print('Bigger')
  print('Finish')
  
#p2
 #2.Comparison operators are <,<=,==,>=,>,!= (Boolean expression using compare operators evaluate to True/False or Yes/No)
 
x = 20
if x==5:
  print('Equals 5')
if x>4:
  print('Greater than 4')
if x>=5:
  print('Greater than or equals 5')
if x<6:
  print('Less than 6')
if x<=5:
  print('Less than or equal 5')
if x!=6:
  print('Not equal to 6')
  
'''
One-way-decisions here if statement is a conditional statement, it determines weather the block of code is performed or not.'''
#p3
  #3.One-way decisions
#
x = 5
print('Before 5')

if x==5:
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('After 5')
print('Before 6')

if x==6:
  print('Is 6')
  print('Is still 6')
  print('Third 6')
  
'''
Indentation The space at the start of code is known as indentation
'''
#p4
 #4.Indentation
 
 #.For Python indentation is important
#  x=1
#  if x>2:
#      print('Bigger than2')
#      print('Still bigger')
#  print('Done with 2')

for i in range(5):
  print(i)
  if i>2:
    print('Bigger than 2')
  print('Done with i',i)
print('All done')

'''
Nested decisions:
  .these are nested if statements i.e., more if conditions in a program i.e., if statement inside a if statement
  .these are useful when we need to make a series of decisions
'''
#p5
 #5.Nested decisions

x=101
if x>1:
  print('More than one')
if x<100:
  print('Less than 100')
print('All done')


#p6
#6.Two-way decisions if: and else: 

x=4
if x>2:
  print('Bigger')
else:
  print('Not Bigger')
print('All Done')


#p7
#7.MultiWay decisions using elif
x=3
if x<2:
  print('Small')
elif x<10:
  print('medium')
else:
  print('Large')
print('All done')

#p8
#8.MultiWay decisions without using elif
x=5
if x<2:
  print('Small')
elif x<10:
  print('Medium')
print("All Done")


'''
Try and except structures These can handle exception i.e., the errors that happens during the execution of the program

    TRY: if an execution is raised it jumps directly to the exception phase
    Exception: this is raised if only there occurs error in try block i.e.,
    if the code i try block works except block is skipped
    if the code in try shows error except block appears
'''

#p9
# 7.try/except to compensate for errors
astr = 'Hello Bob'
try:
  istr = int(astr)
except:
  istr = -1
print('First',istr)
#output: First -1


#p10
astr = '123'
try:
  istr=int(astr)
except:
  istr = -1
print('Second',istr)
#output: Second 123

#p11 try.except with input for number
rawstr= input('Enter a number: ')
try:
  ival = int(rawstr)
except:
  ival=-1
if ival>0:
  print('Nice work')
else:
  print('Not a number')
  #output: Enter a number: 45
#Nice work
  
  
#p11 try.except with input for name
rawstr= input('Enter a number: ')
rawstr= input('Enter any name: ')
try:
  ival = str(rawstr)
except:
  ival='boss'
if ival=='boss':
  print('Nice work')
else:
  print('Not a name')
  #output: Enter a number: Amit
#Enter any name: Amit
#Not a name
  
  
  
# ------------------------------>>>>>>>>>>>>>
# Trupti colabs:
  
  
# find max bet 2 numbers
x, y = 5, 65
# True part  if condition  else False part

print ({x}, "is greater")  if (x>y) else print({y},"is smaller value")

#output:
#5 is greater 



'''salary is given
calculate bonus & display net salary
salary bonus
>5000  50% of sal
others 25% of sal'''

salary = 5000
bonus =  salary*(50/100)  if salary>5000  else salary*(25/100)
netSal = salary+bonus
netSal

#output: 6250.0


#pass statement in python
num = 45
if num>10:
    pass
print('End of code')


# ------------------------------------>>>.
# Try and except
try:
    a=2
    b=0
    c=a/b
    print(c)
except:
    print('Something went wrong')
#output: Something went wrong



try:
    a=2
    b=0
    c=a/b
    print(c)
except Exception as e:
    print(e)
#output: division by zero   


try:
    a=2
    b=10
    c=a/b
    print(d)
except Exception as e:
    print(e)
#output: name 'd' is not defined


try:
    a=2
    b=0
    c=a/b
    print(d)
except ZeroDivisionError:
    print('You cannot divide by zero')
    print('-----------')
except NameError:
    print('Variable is not defined')
    #output: You cannot divide by zero
    
    
try:
    print('Database opened successfully')
    f  = open('myfile11111.txt')
    s = f.readline()
    i = int(s.strip())
    print('First line: ',s)

except OSError as err:
    print(err)

except ValueError:
    print('Could not convert data to intereger')

except Exception as err:
    print(err)

finally:
    print('Database closed successfully')
    
    #output: Database opened successfully
    #[Errno 2] No such file or directory: 'myfile11111.txt'
    #Database closed successfully