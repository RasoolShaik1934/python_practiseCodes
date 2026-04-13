
'''Pandas
An open source package built on top of numpy - pandas is an easy to use package for data structures and data analysis
pandas can be used with different types of data:
- tabular data with heterogeneously typed columns 
- ordered and unordered time series data 
- arbitrary matrix data with row and column labels 
- observational or statistical data sets
Installing And using pandas: - we install pandas using the Python pip install when using Python on the local system or in an IDE using

In collaborator, pandas need to be imported as this library is already available: Import pandas as pd
'''

'''
# **Pandas data structures: “Series and DataFrame”**

There are 2 main data structures in pandas:
1.	Series(1D)
2.	DataFrame(2D)

      i.e., Series + series = DataFrame



**Panda series object:**
an analogue of one dimensional array
-	a panda series is a one dimensional array of indexed data
-	it contains homogeneous data with fixed size

**constructing series object:**
----------#####---->>>Syntax: pd.Series(data, index = index, dtype, copy)

- Here data can be any list , Numpy array, scalar value, or dictionary
-	Index is an optional argument for indexing, must be of same length data

it forms a new series: a wrap of both sequence of values and sequence of indices along with data type.
'''


# construct a series using a list

import pandas as pd
s1 = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
print(s1)

#output
# a    0.25
# b    0.50
# c    0.75
# d    1.00
# dtype: float64


# Construct a series using an array
import numpy as np
import pandas as pd

info = np.array([0.25, 0.5, 0.75, 1.0])


s2 = pd.Series(info, index = ['a', 'b', 'c', 'd'])
print(s2)

#output
# a    0.25
# b    0.50
# c    0.75
# d    1.00
# dtype: float64


#Series object attributes

x = pd.Series([1,2,3], index = ['a', 'b', 'c'])

print("shape:", x.shape)
print("size:", x.size)
print("index:", x.index)
print("values:", x.values)
print("dimensions:", x.ndim)
print("data type:", x.dtype)


#output
# shape: (3,)
# size: 3
# index: Index(['a', 'b', 'c'], dtype='object')
# values: [1 2 3]
# dimensions: 1
# data type: int64



'''Shape returns a tuple of shape of the data
size return the size of the data
index defines the index of the series
values returns the values of series as list
ndim returns the number of dimensions in the
dtype return the data type of the data
'''


'''
# **pandas data frame object:**
- a data frame is an analogue of a 2 dimensional array with both flexible row indices and flexible column names
-	it is a sequence of serious objects that share the same index

i.e., (series1: city, area) + (series2: city, population) = (DataFrame : city, area, population)


**constructing data frame object:**
    ----------#####---->>>syntax: pd.DataFrame(data, index = index, columns = cols)
-	here data can be anything like list, list of dictionaries, series object, Dictionary of lists, Dictionary of series, 2D numpy array.
-	here index to use for resulting frame, must be of same length as data rows
-	column labels to use for resulting frame, must be of same lengths data columns

we get a new data frame: consisting table of values sequence of row indices and sequence of column indices.
-	Data can be a list, in which index and columns need to give explicitly
-	Data can be a dictionary, in which columns default dictionary keys
-	Data can be a Dictionary of series, in which index defaults to series indices
'''

# constructing data frame using list
data = [[423967, 38332521], [170312, 19552860], [149995, 12882135], [141297, 19651127], [695662, 26448193]]
df1 = pd.DataFrame(data, index = ['california', 'florida', 'illinois', 'new york', 'texas'], columns = ['area', 'population'])
print(df1)

#output
#               area  population
# california  423967    38332521
# florida     170312    19552860
# illinois    149995    12882135
# new york    141297    19651127
# texas       695662    26448193


# constructing dataframe using a dictionary
data ={'area': [423967, 170312, 149995, 141297, 695662],
       'population' : [38332521, 19552860, 12882135, 19651127, 26448193]}
df2 = pd.DataFrame(data, index = ['california', 'florida', 'illinois', 'new york', 'texas'])
print(df2)

#output
#              area  population
# california  423967    38332521
# florida     170312    19552860
# illinois    149995    12882135
# new york    141297    19651127
# texas       695662    26448193


#constructing dataframe using a dictionary of series
idx = ['california', 'florida', 'illinois', 'new york', 'texas']
data = {'area': pd.Series([423967, 170312, 149995, 141297, 695662], index = idx),
        'population': pd.Series([38332521, 19552860, 12882135, 19651127, 26448193], index = idx)}
df3 = pd.DataFrame(data)
print(df3)

#output
#               area  population
# california  423967    38332521
# florida     170312    19552860
# illinois    149995    12882135
# new york    141297    19651127
# texas       695662    26448193



#DataFrame object attributes

df = pd.DataFrame({'A': [1,2,3],
                   'B': [1,4,9]},
                  index = ['a','b','c',])
print("shape:", df.shape)
print("size:", df.size)
print("index:", df.index)
print("values", df.values)
print("transpose", df.transpose)

#output
# shape: (3, 2)
# size: 6
# index: Index(['a', 'b', 'c'], dtype='object')
# values [[1 1]
#  [2 4]
#  [3 9]]
# transpose <bound method DataFrame.transpose of    A  B
# a  1  1
# b  2  4
# c  3  9>




'''Shape returns a tuple of shape of the data
size returns the size of the data
index defines the index of the data frame
values returns the values of data frame as list
T swap rows and columns
'''


'''Import/export data with pandas
in pandas we can read by importing the data of CSV, excel, Jason, HTML….etc by using read_*
we can export the data to csv, HTML, excel, Jason, SQL…….etc by using to_*
    pd.read_csv(file name) : read the data from CSV file
    pd.read_table(file name): read the data from determine text file
    pd.read_excel(file name): read the data from the excel file
    Pd.read_sql(query, connection_object): read the data from a SQL table/database
    Pd.read_json(json_string): read the data from a Json formatted string, URL, or file
    '''
'''
the pandas functions that can be used to accomplish most of your data tasks are: 
- Pd.read_csv() 
- df.describe() 
- df.Info() 
- df.Plot() 
- df.iloc() 
- df.loc() 
- df.query() 
- df.Sort_values() 
- df.Isnull() 
- df.fillna() 
- df.dropna() 
- df.drop() 
- df.groupby() 
- df.merge() 
- df.rename() 
- df.to_csv()
'''

#----------------------------------------------->>>>>
#Trupthi madam class:
'''
Pandas in Python

    Pandas is a package that can be used in Python language.
    This library package is used mostly for activities such as
        data processing, cleaning, filtering activities in machine learning programming.

Pandas Data structures (2 types)

    Series - 1 dimensional [can be create using a list/tuple ]
    Dataframe - 2 dimensional [can be create using a nested list / dictionary / series / another dataframe ]
'''

'''Pandas data structures:
There are 2 main data structures in pandas: 1. Series(1D) 2. DataFrame(2D)
Panda series object: - A panda series is a one dimensional array of indexed data - It contains homogeneous data with fixed size
Syntax:
    pd.Series(data, index = index, dtype, copy)
'''

# Create Series from a list
data = ['python','java','php','spark']

series1 = pd.Series(data)
series1

# Create Series from a list with index
data = ['python','java','php','spark']

#-------------------------------------------->>>>>

# Create pandas Series with custom index
data = ['python','java','php','spark']

listLabel = ['r1','r2','r3','r4']

series1 = pd.Series(data, index = listLabel)
series1

#output
# r1    python
# r2      java
# r3       php    
# r4     spark
# dtype: object

#--------------------------------------------->>>>>

# Create pandas Series from a dictionary

data = {'Courses1' :"pandas",
        'Fees' : 20000,
        'Duration' : "30days",
        'Courses' :"pearl", }

series1 = pd.Series(data, name = 'Courses')
series1

#------------------------------------------------------>>>>>

# OBSERVE THE CODE
# Series Object Attributes

# Create Series from a list
data = [34,21,89,77,50,52]

x = pd.Series(data, index = ['a', 'b', 'c','d','e','f'])

print("shape:", x.shape)
print("size:", x.size)
print("index:", x.index)
print("values:", x.values)
print("dimensions:", x.ndim)
print("data type:", x.dtype)
#output
# shape: (6,)
# size: 6  
# index: Index(['a', 'b', 'c', 'd', 'e', 'f'], dtype='object')
# values: [34 21 89 77 50 52]

