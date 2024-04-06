from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

def find_element(driver, by, xpath):
    try:
        element = driver.find_element(by, xpath)
        return element
    except NoSuchElementException:
        print(f"Element not found with XPath: {xpath}")
        return None
    



def click_button_safe(driver, button, timeout=10):
    """
    Safely clicks a button, handling ElementClickInterceptedException and waiting until clickable.
    
    Args:
        driver: WebDriver object representing the browser session.
        button: WebElement object representing the button to click.
        timeout: Maximum time (in seconds) to wait for the button to become clickable (default is 10 seconds).
        
    Returns:
        bool: True if the button was successfully clicked, False otherwise.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        button = wait.until(EC.element_to_be_clickable(button))
        button.click()
        return True
    except TimeoutException:
        print(f"TimeoutException: Button is not clickable within {timeout} seconds.")
        return False
    except ElementClickInterceptedException:
        print("ElementClickInterceptedException: The button is not clickable at this moment.")
        return False

  
