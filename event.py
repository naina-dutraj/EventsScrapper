import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://in.bookmyshow.com/'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options,executable_path="C:/Users/Naina Dutraj/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver.implicitly_wait(10)
driver.get(url)

def click_cities():
    record = []
    # time.sleep(5)
    #cities_name.click()
    time.sleep(2)
    record = []
    for city in range(1,11):
        core_css_selector = f'li.bwc__sc-ttnkwg-18.KUowN:nth-child({city})'
        cities_name = driver.find_element(By.CSS_SELECTOR, value=core_css_selector)
        time.sleep(2)
        cities_name.click()
        time.sleep(2)
        event_click = '//*[@id="super-container"]/div[2]/div[1]/header/div[2]/div/div/div/div[1]/div/a[3]'
        driver.find_element(By.XPATH, event_click).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)-1;")
        time.sleep(2)
        time.sleep(2)
        all_events = '//*[@id="super-container"]/div[2]/div[3]/div[2]/div[3]/div/div/div[2]/a'
        events = driver.find_elements(By.XPATH, all_events)
        for event in events:
            event_name_css = 'div.sc-7o7nez-0.hGuczM'
            location_css = 'div.sc-7o7nez-0.eniJLq'
            type_css = 'div.sc-7o7nez-0.ifFqly'
            cost_css = 'div.sc-133848s-2.sc-133848s-12.hxPdAO:nth-child(4)'
            name = event.find_element(By.CSS_SELECTOR, value=event_name_css).text
            location = event.find_element(By.CSS_SELECTOR, value=location_css).text
            type = event.find_element(By.CSS_SELECTOR, value=type_css).text
            try:
                cost = event.find_element(By.CSS_SELECTOR, value=cost_css).text.split(' ')[1].strip()
            except:
                cost = event.find_element(By.CSS_SELECTOR, value=cost_css).text
            record.append([name, location, type, cost])
            pprint(record)
        driver.execute_script("window.scrollTo(0,0);")
        triangle_button = driver.find_element(By.CSS_SELECTOR, value= 'span.bwc__sc-1nbn7v6-10.cntvL.ellipsis')

        triangle_button.click()
    return record

record = click_cities()
driver.quit()
print(len(record))

data = pd.DataFrame(record, columns =['Event_name','Location','Type','Minimum_cost'] )
data.to_csv('Events.csv', index=False, encoding='utf-8')