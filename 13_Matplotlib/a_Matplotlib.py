'''Import Libraries:
Exercise 1: Line chart
For the given data, plot the Line chart.
Hint: plt.plot
'''

import matplotlib.pyplot as plt  # ← This line MUST be present
import numpy as np


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


#--------------------------------->>>>

'''Matplotlib

    Matplotlib is one of the most popular Python packages used for data visualization.
    It is a cross-platform library for making 2D plots.

pyplot module

    Pyplot is a Matplotlib module
    matplotlib.pyplot is a collection of command style functions
'''


'''
plt.figure()
    We can change the size of the plot above using the figsize() attribute of the figure() function.
    Syntax: figure(figsize=(WIDTH_SIZE,HEIGHT_SIZE))
'''

# Let's create simple line plot/chart/graph

x = np.array([3,7,4,10])
y = np.array([6,9,12,15])

plt.plot(x,y)
plt.show()

# Let's create simple line plot/chart/graph

x = np.array([3,7,4,10])
y = np.array([6,9,12,15])

plt.plot(x,y)
plt.show()

#------------------------------>>>>
# Let's create simple line plot/chart/graph

x = np.array([3,7,4,10])
y = np.array([6,9,12,15])

plt.figure(figsize = (4,2))

plt.plot(x,y)
plt.show()

#------------------------------>>>>

# Mark each point with a diamond
'''Markers

    Marker is used to emphasize each point with a specified marker
    Follow the link for markers, linestype, marker-color
     https://matplotlib.org/stable/api/markers_api.html
     '''
x = np.array([3,7,4,10])
y = np.array([6,9,12,15])

plt.figure(figsize=(4,2))   # set height n width of the plot

plt.plot(x,y, marker='D')    # create plot
plt.show()                   # show the plot/chart

#------------------------------>>>>

# Mark each point with a .....red circle, lines should b dotted

x = np.array([3,7,4,10])
y = np.array([6,9,12,15])

plt.figure(figsize=(4,2))

plt.plot(x,y, 'o:r')
plt.show()

#------------------------------>>>>
x = np.array([3,7,4,10])
y = np.array([6,9,12,15])

plt.figure(figsize=(4,2))

plt.plot(x,y, '*--g')  # green star, dashed line
plt.show()

#   ------------------------------>>>>

# Mark each point with a blue hexagon, lines should be solid
# Give titles to the plot

# Create Labels for 'Information about Sports'

# Assume that x is 'Average Pulse'
x = np.array([78, 85, 90, 95, 100, 105, 110, 115, 120, 125])

