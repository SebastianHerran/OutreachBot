#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options


# ### Extract Facebook links from company webpages

# In[2]:


def selenium_extract_face_link(url):
    global driver
    options_chrome = Options()
    options_chrome.add_argument("headless")
    driver.get(url)
    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, facebook_css)))
    empresa = driver.page_source
    soup_emp = BeautifulSoup(empresa, 'lxml')
    driver.quit()
    return soup_emp


# In[3]:


def RodoBot_extract_fbs(urls):   
    feisbucs=[]
    facebook_css = '[href*="facebook.com/"]:not([href*="facebook.com/sharer"])'
    global driver
    for url in urls:
        try:
            empresa = requests.get(url)
            soup_emp = BeautifulSoup(empresa.content, 'lxml')
            face_link= soup_emp.select(facebook_css)
            
            if len(face_link) > 0: feisbucs.append(face_link[0]['href'])
            else: raise Exception("No Facebook link found")
        except:
            try:
                face_link= selenium_extract_face_link(url).select(facebook_css) 
                feisbucs.append(face_link[0]['href'])
            except:
                try:
                        face_link= selenium_extract_face_link(url).select(facebook_css) 
                        feisbucs.append(face_link[0]['href'])
                except:
                        feisbucs.append('')
    return feisbucs


# ### Outreach Bot

# In[4]:


def OutreachBot(urls):    
    feisbucs = RodoBot_extract_fbs(urls)

    links = pd.DataFrame(zip(urls,feisbucs), columns=['Company Site','Facebook'])
    
    return links


# ### Input

# In[5]:


input_file = os.listdir(os.path.dirname(os.path.abspath('__file__'))+'\\Input')
df_input = pd.read_csv(os.path.dirname(os.path.abspath('__file__'))+'\\Input\\'+input_file[0])


# ### Output

# In[8]:


df_output = OutreachBot(df_input.iloc[:,0])
print('Done! The Output File is now on the Output Folder')
df_output.to_csv(os.path.dirname(os.path.abspath('__file__'))+'\\Output\\'+f'Output-{input_file[0]}.csv')


# In[10]:


df_output


# In[ ]:




