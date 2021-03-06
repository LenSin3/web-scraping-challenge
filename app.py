# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_to_mars

# create instance of Flask app
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_DB")


# create route that renders index.html template
@app.route("/")
def index():
    scraped_data = mongo.db.scraped_data.find_one()
    return render_template("index.html", scraped_data = scraped_data)

@app.route("/scrape")
def scrape():
    scraped_data = mongo.db.scraped_data
    scraped_data_list = scrape_to_mars.scrape()
    scraped_data.update({}, scraped_data_list, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
