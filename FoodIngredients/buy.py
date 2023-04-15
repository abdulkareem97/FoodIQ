from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# import org.openqa.selenium.By;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from FoodIngredients import app

# create a new Chrome browser instance
def buyItems(items):
    
    driver = webdriver.Chrome()
    url = 'https://www.jiomart.com/search'
    driver.get(url)
    time.sleep(1)
    for item in items:
        try:
            driver.get(url+"/"+item)
            wait = WebDriverWait(driver, 3)
            element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ol.ais-InfiniteHits-list li:first-child a div.plp-card-container div.plp-card-details-sub div.plp-card-cart div.product-card-cta button")))
            element.click()

            str1 = " hello "
            print(element,"element clicked")
            time.sleep(1)
        except:
            print("error")
    # return

    url = 'https://www.jiomart.com/checkout/cart'
    driver.get(url)
    time.sleep(100)

