#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

a = np.array([1,2,3])

a


# In[5]:


type(a)


# In[6]:


np.shape(a)


# In[7]:


a[1]


# In[42]:


b = np.array([[1,2,3],
             [4,5,6],
            [7,8,9]
             ])


# In[43]:


b


# In[44]:


b.shape


# In[45]:


c = np.zeros((2,3))
c


# In[46]:


d = np.ones((4,2))
d


# In[47]:


f = np.full((5,2),7)
f


# In[48]:


b


# In[49]:


g=b[1:,1:]
g


# In[64]:


g2 = b[0:2,0:2]
g2


# In[65]:


b


# In[66]:


g


# In[67]:


g2


# In[70]:


g[1,1] = 2021


# In[71]:


g


# In[72]:


b


# In[73]:


b[1,1]=5050


# In[74]:


g


# In[78]:


x = np.array([
    [1,2],
    [3,4]
],
dtype = np.float64)

y = np.array([
    [5,6],
    [7,8]
],
dtype = np.float64)

print('La matriz x es: \n',x)
print('La matriz y es: \n',y)


# In[80]:


print('sum of matrix \n{} y \n{} is \n{} '.format(x,y,x+y))


# In[81]:


print(np.add(x,y))


# In[82]:


comp = x+y == np.add(x,y)
comp


# In[83]:


print(np.array_equal(x+y,np.add(x,y)))


# In[87]:


print(np.array_equal(x-y,np.subtract(x,y)))


# In[88]:


x*y


# In[89]:


np.sum(x,axis = 1)


# In[90]:


x


# In[91]:


np.sum(x,axis=0)


# In[ ]:




