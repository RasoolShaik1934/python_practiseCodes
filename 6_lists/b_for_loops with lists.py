
# List with Loops:


# for loops with list
for i in [20, 22, 24]:
    print(i)
    # output: 20 22 24
    
for i in range(len([20, 22, 24])):
    print(i)
#output:
# 0
# 1
# 2
    
    
    
# Definite Loops:
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')
#output:
'''
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Happy New Year: sfasfgas
Happy New Year: 87345897345
Done!
'''

frineds = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
#output:
'''Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
Happy New Year: Joseph
Happy New Year: Glenn
Happy New Year: Sally
'''