from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium import webdriver
import time


def init_browser():
    
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():

    browser = init_browser()
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
        
    news_title = [title for title in titles]

    news_p = [headline for headline in headlines]

    scraped_data['news_title'] = news_title[1]
    scraped_data['news_p'] = news_p[0]


    table_url = 'https://space-facts.com/mars/'


    mars_df = pd.read_html(str(table_url))[0]


    mars_df.rename(columns = {0: 'Fact', 1:'Data'}, inplace=True)  


    mars_df_html = mars_df.to_html(index = False)


    scraped_data['mars_facts'] = mars_df_html



    mars_hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


    hemisphere_image_url = [{"title" : "Cerberus hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
                       {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
                       {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
                       {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"}]
                     
                       

    scraped_data['hemisphere_image_url'] = hemisphere_image_url

    return scraped_data



    browser.quit()

