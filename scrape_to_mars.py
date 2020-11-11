from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium import webdriver
import time


def init_browser():
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():

    scraped_data = {}

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    quotes = soup.find_all('div', class_ = 'content_title')

    paragraphs = soup.find_all('div', class_="article_teaser_body")   


    headlines = []
    titles = []
    for quote in quotes:
        
        
        titles.append(quote.text)
        
    for paragraph in paragraphs:
        headlines.append(paragraph.text)
        
    news_title = titles[0]

    news_p = headlines[0]

    scraped_data['news_title'] = news_title
    scraped_data['news_p'] = news_p


    table_url = 'https://space-facts.com/mars/'


    mars_df = pd.read_html(str(table_url))[0]


    mars_df.rename(columns = {0: 'Fact', 1:'Data'}, inplace=True)
    





    mars_df_html = mars_df.to_html(index = False)





    scraped_data['mars_facts'] = mars_df_html



    mars_hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    hemisphere_image_url = [{'title' : 'Cerberus hemisphere', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced#open'},
                       {'title': 'Valles Marineris Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'},
                       {'title': 'Syrtis Major Hemisphere ', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'},
                       {'title': 'Schiaparelli Hemisphere', 'img_url': 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'}]

    scraped_data['hemisphere_image_url'] = hemisphere_image_url

    return scraped_data



    browser.quit()

