from web_scraping import scrape
from mysql_connector import *

# Please put in the phone model 

keyword = 'iphone 14'

# Please insert your MySQL credentials
host = #########
user = #########
password = ##########


website1 = 'https://www.amazon.ca/s?k='
website2 = 'https://reebelo.ca/search?query='
scrape(keyword, website1, 1, host, user, password)
scrape(keyword, website2, 2, host, user, password)


connection = connect_to_database(host, user, password,'mydatabase')
max_column(connection, 'mytable', 'price')
average_column(connection, 'mytable', 'price')
min_column(connection, 'mytable', 'price')
close_connection(connection)

