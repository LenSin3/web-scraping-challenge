# Mission To Mars - A Web Scraping Challenge

This objective of this project is to develop a web app that scrapes websites, saves the data in a database and then render the results in a web browser. 

## Step 1 - Scraping

The following tasks were completed in step 1:

- Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.

- Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

- Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

- Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

- Use Pandas to convert the data to a HTML table string.

- Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

## Step 2 - MongoDB and Flask Application

- Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

- Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

- Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.

  - Store the return value in Mongo as a Python dictionary.

- Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

- Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

## Libraries

- Flask-PyMongo
- Beautiful Soup
- Selenium
- Splinter
- Requests
- Pandas
- Time

## Environment and Tools

- Jupyter Notebook Python 3.6 env
- VS Code
- html
- css

## Files

- mission_to_mars.ipynb
- app.py
- mars_table.html
- scrape_to_mars.py
- templates (directory)
   -  index.html
- static
  - style.css








