#!/usr/bin/env python
# coding: utf-8

# In[14]:


print("Importing dependencies....")
import pandas as pd
import numpy
from math import sqrt
from statistics import mean
import random
from dateutil import parser


# In[15]:


print("Ensure .csv is kept at same directory where source is kept")
print("Reading file....This may take a while")
df=pd.read_csv("gyroscopes.csv")
print("File loaded....")


skew_fac=.25
print("Enter degree of skewness......\n\n\tMinimum-0(0% skewed data)\n\tMaximum-1(100 % skewed data)\n\tDefault is set to .25 (25% skewed data)\n\nEnter [0.25] to continue with default\n")
skew_fac=input("Enter skewness factor : ")



# In[16]:


print("Processing CSV File....")
trip_id=df.trip_id.tolist()
x=df.x_value.tolist()
y=df.y_value.tolist()
z=df.z_value.tolist()



# In[17]:


iter=len(trip_id)


# In[18]:


#print(iter)


# In[19]:


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


# In[20]:

skew_fac=pd.to_numeric(skew_fac, errors='ignore')
samples=skew_fac*iter
samples=round(samples)
samples=samples.astype(int)
list_iter=[0] * samples
skewindices=[]
skewindices=random.sample(range(0,iter),len(list_iter))

print("Creating synthetic data....")
xgen,ygen,zgen=[],[],[]
x1,y1,z1=0,0,0
j=0
for i in df['trip_id'].unique():
    
    max_x=max(dictoflist_x.get(i))
    min_x=min(dictoflist_x.get(i))
    max_y=max(dictoflist_y.get(i))
    min_y=min(dictoflist_y.get(i))
    max_z=max(dictoflist_z.get(i))
    min_z=min(dictoflist_z.get(i))
    sampletrips=[]
    sampletrips=df['trip_id'][df['trip_id']==i].tolist()
    
    for j in range(len(sampletrips)):
        x1=round(random.uniform(min_x,max_x),5)
        y1=round(random.uniform(min_y,max_y),5)
        z1=round(random.uniform(min_z,max_z),5)
        xgen.append(x1)
        ygen.append(y1)
        zgen.append(z1)


for j in skewindices:
    xgen[j]=round(random.uniform(-31,22),5)
    ygen[j]=round(random.uniform(-31,55),5)
    zgen[j]=round(random.uniform(-57,51),5)

# In[21]:


print("Creating dataframe schema....")


df_generated= pd.DataFrame()
df_generated['gyroscope_id']=df['gyroscope_id']
df_generated['trip_id']=df['trip_id']
df_generated['x_value']=xgen
df_generated['y_value']=ygen
df_generated['z_value']=zgen


# In[22]:


data=pd.date_range(start='3/6/2019', periods=iter, freq='S')


# In[23]:


df_generated['timestamp']=data
df_generated.head()


# In[25]:


print("Schema created....")
print("Copying dataframe to CSV file....")
df_generated.to_csv("generated_gyroscopes.csv",index=False)
print("Created generated_gyrososcopes.csv at same directory")


# In[ ]:





# In[ ]:





