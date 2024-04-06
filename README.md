# Dynamic Phone Model Scraper
## Description

This is a powerful tool designed to simplify the process of gathering comprehensive information about phone models from Amazon and Reebelo. With this tool, users can input the desired phone model, and the scraper will retrieve and organize all available data from both Amazon and Reebelo, including pricing, ratings, phone condition, and more.

## How to Use

To test the web scraping functionality of this project, follow these steps:

**1.Downlaod all the files**

This includes scrape.py,helpFunc.py, web_scraping.py, Exceptions.py, and mysql_connector.py


**2.Open the scrape.py file and set the keyword**

Locate the keyword variable in the code and assign it the phone model you wish to scrape information for. 

**3.Provide MySQL Credentials**

Replace the placeholders with your MySQL host, username, and password in the appropriate variables to store the scraped data in your database.

**4.Run the Code**

Execute the code to initiate the web scraping process. The program will visit Amazon and Reebelo websites to gather information about the specified phone model.

**5.View Results**

After the scraping is complete, the program will display the average, maximum, and minimum price values for the phone model in the terminal.

