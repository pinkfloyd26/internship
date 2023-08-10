#!/usr/bin/env python
# coding: utf-8

# In[27]:


get_ipython().system('pip install selenium')


# In[28]:


import selenium


# In[29]:


from selenium import webdriver


# In[30]:


import pandas as pd


# In[31]:


from selenium.webdriver.common.by import By


# In[32]:


import warnings
warnings.filterwarnings ('ignore')


# In[33]:


# Answer 1


# In[34]:


driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")


# In[35]:


designation= driver.find_element (By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')


# In[36]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys ('Bangalore')


# In[37]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[38]:


job_title=[]
job_location=[]
company_name=[]
job_experience=[]


# In[41]:


#Titles
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags [0:10]:
    title=i.text
    job_title.append(title)
    
    
#location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags [0:10]:
    location=i.text
    job_location.append(location)
    
    
#company name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags [0:10]:
    company=i.text
    company_name.append(company)
    
    
#Job Experience
experience_tags= driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in company_tags [0:10]:
    experience=i.text
    job_experience.append(experience)


# In[42]:


print (len(job_title) , len(job_location) , len(company_name) , len(job_experience))


# In[43]:


import pandas as pd
df=pd.DataFrame ({'Ttiles':job_title , 'Location':job_location , 'Company': company_name , 'Experience': job_experience})
df


# In[44]:


# Answer 2


# In[45]:


driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")


# In[46]:


designation= driver.find_element (By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[47]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys ('Bangalore')


# In[48]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[49]:


job_title=[]
job_location=[]
company_name=[]
job_experience=[]


# In[50]:


#Titles
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags [0:10]:
    title=i.text
    job_title.append(title)
    
    

#location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags [0:10]:
    location=i.text
    job_location.append(location)
    
    
#company name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags [0:10]:
    company=i.text
    company_name.append(company)
    
    
#Job Experience
experience_tags= driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in company_tags [0:10]:
    experience=i.text
    job_experience.append(experience)

    


# In[51]:


print (len(job_title) , len(job_location) , len(company_name) , len(job_experience))


# In[52]:


import pandas as pd
df=pd.DataFrame ({'Ttiles':job_title , 'Location':job_location , 'Company': company_name , 'Experience': job_experience})
df


# In[53]:


#Answer 3


# In[54]:


driver = webdriver.Chrome()

driver.get("https://www.naukri.com/")


# In[55]:


designation= driver.find_element (By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[56]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys ('Delhi/NCR')


# In[57]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[58]:


filter_36=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[5]/div[2]/div[2]/label/p/span[1]")
filter_36.click()


# In[59]:


job_title=[]
job_location=[]
company_name=[]
job_experience=[]


# In[61]:


#Titles
title_tags=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in title_tags [0:10]:
    title=i.text
    job_title.append(title)
    
    

#location
location_tags=driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft locWdth"]')
for i in location_tags [0:10]:
    location=i.text
    job_location.append(location)
    
    
#company name
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags [0:10]:
    company=i.text
    company_name.append(company)
    
    
#Job Experience
experience_tags= driver.find_elements(By.XPATH,'//span[@class="ellipsis fleft expwdth"]')
for i in company_tags [0:10]:
    experience=i.text
    job_experience.append(experience)

    


# In[62]:


import pandas as pd
df=pd.DataFrame ({'Ttiles':job_title , 'Location':job_location , 'Company': company_name , 'Experience': job_experience})
df


# In[63]:


#Answer 4


# In[144]:


driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")


# In[147]:


search_field= driver.find_element (By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/header/div[1]/div[2]/form/div/div/input")
search_field.send_keys('Sunglasses')


# In[142]:


brand=[]
product_description=[]
price=[]


# In[148]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags [0:10]:
    brands=i.text
    brand.append(brands)


# In[149]:


product_description_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_description_tags [0:10]:
    description=i.text
    product_description.append(description)


# In[150]:


price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
for i in price_tags [0:10]:
    prices=i.text
    price.append(prices)


# In[164]:


print(len(brand), len(product_description) , len(price))


# In[153]:


#Answer 7 


# In[154]:


driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")


# In[155]:


search_field= driver.find_element (By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search_field.send_keys('Laptops')


# In[156]:


search_button=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search_button.click()


# In[158]:


i7_button=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[7]/span[13]/li/span/a/span")
i7_button.click()


# In[159]:


title=[]
ratings=[]
price=[]


# In[165]:


title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags [0:10]:
    titles=i.text
    title.append(titles)


# In[166]:


rating_tags=driver.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]')
for i in rating_tags [0:10]:
    rating=i.text
    ratings.append(rating)


# In[167]:


price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
for i in price_tags [0:10]:
    prices=i.text
    price.append(prices)


# In[168]:


print(len(title) , len(ratings), len(price))


# In[ ]:


#Answer 8 


# In[104]:


driver = webdriver.Chrome()

driver.get("http://www.azquotes.com/")


# In[105]:


top_quotes=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a")
top_quotes.click()


# In[106]:


quotes=[]
authors=[]
type_quotes=[]


# In[108]:


#Quotes
quote_tags=driver.find_elements(By.XPATH,'//a[@class="title"]')
for i in quote_tags:
    quote=i.text
    quotes.append(quote)


# In[109]:


#Authors
author_tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
for i in author_tags:
    author=i.text
    authors.append(author)


# In[110]:


#type_of_Quotes
type_tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
for i in type_tags:
    types=i.text
    type_quotes.append(types)


# In[111]:


print (len(quote_tags) , len(author_tags) , len(type_tags))


# In[112]:


import pandas as pd
df=pd.DataFrame ({'Quotes':quotes , 'Author':authors , 'Type Of Quote': type_quotes})
df


# In[113]:


#Answer 10 


# In[131]:


driver = webdriver.Chrome()

driver.get("https://www.motor1.com/")


# In[132]:


search=driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input")
search.send_keys ('50 most expensive cars')


# In[133]:


search_icon=driver.find_element(By.XPATH,"/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]")
search_icon.click()


# In[134]:


cars_icon=driver.find_element(By.XPATH,"/html/body/div[10]/div[9]/div/div[1]/div/div/div[2]/div/div[1]/h3/a")
cars_icon.click()


# In[135]:


cars=[]


# In[136]:


car_tags=driver.find_elements(By.XPATH,'//h3[@class="subheader"]')
for i in car_tags:
    car=i.text
    cars.append(car)


# In[137]:


import pandas as pd
df=pd.DataFrame ({'Top 50 Most Expensive Cars':cars})
df


# In[ ]:




