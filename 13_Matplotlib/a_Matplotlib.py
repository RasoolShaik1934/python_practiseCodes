'''Import Libraries:
Exercise 1: Line chart
For the given data, plot the Line chart.
Hint: plt.plot
'''

# x-axis values
x = [0, 1, 2, 3, 4]
# y-axis values
y = [2, 4, 6, 8, 10]

# plotting the line graph
plt.plot(x, y)
# setting the x and y axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# setting the title of the graph
plt.title('Simple Line Graph')

# displaying the graph
plt.show()


'''
Exercise 2: Pie chart
For the given data plot the pie chart.
Hint: plt.pie
'''

labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
sizes = [1,2,3,4,5,6,7,8,9,10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

## YOUR CODE HERE
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()


'''
Exercise 3: Heights and weights are given below.
Taking height as x-axis and weight as y-axis, scatter the points.
Hint: plt.scatter
'''
male_heights= [73, 68, 74, 71 , 69, 67, 68, 68, 67, 63]
male_weights= [241, 162, 212, 220 , 206, 152, 183 , 167, 175 , 156]

## YOUR CODE HERE
plt.scatter(male_heights,male_weights)
plt.title('male-heights&weights')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
plt.close()



'''Exercise 4: Female height and weight are given below:
    Along with male height and weight, also plot female height and weight, with different marker.
    Indicate with a label for height and weight (X-axis, Y-axis).
    Indicate with legends for male and female.
Hint: legend and label
'''

female_weights = [102, 141 , 131, 128, 129, 156, 114, 165, 111, 104]
female_heights = [58, 65, 63, 64, 61, 65, 62, 65, 61, 63]

## YOUR CODE HERE
plt.figure(figsize=(20, 10))
plt.scatter(male_heights,male_weights,marker='*',label='Male')
plt.scatter(female_heights,female_weights,marker='o',label='Female')
plt.legend(loc='lower right')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Comparison of Male Female heights and weights')
plt.show()
plt.close()



'''
Exercise 5: For the given data, plot the Bar graph and do the following:
    Set the x and y axis-labels.
    give the title as 'Bar Graph'.
Hint: plt.bar
'''


# x-axis values
x = ['A', 'B', 'C', 'D', 'E']

# y-axis values
y = [10, 20, 30, 40, 50]

# plotting the bar graph
plt.bar(x, y)

# setting the x and y axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# setting the title of the graph
plt.title('Bar Graph')

# displaying the graph
plt.show()


'''Exercise 6: For the given data, create four subplots using 2x2 grid and perform the following:

    The first subplot should show a line graph.
    Second subplot should show a scatter plot.
    The third subplot should show a bar graph of the weight of four men's.
    The fourth subplot should show a histogram of the ages of a group of 4 people.
    '''
    
# Create data for the subplots
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
scatter_data1 = [1, 2, 3, 4]
scatter_data2 = [2, 4, 6, 8]
bar_data = [1, 2, 3, 4]
bar_Weights = [50, 75, 100, 120]
hist_data = [18, 22, 28, 31, 37, 42, 49, 52, 57, 65]

# Create the figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# line graph to the first subplot
axs[0, 0].plot(x, y)
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].set_title('Line Graph')

# scatter plot to second subplot
axs[0, 1].scatter(scatter_data1, scatter_data2)
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Y-axis')
axs[0, 1].set_title('Scatter Plot')

# bar graph to the third subplot
axs[1, 0].bar(bar_data, bar_Weights)
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Men Weights (m)')
axs[1, 0].set_title('Bar Graph')

# histogram to the fourth subplot
axs[1, 1].hist(hist_data, bins=8)
axs[1, 1].set_xlabel('Age')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram')

# title for subplots
fig.suptitle('Four Subplots')

# Adjust the spacing between the subplots
fig.tight_layout()

plt.show()