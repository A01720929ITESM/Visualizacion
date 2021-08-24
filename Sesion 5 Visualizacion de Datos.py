#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from scipy import stats
from pylab import *

stats.norm.rvs(size=10)


# In[7]:


dx = 0.01
x = np.arange(-2, 2, dx)
y= exp(-x**2)

plot(x,y)
plt.show()


# In[14]:


import matplotlib.pyplot as plt
ax = plt.plot(2,3,'x')
plt.title('A title')
plt.xlabel('Valor X')
plt.ylabel('Valor Y')
plt.show()


# In[24]:


data = {
    'Name': ['Jim', 'Dwight', 'Angela', 'Tobi'],
    'Age': [30,22,21,20],
    'Weight': [50,55,60,80]
    
}
df = pd.DataFrame(data)
df


# In[25]:


una_variable= df.plot()


# In[26]:


df.plot()


# In[27]:


df['Age'].plot(kind='hist')


# In[28]:


df= pd.read_csv('datasets/Cartwheeldata.csv')
df.head(2)


# In[43]:


import seaborn as sns

sns.lmplot(
    x='Wingspan',
    y='CWDistance',
    data = df,
    fit_reg = False,
    hue='Gender'
)
plt.show()


# In[50]:


sns.swarmplot(
    x='Gender',
    y='CWDistance',
    data = df
)


# In[54]:


sns.boxplot(
    data = df.loc[:,['Height','Wingspan','CWDistance']]
)
plt.show()


# In[85]:


fig = plt.figure()
ax1 = fig.add_subplot(1,3,1) #1reg,2col,position1
sns.boxplot(
    data= df.loc[df['Gender']=='F',['Score']]
)

ax2= fig.add_subplot(1,3,3)
sns.boxplot(
    data= df.loc[df['Gender']=='M',['Score']]
)

ax1.title.set_text('Female boxplot')
ax2.title.set_text('Male boxplot')

plt.show()


# In[87]:


df = pd.read_excel('datasets/Canada.xlsx',
                  sheet_name = 'Canada by Citizenship',
                  skiprows = range(20),
                  skitpfooter = 2,
                  engine ='openpyxl'
                  )
df.head(2)


# In[88]:


df.set_index('OdName',inplace= True)


# In[91]:


df.index.name = None
df.head(2)


# In[92]:


df.columns


# In[94]:


df.columns = list(map(str,df.columns))
df.columns


# In[95]:


years = list(map(str,range(1980,2014)))
years


# In[96]:


haiti = df.loc['Haiti', years]
haiti.head(3)


# In[105]:


plt.style.available #estilos disponibles


# In[103]:


mpl.style.use('ggplot')


# In[106]:


x = haiti.plot()
plt.ylabel('Numer of Immigrants')
plt.xlabel('Years')
plt.title('Immigration from Haiti to Canada')


# In[107]:


dfci = df.loc[['China','India'],years]
dfci


# In[110]:


x = dfci.plot(kind='line')


# In[111]:


dfci= dfci.transpose()
dfci


# In[112]:


x = dfci.plot(kind='line')


# In[ ]:




