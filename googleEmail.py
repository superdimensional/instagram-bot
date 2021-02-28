from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from accCred import emailGen, nameGen, passGen
import random


browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
sleep(5)

firstName_input = browser.find_element_by_css_selector("input[id='firstName']")
firstName_input.send_keys("XX")

lastName_input = browser.find_element_by_css_selector("input[id='lastName']")
lastName_input.send_keys("XX")

username_input = browser.find_element_by_css_selector("input[id='username']")
username_input.send_keys(nameGen())
print(nameGen())
accPasswd = passGen()

password_input = browser.find_element_by_css_selector("input[name='Passwd']")
password_input.send_keys(accPasswd)

confPass_input = browser.find_element_by_css_selector("input[name='ConfirmPasswd']")
confPass_input.send_keys(accPasswd, Keys.ENTER)

sleep(5)


phoneNum_input = browser.find_element_by_css_selector("input[id='phoneNumberId']")
phoneNum_input.send_keys("6475710755", Keys.ENTER)


# sleep(15)
# browser.close()