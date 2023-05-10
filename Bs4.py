from selenium import webdriver
from selenium.webdriver.common.by import By
link="https://www.cimri.com/dizustu-bilgisayar/en-ucuz-lenovo-n4120-128-gb-4-gb-ram-notebook-fiyatlari,2088029188"
def Cimri(link):
    store_links=[]
    store_prices=[]
    store_names=[]
    condition=0
    driver = webdriver.Chrome()

    driver.get(link)
    xpath_expression = '//div[contains(@class, "s17f9cy4-19") and contains(@class, "heJchT")]//img'
    elements = driver.find_elements(By.XPATH, xpath_expression)
    alt_texts = [element.get_attribute("alt") for element in elements]
    search_item="https://"

    for alt_text in alt_texts:
            if search_item in alt_text:
                store_links.append(alt_text)

    prices=driver.find_elements("xpath","//div[contains(@class,'s17f9cy4-11 gkkxYN')]")
    for price in prices:
        store_prices.append(price.get_attribute("innerHTML"))

    names=driver.find_elements("xpath","//div[contains(@class,'s17f9cy4-25 gufRKu')]//span[@title]")

    for name in names:
        store_names.append(name.get_attribute("innerHTML"))

    for x in range (len(store_links)):
        print(store_links[x] ,store_prices[x])
    driver.quit()

Cimri(link)


