import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# Creating a simple Series
test_series = pd.Series([1, np.nan, 3])
print(test_series)

dates = pd.date_range('20130101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

## Control delimiters, rows, column names with read_csv (see later) 
# adult_data = pd.read_csv("adult.csv") 

## Preview the first 5 lines of the loaded data 
#adult_data.head()

# print(adult_data)