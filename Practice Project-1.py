#!/usr/bin/env python
# coding: utf-8

#  ML Pratice Project

# # Red Wine Quality

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from warnings import filterwarnings
filterwarnings (action ='ignore')


# Uploading the data

# In[5]:


red_wine=pd.read_csv (r'C:\Users\Chinmay\Downloads\winequality-red.csv')
red_wine.sample(50)


# In[6]:


red_wine.info()


# In[7]:


red_wine.describe()


# Finding null values

# In[8]:


red_wine.isnull().sum()


# In[9]:


red_wine.groupby ('quality').mean()


# # Data Analysis

# In[11]:


sns.countplot (red_wine['quality'])
plt.show


# In[12]:


red_wine['volatile acidity'].plot (kind='box')


# Histogram

# In[13]:


red_wine.hist (figsize=(15,15), bins=100)
plt.show


# # Selecting Feature:

# In[14]:


red_wine.sample(50)


# In[15]:


red_wine ['quality'].unique()


# In[17]:


#If the quality of wine is 7 or above then it is considered good wine
red_wine ['goodquality']= [1 if x>=7 else 0 for x in red_wine ['quality']]
red_wine.sample(50)


# In[18]:


#separating dependent and independent variables
X=red_wine.drop(['quality', 'goodquality'],axis=1)
Y=red_wine['goodquality']


# In[19]:


#looking at the total number of good and bad wine samples
red_wine['goodquality'].value_counts()


# In[20]:


X


# In[21]:


print (Y)


# Splitting the dataset

# In[23]:


from sklearn.model_selection import train_test_split
X_train,X_test, Y_train,Y_test= train_test_split(X,Y,test_size=0.3 , random_state=7)


# Result

# In[25]:


model_res=pd.DataFrame (columns=['Model','Score'])


# Logistic Regression

# In[31]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression() 
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix 
# accuracy score (Y_test, Y_pred) 
model_res.loc[len(model_res)]=['LogisticRegression', accuracy_score(Y_test,y_pred)] 
model_res


# Using KNN

# In[34]:


from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3) 
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score 
# accuracy score (Y_test, Y_pred) 
model_res.loc[len(model_res)]=['KNeighborsClassifier', accuracy_score(Y_test,y_pred)] 
model_res


# Using Support Vector Classifier

# In[36]:


from sklearn.svm import SVC
model = SVC()
model. fit(X_train, Y_train) 
y_pred = model.predict(X_test) 
from sklearn.metrics import accuracy_score 
print("Accuracy Score:", accuracy_score(Y_test, y_pred)) 
model_res.loc [len(model_res)] = ['SVC', accuracy_score(Y_test,y_pred)] 
model_res


# In[37]:


from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='entropy', random_state=7) 
model.fit(X_train,Y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score
print("Accuracy Score:", accuracy_score(Y_test, y_pred)) 
# accuracy score (Y_test, Y_pred) 
model_res.loc[len(model_res)]=['DecisionTreeClasifier', accuracy_score(Y_test,y_pred)] 
model_res


# In[38]:


from sklearn.naive_bayes import GaussianNB
model3 = GaussianNB()
model3.fit(X_train, Y_train) 
y_pred = model3.predict(X_test)

from sklearn.metrics import accuracy_score 
print("Accuracy Score:", accuracy_score(Y_test, y_pred)) 
model_res.loc [len(model_res)] = ['GaussianNB', accuracy_score(Y_test,y_pred)] 
model_res


# In[39]:


from sklearn.ensemble import RandomForestClassifier
model2 = RandomForestClassifier(random_state=1)
model2.fit(X_train, Y_train) 
y_pred = model2.predict(X_test)

from sklearn.metrics import accuracy_score 
print("Accuracy Score:", accuracy_score(Y_test, y_pred)) 
model_res.loc [len(model_res)] = ['RandomForestClassifier', accuracy_score(Y_test,y_pred)] 
model_res


# In[40]:


model_res=model_res.sort_values(by='Score', ascending=False)
model_res


# # Medical Cost Personal Insurance

# In[82]:


from matplotlib import style


# In[83]:


mci=pd.read_csv (r'C:\Users\Chinmay\Downloads\medical_cost_insurance.csv')
mci.sample(50)


# In[84]:


mci.info()


# In[85]:


mci.isnull().sum()


# In[86]:


mci.describe()


# In[48]:


plt.figure (figsize=(5,5))
style.use('ggplot')
sns.countplot(x='sex', data=mci)
plt.title('Gender Distribtion')
plt.show()


# In[87]:


sns.countplot (x='smoker' , data=mci)
plt.title('Smoker')
plt.show()


# In[88]:


plt.figure(figsize=(5,5))
sns.countplot(x='region', data=mci)
plt.title('Region')
plt.show()


# In[89]:


plt.figure(figsize=(5,5))
sns.barplot(x='region' , y='charges' , data=mci)
plt.title('Cost Vs Region')


# In[90]:


plt.figure(figsize=(5,5))
sns.barplot(x='smoker' , y='charges' , data=mci)
plt.title('Charges for Smokers')


# In[91]:


plt.figure(figsize=(5,5))
sns.barplot(x='sex' , y='charges' , hue='smoker', data=mci)
plt.title('Charges for Smokers')


# In[92]:


fig,axes= plt.subplots(1,3,figsize=(15,5),sharey=True)
fig.suptitle('Visualizing Categorical Columns')
sns.boxenplot(x='smoker',y='charges',data=mci, ax=axes[0])
sns.boxenplot(x='sex',y='charges',data=mci, ax=axes[1])
sns.boxenplot(x='region',y='charges',data=mci, ax=axes[2])


# In[93]:


mci[['age','bmi','children','charges']].hist(bins=30, figsize=(10,10), color='blue')


# In[94]:


mci['sex']=mci['sex'].apply({'male':0,'female':1}.get)
mci['smoker']=mci['smoker'].apply({'yes':1,'no':0}.get)
mci['region']=mci['region'].apply({'southwest':1, 'southeast':2,'northwest':3,'northeast':4}.get)
mci.head()


# In[95]:


X=mci.drop(['charges','sex'],axis=1)
Y=mci.charges


# In[96]:


X_train,X_test,Y_train, Y_test=train_test_split(X,Y,test_size=0.3, random_state=42) 
print("X_train shape: ",X_train.shape)
print("X_test shape: ",X_test.shape)
print("Y_train shape: ",Y_train.shape)
print("Y_test shape: ",Y_test.shape)
      


# In[97]:


from sklearn.linear_model import LinearRegression


# In[98]:


linreg=LinearRegression()


# In[99]:


linreg.fit(X_train,Y_train)
pred=linreg.predict(X_test)


# In[100]:


from sklearn.metrics import r2_score


# In[102]:


print("R2 score: ",(r2_score(Y_test,pred)))


# In[103]:


plt.scatter(Y_test,pred)
plt.xlabel('Y test')
plt.ylabel('Y pred')
plt.show()


# In[105]:


data={'age':50 , 'bmi':25 , 'children':2 , 'smoker':0, 'region':2}
index=[0]
cust_df=pd.DataFrame(data,index)
cust_df


# In[106]:


cost_pred=linreg.predict(cust_df)
print("The medical insurance cost of the new patient is:" , cost_pred)


# In[ ]:




