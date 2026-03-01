
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
#Demo test repeated for git push remove later
