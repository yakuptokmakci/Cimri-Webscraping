link_Cimri="https://www.cimri.com/cep-telefonlari/en-ucuz-apple-iphone-11-128gb-akilli-cep-telefonu-fiyatlari,a331840845"
def Cimri(link):
    store_prices = []
    store_names = []
    store_scores = []
    store_sites=[]
    alttext=[]

    driver.get(link)

    prices=driver.find_elements("xpath","//div[contains(@class,'s17f9cy4-19 heJchT')]//div[contains(@class,'s17f9cy4-11 gkkxYN')]")
    for price in prices:
        store_prices.append(price.get_attribute("innerHTML"))

    names=driver.find_elements("xpath","//div[contains(@class,'s17f9cy4-23 jFfEpu')]//span")
    images=driver.find_elements("xpath","//div[contains(@class, 's17f9cy4-23 jFfEpu')]//img")
    xpath_query = '//div[contains(concat(" ", normalize-space(@class), " "), "s17f9cy4-23") and contains(concat(" ", normalize-space(@class), " "), "jFfEpu")]'
    div_elements = driver.find_elements(By.XPATH,xpath_query)
    for image in images:
            store_sites.append(image.get_attribute("alt"))

    for div in div_elements:
        span_element = div.find_elements("xpath",".//span")
        if span_element:
            # Span etiketi varsa, title özelliğini alıp listeye ekleyin
            store_names.append(span_element[0].get_attribute("title"))
        else:
            # Span etiketi yoksa, "-" karakterini listeye ekleyin
            store_names.append("-")

    # Sonuçları yazdırın

    for x in range (len(store_prices)):
        print(store_sites[x],store_names[x],store_prices[x])



Cimri(link_Cimri)