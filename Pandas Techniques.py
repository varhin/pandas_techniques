#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#.SORT_VALUES()
#sorting one column
df.sort_values('age')

#sorting two or more columns 
df.sort_values(['age', 'weight'])


# In[ ]:


#sorting in ascending order
df.sort_values('age', ascending = True)

#sorting in descending order
df.sort_values('age', ascending = False)


# In[ ]:


#.SORT_INDEX()
df.sort_index()

#sort along row
df.sort_index(axis=0)
#sort along column
df.sort_index(axis=1)
#sort in ascending order
df.sort_index(ascending=True)
#sort in descending order
df.sort_index(ascending=False)


# In[ ]:


#merging DataFrames
pd.merge(dataframe_1, dataframe_2, on='column_name', how='inner')


# In[ ]:


#viewing a DataFrame
#first few rows
df.head()

#viewing a number of rows(from the top)
df.head(7)

#last few rows
df.tail()
#viewing a number of rows(from the bottom)
df.tail(4)

#shape of a DataFrame
df.shape
#number of rows
df.shape[0]
#number of columns
df.shape[1]

#information about a DataFrame
df.info()


# In[ ]:


#selecting rows and columns in a DataGFrame
df.iloc[2,3]

df.loc['row_name', 'column_name']

#using index
df.ix[1,4]
#using label
df.ix['row','column']
#using both index and label
df.ix[3, 'column']


# In[ ]:


#summary statistics

#calculates the mean
df.mean()

#find the median
df.median()

#find the mode
df.mode()

#find minimum value
df.min()

#find maximum value
df.max()

#calculate the standard deviation
df.std()

#calcuate the variance 
df.var()

