#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')

    


# In[8]:


from bs4 import BeautifulSoup
import requests


# In[9]:


#Answer 1


# In[10]:


page1= requests.get ("https://en.wikipedia.org/wiki/Main_Page")


# In[11]:


soup1= BeautifulSoup (page1.content)
soup1


# In[16]:


header1= []
for i in soup1.find_all ('span', class_ = "mw-headline"):
   header1.append(i.text)
       


# In[17]:


header1


# In[18]:


import pandas as pd1
df1 = pd1.DataFrame({'Header': header1})


# In[19]:


df1


# In[20]:


#answer 2


# In[21]:


page2= requests.get ("https://presidentofindia.nic.in/former-presidents.htm")


# In[22]:


soup2= BeautifulSoup (page2.content)


# In[129]:


name2= []
for i in soup2.find_all ('div', class_ ="presidentListing"):
    name2.append (i.text.split ('|') [0])


# In[130]:


name2


# In[31]:


import pandas as pd2
df2= pd2.DataFrame ({'Name and years of office': name2})


# In[32]:


df2


# In[33]:


#Answer 3


# In[71]:


page4= requests.get("https://www.cnbc.com/world/?region=world")


# In[72]:


soup4= BeautifulSoup (page4.content)


# In[73]:


soup4


# In[74]:


headline= []
for j in soup4.find_all ('a', class_ = "LatestNews-headline"):
    headline.append(j.text)


# In[75]:


headline


# In[76]:


time= []
for k in soup4.find_all ('time', class_ = "LatestNews-timestamp"):
    time.append(k.text)


# In[77]:


time


# In[146]:


import pandas as pd4
df4 = pd4.DataFrame({'Headline': headline , 'Time': time})
df4


# In[85]:


page5= requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")


# In[86]:


soup5= BeautifulSoup (page5.content)


# In[87]:


pt= []
for w in soup5.find_all ('h2', class_ = "sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    pt.append(w.text)


# In[88]:


pt


# In[89]:


authors= []
for x in soup5.find_all ('span', class_ = "sc-1w3fpd7-0 dnCnAO"):
    authors.append(x.text)


# In[90]:


authors


# In[144]:


import pandas as pd5
df5 = pd5.DataFrame({'Paper Title': pt , 'Authors': authors})


# In[145]:


df5


# In[95]:


page6= requests.get ("https://www.dineout.co.in/delhi-restaurants/buffet-special")


# In[96]:


soup6= BeautifulSoup (page6.content)


# In[97]:


restnam= []
for o in soup6.find_all ('a', class_ = "restnt-name ellipsis"):
    restnam.append(o.text)


# In[98]:


restnam


# In[103]:


cuisine= []
for q in soup6.find_all ('span' , class_= "double-line-ellipsis"):
    cuisine.append (q.text.split ('|') [1])


# In[104]:


cuisine


# In[107]:


loc= []
for p in soup6.find_all ('div', class_="restnt-loc ellipsis"):
    loc.append (p.text)


# In[108]:


loc


# In[109]:


ratings= []
for r in soup6.find_all ('div', class_="restnt-rating rating-4"):
    ratings.append (r.text)


# In[110]:


ratings


# In[113]:


url= []
for s in soup6.find_all ('img', class_="no-img"):
    url.append (s.get ('data-src'))


# In[114]:


url


# In[115]:


import pandas as pd6
df6 = pd6.DataFrame({'Restaurant Name': restnam , 'Cuisine': cuisine, 'Location': loc , 'Ratings': ratings , 'Image URL': url})


# In[116]:


df6


# In[ ]:




