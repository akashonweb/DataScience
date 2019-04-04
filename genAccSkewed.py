#!/usr/bin/env python
# coding: utf-8

# In[54]:


print("Importing dependencies....")
import pandas as pd
import numpy
from math import sqrt
from statistics import mean
import random
from dateutil import parser


# In[55]:


print("Ensure .csv is kept at same directory where source is kept")
print("Reading file....This may take a while")
df=pd.read_csv("accelerations.csv")
print("File loaded....")


# In[56]:


skew_fac=.25
print("Enter degree of skewness......\n\n\tMinimum-0(0% skewed data)\n\tMaximum-1(100 % skewed data)\n\tDefault is set to .25 (25% skewed data)\n\nEnter [0.25] to continue with default\n")
skew_fac=input("Enter skewness factor : ")


# In[57]:


print("Processing CSV File....")
trip_id=df.trip_id.tolist()
x_val=df.x_value.tolist()
y_val=df.y_value.tolist()
z_val=df.z_value.tolist()


# In[58]:


resultant = [x + y + z for x, y,z in zip(x_val, y_val,z_val)]


# In[59]:


df['resultant']=resultant
resultant_norm=[]
df_unwanted= pd.DataFrame()
df_unwanted= df[ df['resultant'] == 0 ]
df=df.drop(df_unwanted.index, axis=0)
resultant_norm=df['resultant']
iter=len(resultant_norm)


# In[60]:




# In[61]:


print("Analysing information from CSV file....")

dictoflist_x,dictoflist_y,dictoflist_z={},{},{}
list=[]
j=0;
for i in df['trip_id'].unique():
    #for x
    list=df['x_value'][df['trip_id']==i]
    dictoflist_x[i]=list
    #for y
    list=df['y_value'][df['trip_id']==i]
    dictoflist_y[i]=list
    #for z
    list=df['z_value'][df['trip_id']==i]
    dictoflist_z[i]=list


# In[62]:


skew_fac=pd.to_numeric(skew_fac, errors='ignore')
samples=skew_fac*iter
samples=round(samples)
samples=samples.astype(int)
list_iter=[0] * samples
skewindices=[]
skewindices=random.sample(range(0,iter),len(list_iter))


# In[72]:


print("Creating synthetic data....")
xgen,ygen,zgen=[],[],[]
x1,y1,z1=0,0,0
j=0
h=0
k=0
for i in df['trip_id'].unique():
    
    max_x=max(dictoflist_x.get(i))
    min_x=min(dictoflist_x.get(i))
    max_y=max(dictoflist_y.get(i))
    min_y=min(dictoflist_y.get(i))
    max_z=max(dictoflist_z.get(i))
    min_z=min(dictoflist_z.get(i))
    sampleresultant=[]
    sampleresultant=df['resultant'][df['trip_id']==i].tolist()
    
    for j in range(len(sampleresultant)):
            x1=random.uniform(min_x,max_x)
            y1=random.uniform(min_y,max_y)
            z1=random.uniform(min_z,max_z)
            sum=x1+y1+z1
            x1=(x1/sum)*sampleresultant[j]
            y1=(y1/sum)*sampleresultant[j]
            z1=(z1/sum)*sampleresultant[j]
            xgen.append(round(x1,5))
            ygen.append(round(y1,5))
            zgen.append(round(z1,5))


# In[73]:


for j in skewindices:
    xgen[j]=round(random.uniform(-1,1),5)
    ygen[j]=round(random.uniform(-1,1),5)
    zgen[j]=round(random.uniform(-1,1),5)


# In[74]:


print("Creating dataframe schema....")
df_generated= pd.DataFrame()
df_generated['acceleration_id']=df['acceleration_id']
df_generated['trip_id']=df['trip_id']
df_generated['x']=xgen
df_generated['y']=ygen
df_generated['z']=zgen


# In[75]:


data=pd.date_range(start='3/24/2019', periods=iter, freq='S')


# In[76]:


df_generated['timestamp']=data


# In[80]:


print("Schema created....")
print("Copying dataframe to CSV file....")
df_generated.to_csv("generated_accelerations.csv",index=False)
print("Created generated_accelerations.csv at same directory")


# In[ ]:




