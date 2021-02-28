from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select



import random

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/accounts/emailsignup/')
sleep(5)

browser.close()