from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from accCred import emailGen, nameGen, passGen

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/accounts/emailsignup/')
sleep(2)



email_input = browser.find_element_by_css_selector("input[name='emailOrPhone']")
fullname_input = browser.find_element_by_css_selector("input[name='fullName']")
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

email_input.send_keys(emailGen())
fullname_input.send_keys(nameGen())
username_input.send_keys(nameGen())
password_input.send_keys(passGen())

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)

selectYear_input = browser.find_element_by_xpath("//select[@title='Year:']")
selectYear_input.click()
birthYear_input = browser.find_element_by_xpath("//select[@title='1969']")
birthYear_input.click()

sleep(10)
browser.close()
