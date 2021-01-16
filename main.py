import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

years = ['1999', '2017', '2018']
prices = ['35000000', '222000000', '145000000']
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

for year, price in zip(years, prices):
    url = 'https://www.in2013dollars.com/europe/inflation/{}'.format(year)
    driver.get(url)
    time.sleep(2)

    amount_input = driver.find_element(By.XPATH, '//*[@id="amount"]')
    amount_input.clear()
    amount_input.send_keys(price)
    time.sleep(1)

    calculate_btn = driver.find_element(By.XPATH, '//*[@id="btn-calculate"]')
    calculate_btn.click()
    time.sleep(3)

    today_value = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/table/tbody/tr[9]/td[2]')
    today = today_value.text
    print("Price in 1999 --> €{} || Price in 2020 ---> {}".format(price, today))
    time.sleep(3)

time.sleep(5)
driver.close()