#------------------------------
'''Create pandas DataFrame

    One of the easiest ways to create a pandas DataFrame is by using its constructor.
    The DataFrame constructor takes several optional params that are used to specify the characteristics of the DataFrame.
    Syntax :
        pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

Note: A dataframe can be created using a list, nestedList, tuple, series, dictionary or another dataframe
'''

#----------------------------->>>>>>

# Create Series (with a name) using a list
mylist = ['python','java','pearl','php']

series1 = pd.Series(mylist, name='Courses')
print(series1)
print("------>>>>>>>-------->>>>>>")

# Create a DataFrame from a Series

df = pd.DataFrame(series1)
df

#output
# 0   python
# 1     java
# 2    pearl
# 3      php
# Name: Courses, dtype: object

#------------------------------>>>>>>

# Create a dataframe using a nested list

data = [[423967, 38332521],
        [170312, 19552860],
        [149995, 12882135],
        [141297, 19651127],
        [695662, 26448193]]

indlist = ['california', 'florida', 'illinois', 'new york', 'texas']

df = pd.DataFrame(data,index=indlist)
df
#output
#               0          1   
# california  423967    38332521
# florida     170312    19552860
# illinois    149995    12882135
# new york    141297    19651127
# texas       695662    26448193

#------------------------------>>>>>>

# Create a dataframe using a nested list

data = [[423967, 38332521],
        [170312, 19552860],
        [149995, 12882135],
        [141297, 19651127],
        [695662, 26448193]]

indlist = ['california', 'florida', 'illinois', 'new york', 'texas']

df = pd.DataFrame(data, index = indlist, columns = ['Area', 'Population'])
df


# Create a DataFrame using a dictionary
data = {'Courses': ['Pearl', 'R', 'Python'],
        'Duration':['30 days', '40 days', '50 days'],
        'Fee': [20000, 25000, 26000]
        }
df = pd.DataFrame(data)
df

#output
#   Courses Duration    Fee
# 0  Pearl  30 days  20000
# 1     R  40 days  25000
# 2  Python  50 days  26000

#------------------------------->>>>>>

# Create Lists
Courses = ['Spark', 'Pandas', 'NumPy']
Fee = [20000,25000]
Duration = ['30days','40days']

# Merge all the list objects using zip()
tuplelist = list(zip(Courses,Fee,Duration))

tuplelist

#output
[('Spark', 20000, '30days'), ('Pandas', 25000, '40days')]

df = pd.DataFrame(tuplelist)
df
#output
#        0      1        2  
# 0   Spark  20000  30days
# 1  Pandas  25000  40days

#-------------------------------->>>>>>

# Consider a given DataFrame
df = pd.DataFrame({
   'A': ['1', '2', '3'],
   'B': ['4', '5', '6'],
   'C': ['7', '8', '9']
})
df
#output
#    A  B  C
# 0  1  4  7
# 1  2  5  8
# 2  3  6  9

# modify col A as float
df['A'] = df['A'].astype(float)
df.dtypes
#output
# A    float64

# modify multiple cols
df = df.astype({'B': int, 'C':int })
df


#------------------------------->>>>>>

# Observe the code
# DataFrame object attributes

df = pd.DataFrame({'code': [101,205,307],
                   'name': ['John','Shilpa','Kelly']},
                  index = ['a','b','c',])

print("Shape:")
print(df.shape)
print("Size:")
print(df.size)
print("Index:")
print(df.index)
print("Values")
print(df.values)
print("Transpose")
print(df.T)

#output
# Shape:
# (3, 2)
# Size:
# 6
# Index:
# Index(['a', 'b', 'c'], dtype='object')
# Values
# [['101' 'John']
#  ['205' 'Shilpa']
#  ['307' 'Kelly']]
# Transpose
# code    101   205   307
# name  John Shilpa Kelly

#directMethod:

df = pd.DataFrame({'code': [101,205,307],
                   'name': ['John','Shilpa',None]},
                  index = ['a','b','c',])
df
#output
#    code    name
# a   101    John
# b   205  Shilpa
# c   307    None


# ------------------------------->>>>>>