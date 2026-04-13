
'''
Import/export data with pandas
in pandas we can read by importing the data of CSV, excel, Jason, HTML….etc by using read_*
we can export the data to csv, HTML, excel, Jason, SQL…….etc by using to_*
'''

'''
    We can download and observe the datasets from kaggle
    Open the given link: https://www.kaggle.com/datasets
    You can observe and search the topics on which the datasets are given
For example:
    We can download automobile csv file from the given link:
        https://www.kaggle.com/datasets/toramky/automobile-dataset
    We can download penguins csv file from the given links
        https://www.kaggle.com/datasets/larsen0966/penguins

Working with CSV(comma seperated values) files in Panda
'''

# Import hard disk files on colab

from google.colab import files
uploaded = files.upload()
#------------
myfile = "Automobile_data.csv"

df = pd.read_csv(myfile)
df
#------------
df.columns
df.describe()
df.info()
df.shape()
df.head()
df.tail()


myfile = "/content/global_alcohol.csv"

df = pd.read_csv(myfile)
df.head()


# replace whitespace into underscore
df.columns = df.columns.str.replace(' ','_')
df.columns

# top 10 entries of display value
df.sort_values(by= 'Display_Value', ascending = False).head(10)


# create a new col, having displ value as more than .7
df['High_Consumption'] = df['Display_Value'] > .7
df[df['High_Consumption']] [['Country','Display_Value']]


# create a new col, having displ value as more than .7
df['High_Consumption'] = df['Display_Value'] > .7
High_Consumption = df[df['High_Consumption']] [['Country','Display_Value']]
High_Consumption

# create a flag for popular countries for wine
df['Wine_flag'] = df.apply(lambda row: 'Top Wine Country'  if row['Beverage_Types']=='Wine' and
                           row['Display_Value']>5 else '', axis=1)
df

'''
Pandas to_csv()
    The to_csv() method is a built-in function in Pandas
    It allows you to save a Pandas DataFrame as a CSV file.
    This method exports the DataFrame into a comma-separated values (CSV) file, which is a simple and widely used format for storing tabular data.
'''

# multiple examples (simple n complex) of decorators


#-------------------->>>
# simple decorator
def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Welcome to the session.")
    return wrapper
@greet_decorator
def intro():
    print("I am learning Python.")
intro()

#------------------->>>
# decorator with argument
def multiply_decorator(func):
    def wrapper(x, y):
        print(f"Multiplying {x} and {y}")
        result = func(x, y)
        print(f"Result is: {result}")
        return result
    return wrapper
@multiply_decorator
def multiply(a, b):
    return a * b
multiply(3, 4)

#----------------------->>>
# Decorator for Timing Function Execution (Useful in Data Science)

import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper
@timing_decorator
def compute_square(n):
    return [x**2 for x in range(n)]
compute_square(20)  # modify 20 by 10000 and observe the o/p


#-------------------------->>>  

# Decorator for Timing Function Execution (Useful in Data Science)

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def compute_square(n):
    return [x**2 for x in range(n)]

compute_square(20)  # modify 20 by 10000 and observe the o/p

#-------------------------->>>

# Use Case: Data Preprocessing Decorator in Data Science

def clean_data(func):
    def wrapper(data):
        # Remove null values and reset index
        cleaned = data.dropna().reset_index(drop=True)
        return func(cleaned)
    return wrapper

import pandas as pd

@clean_data
def analyze(df):
    print("Average Age:", df["Age"].mean())

df = pd.DataFrame({
    "Name": ["Alice", "Bob", None],
    "Age": [25, None, 30]
})

analyze(df)

#-------------------------->>>

