#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
from dash import html
from dash import dcc
from jupyter_dash import JupyterDash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


air_data=pd.read_csv('datasets/airline_data.csv',
                    encoding='ISO-8859-1',
                    low_memory=False)

air_data.head(2)

data = air_data.sample(n=500,
                      random_state=42)
data.head(2)

figS=px.sunburst(data,
                path=['Month','DestStateName'],
                values='Flights'
                )
figS.show()


# In[22]:


app=JupyterDash(__name__)
app.layout=html.Div(children=[html.H1('Airline Dashbord'),
                              html.P('Test'),
                              dcc.Graph(figure=figS)])
if __name__=='__main__':
    app.run_server()


# In[ ]:




