# web-scraping-challenge - Mission to Mars
Challenge is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page


## Overview

Web Scraping Challenge Assignment - Scraping multiple sites using: Splinter for automation for accessing and navigating sites, BeautifulSoup to read the html, and Flask/Python to drive the application.  

* Included in this repository is 1 Folder, with a standard Flask file structure:  
   
  * [Code:](Code) Contains Jupyter notebook for original development of the scraping code, and 2 Python apps that drive the flask application.  
  
  * [Templates:](Code/templates) Contains the index.html landing page where all the scraped content is consolidated.   
  
  * [CSS:](Code/static/css) Contains css style sheet to format the landing page above.  


## Files

* [Code:](Code)

  * [Jupyter Notebook "mission_to_mars":](Code/mission_to_mars.ipynb) Scrapes 4 sites for text, images and tables and creates dictionary of all the data that is inserted into Mongo collection. 

  * [Python scraping function "scrape_mars":](Code/scrape_mars.py) callable python version of the above. Scrapes 4 sites for text, images and tables and creates dictionary of all the data that is inserted into Mongo collection. 

  * [Flask / Python app "mars_app":](Code/mars_app.py) Python app that runs the application, with main and scraping routes, and renders the landing page.  

  * [Landing Page:](Code/templates/index.html) Starting point for the site with button that initiates the scraping activity.  Displays thescraped information. 

  * [CSS Styles:](Code/static/css/style.css) Bootstrap Version 4 style sheet for the site.  

   