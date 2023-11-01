#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Evaluate the FAA Dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: VIew and import the dataset

# In[1]:


#Import necessary libraries
import pandas as pd
import sqlite3 as sql


# In[9]:


#Import the FAA (Federal Aviation Authority) dataset
df = pd.read_csv("C:\\Users\\sagar\\Downloads\\Lesson 7 -1\\faa_ai_prelim\\faa_ai_prelim.csv")


# #### 2: View and understand the dataset

# In[11]:


#View the dataset shape
df.shape


# In[12]:


#View the first five observations
df.head()


# In[13]:


#View all the columns present in the dataset
df.columns


# #### 3: Extract the following attributes from the dataset:
# 1. Aircraft make name
# 2. State name
# 3. Aircraft model name
# 4. Text information
# 5. Flight phase
# 6. Event description type
# 7. Fatal flag

# In[24]:


#Create a new dataframe with only the required columns
df1 = df[['ACFT_MAKE_NAME','LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT','FLT_PHASE', 'EVENT_TYPE_DESC','FATAL_FLAG']]


# In[25]:


#View the type of the object
type(df1)


# In[26]:


#Check if the dataframe contains all the required attributes
df1.head()


# #### 4. Clean the dataset and replace the fatal flag NaN with “No”

# In[27]:


#Replace all Fatal Flag missing values with the required output
df1['FATAL_FLAG'].fillna("No", inplace = True)


# In[23]:


#Verify if the missing values are replaced
df1


# In[28]:


#Check the number of observations
df1.shape


# #### 5. Remove all the observations where aircraft names are not available

# In[29]:


#Drop the unwanted values/observations from the dataset
df2 = df1.dropna(subset = ["ACFT_MAKE_NAME"])
df2


# #### 6. Find the aircraft types and their occurrences in the dataset

# In[30]:


#Check the number of observations now to compare it with the original dataset and see how many values have been dropped
df2.shape


# In[35]:


#Group the dataset by aircraft name
at = df2.groupby("ACFT_MAKE_NAME")


# In[36]:


#View the number of times each aircraft type appears in the dataset (Hint: use the size() method)
at.size()


# #### 7: Display the observations where fatal flag is “Yes”

# In[37]:


#Group the dataset by fatal flag
ff = df2.groupby('FATAL_FLAG')


# In[39]:


#View the total number of fatal and non-fatal accidents
ff.size()
aff = ff.get_group("Yes")


# In[40]:


#Create a new dataframe to view only the fatal accidents (Fatal Flag values = Yes)
aff


# In[ ]:




