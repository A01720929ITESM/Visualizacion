#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')

df= pd.read_excel('datasets/Canada.xlsx',
                 sheet_name='Canada by Citizenship',
                 skiprows=range(20),
                 skipfooter=2,
                 engine='openpyxl')
df.head(2)                  


# In[2]:


df.shape


# In[4]:


years = list(map(str, range(1980,2014)))


# In[5]:


df.columns= list(map(str,df.columns))


# In[7]:


df_t = pd.DataFrame(df[years].sum(axis=0))
df_t.head(2)


# In[8]:


df_t.index=map(float,df_t.index)
df_t.reset_index(inplace=True)
df_t.head(2)


# In[10]:


df_t.columns=['year','total']
df_t.tail(2)


# In[22]:


plt.figure(figsize=(15,10))
sns.set(font_scale=1.5)
sns.set_style('whitegrid')
reg_plot = sns.regplot(x='year',
                      y='total',
                      data=df_t,
                      color='g',
                      marker='+',
                      scatter_kws ={'s':150})

reg_plot.set(xlabel='year',
            ylabel='Total immigration')
reg_plot.set_title('Total immigration to Canada from 1980-2013')

plt.show()


# In[4]:


df = pd.read_csv('datasets/headbrain.csv')
df.head(2)


# In[6]:


a = df['Head Size(cm^3)']
b = df['Brain Weight(grams)']
#print(a)
#print(b)


# In[7]:


np.corrcoef(a,b)


# In[8]:


plt.scatter(a,b,
           c='y',
           label='Data points'
           )
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.legend()
plt.show()


# In[29]:


import statsmodels.api as sm

model = sm.OLS.from_formula('b~a',
                            data=df)

result=model.fit()
result.summary()


# In[9]:


from sklearn import linear_model

lm= linear_model.LinearRegression()
X = pd.DataFrame(df['Head Size(cm^3)'])
Y = pd.DataFrame(df['Brain Weight(grams)'])

model_lm = lm.fit(X,Y)
model_lm


# In[10]:


model_lm.intercept_


# In[12]:


model_lm.coef_


# In[13]:


model_lm.score(X,Y)


# In[15]:


brain_weight = pd.DataFrame([200])
predict_headsize = model_lm.predict(brain_weight)
predict_headsize


# In[17]:


df.plot(kind='scatter',
       x = 'Head Size(cm^3)',
       y = 'Brain Weight(grams)',
       color = 'r')

plt.plot(X,
        model_lm.predict(X),
        linewidth=2,
        color = 'g')
plt.show()


# In[18]:


get_ipython().run_line_magic('ls', "'datasets/'")


# In[20]:


df = pd.read_csv('datasets/nhanes_2015_2016.csv')
df.head(2)


# In[22]:


df.columns


# In[24]:


vars=['BPXSY1','RIDAGEYR','RIAGENDR','RIDRETH1','DMDEDUC2','BMXBMI','SMQ020']
df = df[vars]
df.head(10)


# In[25]:


df = df[vars].dropna()
df.head(10)


# In[27]:


df[vars].corr()


# In[31]:


model = sm.OLS.from_formula('BPXSY1~RIDAGEYR+RIAGENDR',
                           data=df)

result=model.fit()
result.summary()


# In[ ]:




