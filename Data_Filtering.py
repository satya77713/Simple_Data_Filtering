#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
data = {
"Name": ["Rahul", "Priya", "Arjun", "Sneha", "Vikram", "Ananya"],
"Age": [20, 21, 19, 22, 20, 21],
"Department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE"],
"Marks": [85, 92, 76, 88, 55, 95]
}


# In[15]:


df = pd.DataFrame(data)

print(df)


# In[16]:


high_scorers = df[df["Marks"] >= 85]

print(high_scorers)


# In[17]:


lowest_score = df[df["Marks"]<= 60]

print(lowest_score)


# In[23]:


age = df[df["Age"]>= 20]
print(age)


# In[22]:


course = df[df["Department"] == "ECE"]
print(course)


# In[ ]:




