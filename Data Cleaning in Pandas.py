#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
df=pd.read_excel(r"C:\Users\PC\Desktop\DATA ANALYSIS\Pandas Tutorials\Customer Call List.xlsx")
df


# In[35]:


df=df.drop_duplicates()
df


# In[36]:


#Dropping Columns
df=df.drop(columns='Not_Useful_Column')
df


# In[41]:


df['Last_Name']=df['Last_Name'].str.strip('._/')


# In[42]:


df


# In[53]:


#cleaning phone numbers

df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
df['Phone_Number']=df['Phone_Number'].apply(lambda x:str(x))
df['Phone_Number']=df['Phone_Number'].apply(lambda x:x[0:3]+'-'+x[3:6]+'-'+x[6:10])
df['Phone_Number']=df['Phone_Number'].str.replace('nan--','')
df['Phone_Number']=df['Phone_Number'].str.replace('Na--','')
df


# In[54]:


df


# In[58]:


#splitting address
df[['Street_Address','State','Zip_code']]=df['Address'].str.split(',',2,expand=True)
df


# In[61]:


#Cleaning Paying Customer
df['Paying Customer']=df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer']=df['Paying Customer'].str.replace('No','N')
df


# In[62]:


#Cleaning Paying Customer
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact']=df['Do_Not_Contact'].str.replace('No','N')
df


# In[63]:


#Removing Null Values
df=df.fillna('')
df


# In[66]:


#Dropping Do Not call Contacts
for x in df.index:
    if df.loc[x,'Do_Not_Contact']=='Y':
        df.drop(x,inplace=True)
df


# In[74]:


#Dropping customers with no numbers
for x in df.index:
    if df.loc[x,'Phone_Number']=='--':
        df.drop(x,inplace=True)
df


# In[75]:


df=df.reset_index(drop=True)
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




