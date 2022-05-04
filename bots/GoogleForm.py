import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://forms.gle/1tR3pXjG75eY7L3L9")

i = 0
while i < 5:
    r = random.randint(1, 2)
    print(r)
    time.sleep(0.2)
    if r == 1:
        driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[2]/label").click()
    elif r == 2:
        driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span/div/div[1]/label").click()
    driver.find_element(by=By.XPATH ,value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span").click()
    i += 1
    driver.get("https://forms.gle/1tR3pXjG75eY7L3L9")
    
driver.close()
