from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import pymongo
import io

# executable_path = {'executable_path': ChromeDriverManager().install()}
executable_path = {'executable_path': 'chromedriver.exe'} # Ed needs this to run on his PC
browser = Browser('chrome', **executable_path, headless=False)

# --- 
# # Step 1 - Scrape the Sites for info
# --- 
# ### Part 1-1 - Scrape the NASA Mars News Site for the latest News Title and Paragraph Text
# ---

# Open browser to scrape the Nasa Mars News Site and collect the latet News Title and Paragraph Text. 
# URL = https://mars.nasa.gov/news/
browser.visit('https://mars.nasa.gov/news/')

# pause for brower to open
time.sleep(1)

# Pull in the HTML from the page
html = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) # if need to see what was pulled

# Scan and pull the content_title div
news_title_list = soup.find_all('div', class_='content_title')

# Pull the text from the second item, "1" which is the title
news_title = news_title_list[1].text
print(news_title)

# Scan and pull the article_teaser_body div
news_paragraph_list = soup.find_all('div', class_='article_teaser_body')

# Pull the text from the first item, "1" which is the short paragraph
news_p = news_paragraph_list[0].text
print(news_p)

# ---
# ### Part 1-2 - Scrape the JPL Mars Space Images for Featured Image
# ---

# Open browser to scrape the JPL Site and collect the items and images 
# URL = https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

# pause for brower to open
time.sleep(1)


# Pull in the HTML from the page
html = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) # if need to see what was pulled

# Scan and pull the first SearchResultCard div
jpl_small_images_list = soup.find('div', class_='SearchResultCard')

# Pull the 'href' item which is what must be 'clicked' to get to next page
jpl_small_image = jpl_small_images_list.a['href']
print(jpl_small_image)

# Call browser to 'click' on the small image to get to the large one
browser.click_link_by_href(jpl_small_image)

# pause for brower to open
time.sleep(1)

# Pull in the HTML from the secondary page
html = browser.html

# Parse this new HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) # if need to see what was pulled

# Scan and pull the BaseImagePlaceholder div
jpl_large_images_list = soup.find_all('div', class_='BaseImagePlaceholder')
# print(jpl_large_images_list)

# pull the url from the img data-src attribute for 1st "0" item
featured_image_url = jpl_large_images_list[0].img["data-src"]
print(featured_image_url)

# ---
# ### Part 1-3 - Scrape the Mars Facts page for the Mars Facts Table
# ---

# Use Pandas to scrape the Space-Facts.com site for the data table on mars 
# url = "https://space-facts.com/mars/"
url = "https://space-facts.com/mars/"

# This is the Pandas method to pull all the tables from the page
tables = pd.read_html(url)
# tables

# The Mars table is the first "0" table on the page...
mars_table = tables[0]

# Per the requrested format, rename the columns...
mars_table.rename(columns={0:"Description",1:"Mars"},inplace= True)

# and rename the index
mars_table.set_index("Description",inplace=True)

# Use the StringIO function to put into a string
str_io = io.StringIO()

mars_table.to_html(buf=str_io, classes='table')

mars_table_html_string = str_io.getvalue()
# print(mars_table_html_str)

# ---
# ### Part 1-4 - Scrape the Astrogeology site for High resolution Mars hempsphere pictures (4)
# ---

# Scrape the Astrogeology Site and collect the items and images 
# breaking up the given url into 2 pieces since just the top portion is needed later
# Complete URL is: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# Break URL into pieces and combine for first search
base_url = 'https://astrogeology.usgs.gov/'
search_adder = 'search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

# browse the url
browser.visit(base_url + search_adder) 

# pause for brower to open
time.sleep(1)

# Pull in the HTML from the page
html = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify()) # if need to see what was pulle

# create a list of all the image items
image_items_list = soup.find_all('div', class_='item')

# iterate over the list of images to click to the full image and pull in the url

# create list to hold the image dictionary entries
hemisphere_image_urls = []

for item in image_items_list:
    # get the title, but need to strip off "enhanced" from the end
    h_title_long = item.div.a.h3.text
    h_title = h_title_long.rsplit(' ', 1)[0]
    # print(h_title)
    
    # get the partial link, which needs the base_url added
    h_link_end = item.a['href']
    # print(h_link)
    
    # create the full link and go there with the browser
    browser.visit(base_url + h_link_end) 
    #  Pause for it to render
    time.sleep(1)
    
    # Pull in the HTML from the page that has the full .jpg
    html = browser.html
    
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # find the image item
    mars_large_image = soup.find('div', class_='wide-image-wrapper')
    
    # pull the href for the full image
    mars_large_image_info = mars_large_image.div.ul.li.a["href"]
    
    # append the image and name to the list of urls for hemisphere images 
    hemisphere_image_urls.append({"title":h_title,"img_url":mars_large_image_info})

# print(hemisphere_image_urls)

# ---
# ### Part 1-5 - Clean up browser and any other housekeeping
# ---
browser.quit()

# ---
# ### Part 1-6 - Create dictionary and store the scraped data into the dictionary to pass back when this is put into python script as function scrape
# ---

# set up dictionary to pass values back to calling program when this is an app
mars_dictionary = []
mars_dictionary = {
    'news_title': news_title,
    'news_p': news_p,
    'featured_image_url': featured_image_url,
    'mars_table_html_string': mars_table_html_string,
    'hemisphere_image_urls' : hemisphere_image_urls    
}
print(mars_dictionary)
