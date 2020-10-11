#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_excel(r'C:\dz\Looks_Data.xlsx')


# In[4]:


df.shape


# In[6]:


df.head()


# In[7]:


df.dtypes


# In[41]:


df.groupby('product_id').product_id.count() #сколько раз встретился тот или иной product


# In[27]:


#сортировка по времени создания луков
ndf = df.sort_values(by='look_created_on', ascending=True)
ndf.groupby(['product_id','look_id']).head()


# In[28]:


#надо посчитать сколько раз встретился тот или иной  лук, необходимо удалить все текоторые в сумме встречались > 15 раз
gdf = ndf.groupby('look_id').count() #считаю сколько раз какой продакт встретился
needed_id = gdf.loc[gdf['id'] <= 15].index #выделяю те, что встретились <16 раз
df1 = ndf.set_index('look_id').loc[needed_id]#фильтрую по этому условию


# In[29]:


# удаляю повторяющиеся луки, соответственно остаются наиболее ранние и получаем наш топ наиболее ранних луков (15<=) 
df1.drop_duplicates('id')


# In[ ]:




