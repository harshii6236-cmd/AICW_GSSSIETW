#!/usr/bin/env python
# coding: utf-8

# # DAY 3 AICW

# In[2]:


# package/lib/mod installation - pip
get_ipython().system('pip install pandas numpy seaborn matplotlib scikit-learn')


# In[3]:


import numpy as np


# In[4]:


# array 
arr1 = np.array([1, 2, 3, 4])
arr1


# In[8]:


type(arr1)


# In[9]:


# attributes - shape - dimension - dt
arr1.shape


# In[10]:


arr1.ndim


# In[11]:


# array operation 
arr2 = np.array([1, 2, 3,])
arr3 = np.array([3, 2, 1])
add_array = arr2 + arr3
mul_array = arr2 * arr3
print(add_array)
print(mul_array)


# In[13]:


arr2 = np.array([1, 2, 3,])
arr3 = np.array([3, 2, 1, ])
add_array = arr2 + arr3
mul_array = arr2 * arr3
print(add_array)
print(mul_array)


# In[14]:


# indexing and slicing
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr4


# In[15]:


arr4[1, 2]


# In[16]:


arr4[2, 1]


# In[17]:


arr4[1]


# In[18]:


arr4[1,0:1]


# In[19]:


arr4[1,0:2]


# In[20]:


arr4[:,1]


# In[21]:


arr5 = np.arange(12)
arr5


# In[22]:


arr6 = arr5.reshape(3, 4)
arr6


#  ### Stats

# In[23]:


print('mean:', np.mean(arr5))


# In[26]:


print('median:', np.median(arr5))


# In[27]:


print('Std dev:', np.std(arr5))


# ### Dot prod

# In[28]:


a = np.array([[1, 2],[3, 4]])
b = np.array([[5, 6],[7, 8]])
print('Dot prod', np.dot(a,b))


# ## PANDAS

# In[1]:


# pandas - lib - data manipulation
import pandas as pd


# In[2]:


s = [1, 2, 5, 9]
s1 = pd.Series(s)
s1


# In[3]:


d = {
    'Name':'Harshz',
    'Age':'20',
    'place':'Dvg'
}


# In[4]:


type(d)


# In[5]:


df = pd.DataFrame(d, index=[0])
df


# In[6]:


d1 = {
    'Name':['A', 'B','C','D','E'],
    'Age':[12, 22, 10, 9, 20],
    'Marks':[99, 60, 22, 94, 96]
}


# In[7]:


df1 = pd.DataFrame(d1)
df1


# In[8]:


# columns
df1.Name


# In[9]:


df1['Name']


# In[10]:


df1['Marks']


# In[11]:


df1[['Name','Age']]


# In[12]:


df1.loc[1:3]


# In[13]:


df1.iloc[0:3,1:3]


# In[14]:


df1.iloc[3:,2:]


# In[15]:


df1.describe()


# In[16]:


df1.head(2)


# In[17]:


df1.tail(2)


# In[18]:


# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


# load the dataset
df = pd.read_csv(r"C:\Users\GSSS\Downloads\Student_Behaviour.csv")


# In[20]:


# top 5 rows
df.head()


# In[21]:


# rows/column
df.shape


# In[22]:


print(f'Number of rows are {df.shape[0]} and cloumns are {df.shape[1]}')


# In[23]:


df.columns


# In[24]:


# access of column
df.Gender


# In[25]:


df['Certification Course']


# In[26]:


df['Gender']


# In[27]:


df.info()


#  ### stats of dataset

# In[28]:


df.describe()


# In[29]:


df.isnull().sum()


# In[30]:


df.duplicated().sum()


# In[31]:


# visualize - univariable
sns.histplot(data= df, x='Gender')


# In[32]:


sns.histplot(data= df, x='Gender')
plt.title('Univariant Analysis')
plt.show()


# In[34]:


df.columns


# In[35]:


sns.histplot(data=df, x= 'Certification Course')


# In[40]:


sns.histplot(data=df, x='Travelling Time ')


# In[41]:


df['Certification Course'].unique()


# In[42]:


df['Certification Course'].nunique()


# In[43]:


df['Certification Course'].value_counts()


# In[44]:


df['Height(CM)'].value_counts()


# In[46]:


df.Gender.value_counts()


# In[47]:


df.Gender.value_counts().plot(kind='pie', autopct='%1.2f%%')


# In[50]:


df.Gender.value_counts().plot(kind='bar')


# In[51]:


df['Department'].unique()


# In[52]:


df['Department'].nunique()


# In[53]:


df['Department'].value_counts()


# In[56]:


df[['Department','Gender']].value_counts()


# In[ ]:




