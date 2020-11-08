#!/usr/bin/env python
# coding: utf-8

# In[185]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[192]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[145]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)


# In[146]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')

quotes = soup.find_all('div', class_ = 'content_title')

paragraphs = soup.find_all('div', class_="article_teaser_body")   


# In[171]:


headlines = []
titles = []
for quote in quotes:
    
    
    titles.append(quote.text)
    
for paragraph in paragraphs:
    headlines.append(paragraph.text)
    
news_title = titles[0]

news_p = headlines[0]


# ## JPL Mars Space Images - Featured Image

# In[194]:


# image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# browser.visit(image_url)
# browser.find_by_name('FULL IMAGE').click()


# In[190]:


# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')


# In[ ]:





# ## Mars Facts

# In[154]:


import pandas as pd


# In[155]:


table_url = 'https://space-facts.com/mars/'


# In[160]:


mars_df = pd.read_html(str(table_url))[0]


# In[167]:


mars_df.rename(columns = {0: 'Fact', 1:'Data'}, inplace=True)
mars_df


# In[169]:


mars_df_html = mars_df.to_html(index = False)


# In[170]:


mars_df_html


# ## Mars Hemispheres

# In[ ]:


mars_hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[ ]:


hemisphere_image_url = [{'title' : 'Cerberus hemisphere',                         'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced#open'},
                       {'title': 'Valles Marineris Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'},
                       {'title': 'Syrtis Major Hemisphere ', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'},
                       {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'}]


# In[ ]:





# In[151]:


browser.quit()

