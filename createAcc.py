from time import sleep
from selenium import webdriver
from accCred import nameGen
from accCred import passGen

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/accounts/emailsignup/')
sleep(2)



username_input = browser.find_element_by_css_selector("input[name='emailOrPhone']")
# password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("testusername")
# password_input.send_keys(passGen())

# login_button = browser.find_element_by_xpath("//button[@type='submit']")
# login_button.click()

# sleep(5)
# browser.close()
