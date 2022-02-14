#!/usr/bin/env python
# coding: utf-8

# # Python for analysis of Indian IPO in 2021 
# - Abhijay Rane 

# In[2]:


#for mathematical computation
import numpy as np
import pandas as pd
import scipy.stats as stats


# In[3]:


#for data visualization
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from matplotlib.pyplot import figure


# In[4]:


pwd


# In[5]:


df = pd.read_csv("abhijay_IPO.csv", encoding='latin-1')
df.head()


# In[6]:


df.info()
df.describe()


# In[7]:


f,ax = plt.subplots(figsize=(15,8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", ax=ax)
plt.show()


# In[8]:


date = df.Date.str.split('-', expand =True)
df['year'] = date[2]
df['month'] = date[1]
df['day'] = date[0]

df.year = pd.to_numeric(df.year)
df.month = pd.to_numeric(df.month)
df.day = pd.to_numeric(df.day)


# In[9]:


df.head()


# In[10]:


fig1 = px.pie(df, names='year')
fig1.show()


# In[11]:


fig2 = px.pie(df, names='month')
fig2.show()


# In[12]:


#IPO listed in 2021 
a = df[df['year'] == 21]
a


# In[13]:


#word cloud to display the most prominent or frequent words in a body of text.
from wordcloud import WordCloud
wordCloud = WordCloud().generate(' '.join(df.IPO_Name))

plt.figure(figsize=(15,10))
plt.axis('off')
plt.imshow(wordCloud, interpolation='bilinear')
plt.show()


# In[81]:


#Top gainers in Percentage at the time of Listing
top_gainer = df.groupby('IPO_Name').sum().sort_values('Listing_Gains(%)', ascending=False).head(20)
top_gainer = top_gainer.reset_index()
top20 = px.bar(x='IPO_Name', y ="Listing_Gains(%)", data_frame=top_gainer)
top20.update_traces(marker_color='green')
top20.show()


# In[72]:


x = df[df['IPO_Name'] == 'Sigachi Ind']
x
#The issued price of this IPO was Rs. 163. It opened at Rs. 575 and closes at Rs. 603.75.


# In[82]:


#Top Losers in Percentage at the time of Listing.
top_loser = df.groupby('IPO_Name').sum().sort_values('Listing_Gains(%)', ascending=True).head(20)
top_loser = top_loser.reset_index()
losers20 = px.bar(x='IPO_Name', y ="Listing_Gains(%)", data_frame=top_loser)
losers20.update_traces(marker_color='red')
losers20.show()


# In[84]:


y = df[df['IPO_Name'] == 'VKS Projects']
y
#listing gain= -97.15%, issue_open= 55.8, listing_close=1.57 


# In[91]:


#finding IPO size of company (in Rs crores)
issue_size = df.groupby('IPO_Name').sum().sort_values('Issue_Size(crores)', ascending=False).head(20)
issue_size = issue_size.reset_index()
ipo_size = px.bar(x='IPO_Name', y ="Issue_Size(crores)", data_frame=issue_size)
ipo_size.update_traces(marker_color='black')
ipo_size.show()

