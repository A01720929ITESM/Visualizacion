#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


air_data = pd.read_csv('datasets/airline_data.csv',
                      encoding='ISO-8859-1',
                      low_memory=False)
air_data.head(2)


# In[3]:


air_data.shape


# In[4]:


data = air_data.sample(n=500,
                      random_state=42)
data.head(2)


# In[5]:


data.shape


# In[8]:


fig=go.Figure(data=go.Scatter(x=data['Distance'],
                             y=data['DepTime'],
                             mode='markers',
                             marker=dict(color='red')
                             )
             )
fig.update_layout(title='Distance vs Departure time',
                 xaxis_title='Distance',
                 yaxis_title='DepTime'
                 )
fig.show()


# In[9]:


line_data=data.groupby('Month')['ArrDelay'].mean().reset_index()


# In[10]:


line_data


# In[12]:


lfig=go.Figure(data=go.Scatter(x=line_data['Month'],
                              y=line_data['ArrDelay'],
                              mode='lines',
                              marker=dict(color='green')
                              )
              )
lfig.show()


# In[14]:


figS= px.sunburst(data,
                 path=['Month','DestStateName'],
                 values='Flights'
                 )
figS.show()


# In[15]:





# In[ ]:




