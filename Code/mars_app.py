from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()
    # See if we have actual data, or a blank return
    try:
        print(mars_data["hemisphere_image_urls"][0]["img_url"])
    # if a TypeError return we did not get anything and need to create dummy data    
    except TypeError:
        mars_data = []
        hemisphere_image_urls = []
        hemisphere_image_urls.append({"title": "","img_url":""})
        hemisphere_image_urls.append({"title": "","img_url":""})
        hemisphere_image_urls.append({"title": "","img_url":""})
        hemisphere_image_urls.append({"title": "","img_url":""})
        mars_data = {
            'news_title': '(TBD) - Press "Scrape New Data Button for latest information',
            'news_p': '',
            'featured_image_url': '',
            'mars_table_html_string': '',
            'hemisphere_image_urls' : hemisphere_image_urls    
        }
        print("Null entry created")
        
# Return template and data
    return render_template("index.html", mars=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
