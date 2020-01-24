#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df=pd.read_csv('911.csv')


# In[ ]:


df.info()


# In[ ]:


df.head()


# In[ ]:


df['zip'].value_counts().head()


# In[ ]:


df['twp'].value_counts().head()


# In[ ]:


df['title'].nunique()


# In[ ]:


df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[ ]:


df['Reason'].value_counts()


# In[ ]:


sns.countplot(x=df['Reason'],data=df)


# In[ ]:


type(df['timeStamp'].iloc[0])


# In[ ]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)


# In[ ]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[ ]:


df['Day of Week'] = df['Day of Week'].map(dmap)


# In[ ]:


sns.countplot('Day of Week',data=df,hue='Reason')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:


sns.countplot('Month',data=df,hue='Reason')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[ ]:


byMonth = df.groupby('Month').count()
byMonth.head()


# In[ ]:


byMonth['twp'].plot()


# In[ ]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[ ]:


df['Date']=df['timeStamp'].apply(lambda x: x.date())


# In[ ]:


abc=df.groupby('Date')
abc.count()['twp'].plot()


# In[ ]:


df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[ ]:


df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[ ]:


df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[ ]:


dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()


# In[ ]:


xyz=df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack(level=-1)

xyz.head()


# In[ ]:


sns.heatmap(xyz)


# In[ ]:


sns.clustermap(xyz)


# In[ ]:


xyz=df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack(level=0)

xyz.head()


# In[ ]:


sns.heatmap(xyz)


# In[ ]:


sns.clustermap(xyz)


# In[ ]:




