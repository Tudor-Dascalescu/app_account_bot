from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
import requests


# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("Generating accounts")
index = 0
driver = webdriver.Chrome(options=options)
driver.get("http://localhost:8080/#/public/login")
sleep(6)
while index < 6:
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div/button[2]').click() #click on Log In with test identity
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-portal-modal-container"]/div/div/div/div/div[2]/button[1]').click() #click on identities
    sleep(1)
    driver.find_element(By.ID, 'title').send_keys(f'test{index}') #enter identity name in input
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-portal-modal-container"]/div/div/div/div/div[1]/div[4]/button').click() #click on + button
    sleep(1)
    identity_list = driver.find_element(By.XPATH, '//*[@id="react-portal-modal-container"]/div/div/div/div/div[1]/div[3]/ul') #get identity list
    items = identity_list.find_elements(By.TAG_NAME, "li") # extract all identities

    driver.find_element(By.XPATH, f'//*[@id="react-portal-modal-container"]/div/div/div/div/div[1]/div[3]/ul/li[{len(items)}]').click() #select last created identity
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-portal-modal-container"]/div/div/div/div/div[2]/button[2]').click() #click on consent
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-portal-modal-container"]/div/div/div/div/div[2]/button[2]').click() #click on log in
    sleep(3)
    driver.find_element(By.ID, 'username').send_keys(f'test{index}') #enter username
    driver.find_element(By.ID, 'fullname').send_keys(f'TEST{index}') #enter fullname
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div[2]/div/form/button').click() #click on create account
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/div/div[1]/div[2]/div/button').click() #click on skip button
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/nav/div[2]/li[2]').click() #click on avatar button
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/aside/div/div[2]/div[2]/div/div/button[1]').click() #click on log out
    index+=1

print('clicked')
driver.quit()
