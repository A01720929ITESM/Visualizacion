#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[5]:


get_ipython().run_line_magic('ls', '')


# In[6]:


df = pd.read_excel('datasets/Canada.xlsx',
                  engine = 'openpyxl', sheet_name='Canada by Citizenship', skiprows=range(20))


# In[12]:


df.head(3)


# In[13]:


df.tail(3)


# In[14]:


pd.set_option('display.max_rows',None)


# In[15]:


df


# In[16]:


df.columns


# In[17]:


df.info(verbose=False)


# In[18]:


df.index


# In[21]:


df.drop(['AREA','REG','DEV','Type','Coverage'],
       axis = 1,
       inplace= True)

df.columns


# In[22]:


df.head()


# In[23]:


df.rename(columns={'OdName':'Country',
                  'AreaName':'Continent',
                  'RegName':'Region'},
         inplace = True)


# In[24]:


df.head()


# In[ ]:




