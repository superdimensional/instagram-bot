import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select, WebDriverWait

from accCred import emailGen, nameGen, passGen

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://mail.protonmail.com/create/new?language=en')
sleep(5)

username_input = browser.find_element_by_css_selector('input[name="username"]')
username_form = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, 'input[name="username"]')))
username_form.click()
# username_input.click()
# sleep(1)
# username_input.send_keys(nameGen())

# accPasswd = passGen()
# print(nameGen())
# print(accPasswd)

# password_input = browser.find_element_by_css_selector("input[id='password']")
# password_input.send_keys(accPasswd)

# confPass_input = browser.find_element_by_css_selector("input[id='passwordc']")
# confPass_input.send_keys(accPasswd, Keys.ENTER)

# sleep(3)
# browser.close()

#! theres no way i can get this to work
