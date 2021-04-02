# web-scraping-challenge - Mission to Mars
Challenge is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page


## Overview

Web Scraping Challenge Assignment - Scraping multiple sites using: Splinter for automation for accessing and navigating sites, BeautifulSoup to read the html, and Flask/Python to drive the application.  

* Included in this repository is 1 Folder, with a standard Flask file structure:  
   
  * [Code:](Code) Contains Jupyter notebook for original development of the scraping code, and 2 Python apps that drive the flask application.  
  
  * [Templates:](Code/templates) Contains the index.html landing page where all the scraped content is consolidated.   
  
  * [CSS:](Code/static/css) Contains css style sheet to format the landing page above.  

## Files

* [Pages:](Pages)

  * [Landing Page:](Pages/index.html) - Starting point for the site with navbar and image links to other pages.  

  * [CSS Styles:](Pages/V4Style.css) - Bootstrap Version 4 style sheet for the site.  

  * [Comparison Page](Pages/comparisons.html) - Shows all the measurement images on one page with clickable images.  Highlights which one is active in thumbnails.

  * [Data Table Page](Pages/table.html) - Scrollable, responsive table with 10 columns of data.  

  * [Temperature Page](Pages/temperature.html) - Temperature vs latitude - image, observation info and links to the other measurement pages. 

  * [Humidity Page](Pages/humidity.html) - Humidity % vs latitude - image, observation info and links to the other measurement pages. 
 
  * [Cloudiness Page](Pages/cloud.html) - Cloudiness % vs latitude - image, observation info and links to the other measurement pages. 

  * [Wind Page](Pages/wind.html) - Wind Speed vs latitude - image, observation info and links to the other measurement pag
