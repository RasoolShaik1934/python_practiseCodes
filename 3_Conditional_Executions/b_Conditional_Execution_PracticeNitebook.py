'''
Comparison Operators are available for the purpose of comparison. We validate equal to, greater than or less than and so on. To support these kind of comparisons, we use comparison operators. The following are list of comparison operators:

a == b # it represents a equal to b

a > b # it represents a greater than b

a < b # it represents a less than b

a != b # it represents a not equal to b

a >= b # it represents a greater than or equal to b

a <= b # it represents a less than or equal to b
Exercise 1: Assume variable a holds 10 and variable b holds 20, then perform each of the comparison operators listed above.
'''
'''
Exercise 2:

    Input two variables, marks_student (marks that a student in the class obtained), max_marks (maximum marks scored in the class).
    Write one block of 'if' statement to compare whether the marks scored by the student is valid (i.e. less than or equal to max marks) or not.
    If marks are less than maximum marks in the class and greater than 40, print, welcome to the class, your marks are: (marks of the student).

'''
'''#### Exercise 3:

There is an ongoing recruitment process for the march past parade in the police academy.
- The selection procedure for this activity is very simple.
* If the candidate's height is greater than 180 cm, they can participate in the activity.
__________________________________

* Input height of the individual
* write one block of 'if' statement to compare the height of the individual with 180 cm.
* For a candidate whose height is greater than 180 cm, print the statements:
  * Welcome to the academy.
  * We will begin march past practice from tomorrow.
  * You will receive your selection letter via mail.
  '''
  
'''
  There is a good news for the participants. If they applied for march past parade but could not make it to the activity because their height is less than 180 cm, they can still participate in the Tug-Of-War activity.
Write if-else-if statements:
    if the required height was met, they participated.
    else, they could not participate in march past.
    But if their weight is between 65-80, give them a good news that they can participate in Tug-Of-War.
  '''
#YOUR CODE HERE
height = 180
weight = 80
p1Height = 160
p1Weight = 65
if p1Height>=height:
  print("you can participate in parade")
elif p1Weight<=weight:
  print("you can participate in Tug-Of-War")
  
'''
 Exercise 6:
    There is one more activity being held in the police academy.
    It is a 'Tug-Of-War' competition.
    The only individuals whose height is above 180 cm can attend the event because they are part of march past team.
    The individuals whose weight is between 65 to 70/ 70 to 75/ 75 to 80 Kg will play the game in different teams.
In the similar fashion.
    write 'else-if' ladder to display appropriate messages to the selected individuals.
    If the requirement of their height is met, they can attend the program.
    If their weight is between 65 to 70, they will play in Team A.
    If their weight is between 70 to 75, they will play in Team B.
    If their weight is between 75 to 80, they will play in Team C.
    
    If the individual's height is more than 180 cm, they are already a part of another event and hence they will not participate here.
 '''
 #YOUR CODE HERE
height = 180

minweight = 65
maxweight = 80

p1Height = 190
p1Weight = 80

p2Height = 170
p2Weight = 70

p3Height = 179
p3Weight = 75

p4Height = 168
p4Weight = 80

if p1Height>=height and p1Weight>=80:
  print("P1 you can participate in both Parade and TeamC")
if p2Height<=height and p2Weight>=65:
  print("P2 will play in Team A.")
if p3Height<=height and p3Weight>=75:
  print("P3 will play in Team B.")
if p4Height<=height and p4Weight>=80:
  print("P4 will play in Team C.")