# Assume that y is 'Calorie Burnage'
y = np.array([230, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.figure(figsize=(5,3))

plt.plot(x,y, 'H-b')

plt.title("Information about Sports")
plt.xlabel('Average Pulse')
plt.ylabel('Calorie Burnage')

plt.show()

#------------------------------>>>>

# Create a single subplot

x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Create a figure and a single subplot
fig, ax = plt.subplots()  # subplots() returns a tuple (fig, ax)

# Plot the data
ax.plot(x,y, marker = 'o', color='blue', label='Sample Data')

# Add title and labels
ax.set_title("Simple line plot")
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')

# Optional: Add grid and legend
ax.grid(True)
ax.legend()

# Show the plot
#plt.tight_layout()
plt.show()

#------------------------------>>>>

# draw 4 subplots

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [1, 4, 9, 16, 25]
y3 = [50, 40, 30, 20, 10]
y4 = [2, 3, 5, 7, 11]

# Create 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Top-left plot
axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title('Line Plot')

# Top-right plot
axs[0, 1].bar(x, y2, color='green')
axs[0, 1].set_title('Bar Plot')

# Bottom-left plot
axs[1, 0].scatter(x, y3, color='red')
axs[1, 0].set_title('Scatter Plot')

# Bottom-right plot
axs[1, 1].fill_between(x, y4, color='orange', alpha=0.6)
axs[1, 1].set_title('Area Plot')

# Adjust layout
plt.tight_layout()
plt.show()

#------------------------------>>>>

# Create a bar plot for Sales-Of-Fruits

x = ["ORANGE", "BLUEBERRY", "APPLES", "BANANAS"]
y = [280, 400, 670, 350]
colors = np.array(["orange", "purple", "beige", "tan"])

plt.bar(x,y, color = colors)

plt.xlabel('Fruit names')
plt.ylabel('Sale of fruits')
plt.title('Fruit Sale Chart')

plt.show()
#------------------------------>>>>

# create a bar plot with bar labels

x = ["ORANGE", "BLUEBERRY", "APPLES", "BANANAS"]
y = [280, 400, 670, 350]
colors = np.array(["orange", "purple", "beige", "tan"])

fig, ax = plt.subplots(figsize = (7,4))
bars = ax.bar(x,y, color= colors)

ax.bar_label(bars, padding = 3)

ax.set_ylim(0, 750)  # will extend the y-limit upto 750

plt.show()

#------------------------------>>>>

# create a horizontal bar plot

x = ["ORANGE", "BLUEBERRY", "APPLES", "BANANAS"]
y = [280, 400, 670, 350]
colors = np.array(["orange", "purple", "beige", "tan"])


fig, ax = plt.subplots(figsize = (7,4))
bars = ax.barh(x,y, color= colors)

ax.bar_label(bars, padding = 3)

ax.set_xlim(0, 800)  # will extend the x-limit upto 800

plt.show()

#------------------------------>>>>

'''Histogram

    A histogram is a graph showing frequency distributions
    It gives you accurate representation of a numerical data
    It shows the number of observations within each given interval
    '''

# simple histogram

# Generate random data for the histogram
data = np.random.randn(1000)

# Plotting a basic histogram
plt.hist(data, bins=5, color='skyblue', edgecolor='black')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

# Display the plot
plt.show()

#output will be a histogram with 5 bins, showing the frequency distribution of the random data generated. The x-axis will represent the values of the data, while the y-axis will represent the frequency of those values within each bin. The bars of the histogram will be colored sky blue with black edges for better visibility.

#------------------------------->>>>
# Marks data
marks = [90, 43, 87, 91, 34, 37, 82, 71, 60, 52]

# Define intervals and labels
grade_intervals = [0, 35, 70, 100]
grade_labels = ['Fail', 'Pass', 'Distinction']

# Create a DataFrame
df = pd.DataFrame({'Marks': marks})

# Bin the marks into categories
df['Grade'] = pd.cut(df['Marks'], bins=grade_intervals, labels=grade_labels, right=True)

# Count number of students in each category
grade_counts = df['Grade'].value_counts().sort_index()

# Plot the histogram as a bar chart
fig, ax = plt.subplots(figsize=(8,6))
grade_counts.plot(kind='bar', color='skyblue', ax=ax)

# Set titles and labels
ax.set_title('Distribution of Student Grades')
ax.set_xlabel('Grade Category')
ax.set_ylabel('Number of Students')

# Display plot
plt.tight_layout()
plt.show()

#-------------------------------------- 
'''
Scatter Plot

    A scatter plot is a diagram where each value in the data set is represented by a dot.
    The matplotlib.pyplot.scatter() plots serve as a visual tool to explore and analyze the relationships between variables, utilizing dots to depict the connection between them.
    The scatter() method is specifically designed for creating scatter plots.
'''
# Sample data: Advertising budget vs sales
ad_budget = [100, 200, 300, 400, 500]
sales = [20, 40, 60, 80, 100]

# Create scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(ad_budget, sales, color='blue', s=80)

# Add labels and title
plt.title("Ad Budget vs Sales")
plt.xlabel("Advertising Budget ($)")
plt.ylabel("Sales ($)")

plt.grid(True)
plt.tight_layout()
plt.show()

#------------------------------>>>>
'''
Pie plot:
    Pie charts provide a visual representation of data that makes it easy to compare parts of a whole.
    Syntax:
        matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)
'''

# Sample data: Fruit distribution

labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 25, 20]

# Plot pie chart
plt.figure(figsize=(5, 5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Fruit Distribution")
plt.axis('equal')

plt.tight_layout()
plt.show()