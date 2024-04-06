from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.support.ui import Select
from Exceptions import find_element

#Amazon 1
#Reebelo 2


    
def get_page(count, links,driver,product_name,a):
    # for loop
    k = 0
    list_of_dicts = []
    
    
    for link in links:
        website = link
        driver.get(website)
        time.sleep(1)
        info = memory(driver,product_name[k],a)
        ratings = get_ratings(driver,a)
        seller_info = get_seller_info(driver,a)
        
        
        for i in range(0,len(info),4):
            # info as dictionary
            person_dict = {'name': product_name[k], 'price': info[i+3], 'phone_condition': info[i], 'color': info[i+1], 'storage':info[i+2],'seller_info': seller_info, 'ratings': ratings}
            list_of_dicts.append(person_dict)
        k = k+1
        
        if (a == 2 and k == 1):
            break
    '''    
    # for only one iteration
    website = links[1]
    driver.get(website)
    info = memory(driver,product_name[1],a)
    print(info)
    ratings = get_ratings(driver,a)
    seller_info = get_seller_info(driver,a)
    
    for i in range(0,len(info),4):
    # info as dictionary
        person_dict = {'name': product_name[0], 'price': info[i+3], 'phone_condition': info[i], 'color': info[i+1], 'storage':info[i+2],'seller_info': seller_info, 'ratings': ratings}
        list_of_dicts.append(person_dict)'''
    
    
    return list_of_dicts
    
    
    
def memory(driver,product_name,a):
  
    # find from xpath
    info = []
    if a == 1:
        memory_name = find_element(driver,By.XPATH, "//tr[@class = 'a-spacing-small po-memory_storage_capacity']//td[@class = 'a-span9']//span")
        

        if memory_name:
            memory_text = str_to_int(memory_name.text)
        else:
            memory_text = None
            
        info = colour(driver,memory_text,product_name,a)
    
    
    # if no use button
    else:

        memory_buttons = driver.find_elements(By.XPATH, "//div[@id = 'e2e-product-storage']//div[@class = 'false']//a") 
        
        for i in range(len(memory_buttons)):
            if 'dash' not in memory_buttons[i].get_attribute('class'):
                memory_buttons[i].click()             
                info = info+ colour(driver,str_to_int(memory_buttons[2].text), product_name,a)
    return info
    
    
    
    
def colour(driver,storage_space,product_name,a):
    info = []
    if a==1:
        colour_name = find_element(driver,By.XPATH, "//tr[@class = 'a-spacing-small po-color']//td[@class = 'a-span9']//span")

        if colour_name:
            colour_text = colour_name.text
        else:
            colour_text = None
            
        info = phone_cond(driver, storage_space,colour_text,product_name,a)
    
    
    else:
        time.sleep(2)
        colour_buttons = driver.find_elements(By.XPATH, "//div[@class = 'flex items-center justify-center']/*[@class= 'h-[50px] w-[50px] xs:h-[26px] xs:w-[26px]']")
        for button in colour_buttons:
            button.click()
            time.sleep(1)
            colour_name = driver.find_element(By.XPATH, '//h5[@class="mb-1 text-[10px] font-bold uppercase text-gray-700 xs:mb-2 lg:font-normal"]//b').text             
            info = info+(phone_cond(driver,storage_space, colour_name, product_name,a))
    return info





            
def phone_cond(driver, storage_space,phone_colour,product_name,a):
    info = []
        
    #use button   
    if a==2:
        cond_buttons = driver.find_elements(By.XPATH, '//div[@id = "e2e-product-condition"]//div[@class = "false"]//a')
        for button in cond_buttons:
            if 'dash' not in button.get_attribute('class'):
                button.click()
                time.sleep(1)
                price = driver.find_element(By.XPATH,"(//h2 [@id = 'e2e-product-price'])[1]")
                info = [button.text,phone_colour, storage_space,str_to_int(price.text)]
                
                
    # from name
    else:
        price = find_element(driver,By.XPATH,"(//span[@class = 'a-price a-text-price a-size-medium']//span)[2]")
        if price:
            price_name = str_to_int(price.text)
        else:
            price_name = None
        keyword = 'renewed'
        if keyword in product_name.lower():
            info = [keyword,phone_colour, storage_space,price_name]
        else:
            info = ["NAN",phone_colour, storage_space,price_name]
    
    return info
            
            
            
    
    
def get_ratings(driver,a):
    if a == 1:
        rating = find_element(driver, By.XPATH,"//span[@data-hook = 'rating-out-of-text']")      
        if rating:
            num = convert_to_float(rating.text)
        else:
            num = None
        
    else:
        rating = find_element(driver, By.XPATH,"//div[@class = 'mr-2 flex']//span") #Reebelo
        
        if rating:
            num = float(rating.text)
        else:
            num = None
        
        
    
    return(num)
    
def get_seller_info(driver,a):
    if a == 1:
        
        seller_info = find_element(driver, By.XPATH, "//div[@offer-display-feature-name = 'desktop-merchant-info' and @class = 'offer-display-feature-text']/div/span/a")
        if seller_info:
            return(seller_info.text)
        else:
            return(None)
        
    else:
        return("Reebelo")
    
def str_to_int(price_str):
    # Remove non-numeric characters and keep the decimal point
    numeric_part = ''.join(filter(lambda x: x.isdigit() or x == '.', price_str))

    # Convert the numeric part to a float
    try:
        price_numeric = float(numeric_part)
    except ValueError:
        # Handle cases where conversion fails
        price_numeric = None
    
    return price_numeric


def convert_to_float(string):
    # Split the string by spaces
    if string == None:
        return None
    parts = string.split()
    # Iterate through the parts and extract the numeric part
    for part in parts:
        if part.isdigit():
            # Convert the numeric part to float
            return float(part)
    return None  # Return None if no numeric part is found


    







    

    
    