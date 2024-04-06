from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpFunc import get_page
from mysql_connector import *


    
def scrape(keyword,website,a,host,user,password):

    #keyword = 'iphone 14' #wirte a TAC file to find
    #website = 'https://www.amazon.ca/s?k=' #write a csv file to loop through
    webKey = website + keyword
    driver = webdriver.Chrome()
    driver.get(webKey)
    driver.maximize_window()




    # links stores the hyperlinks that matches the products
    links = []
    count = []
    texts = []

    time.sleep(2)
    if a == 1:
        product_name = driver.find_elements(By.XPATH, "//span[@class = 'a-size-base-plus a-color-base a-text-normal']") #Amazon
    else:
        product_name = driver.find_elements(By.XPATH, "//h4[@class = 'three-line-ellipsis mb-2 flex-col text-xs font-bold leading-5 text-gray-700 hover:text-blue-500 sm:text-sm']")



    word1 = 'case'
    word2 = 'protector'
    word3 = 'charg'

    cnt = 0

    for item in product_name:
        text = item.text.lower()
        cnt = cnt+1
        if keyword in text and not any(word in text for word in [word1, word2, word3]): # still need to 過濾 iphone mini,pro balabala
            count.append(cnt)
            texts.append(text)
            if a == 1:
                link_path = driver.find_element(By.XPATH, f"(//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'])[{cnt}]") 
            else:
                link_path = driver.find_element(By.XPATH, f"(//a[@class = 'relative flex cursor-pointer flex-col rounded-md bg-white p-3 xxs:p-4 xs:p-5'])[{cnt}]") 
            link = link_path.get_attribute('href')
            links.append(link)



    list = get_page(count, links,driver,texts,a)


    connection = connect_to_database(host, user, password,'mydatabase')
    create_database(connection, 'mydatabase')

    create_table(connection, 'mytable', {'name': "VARCHAR(255)", 'price':"FLOAT", 'phone_condition': "VARCHAR(255)", 'color': "VARCHAR(255)", 'storage': "FLOAT",'seller_info': "VARCHAR(255)", 'ratings': "FLOAT"})
    for dic in list:
        insert_data(connection, 'mytable', dic)

    max_column(connection, 'mytable', 'price')
    average_column(connection, 'mytable', 'price')
    min_column(connection, 'mytable', 'price')



    close_connection(connection)


        
    time.sleep(5)
    driver.quit()








