import random
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from accCred import emailGen, nameGen, passGen


# TODO: import email credential json and use it to create accounts

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
username_input.send_keys(nameGen()))
password_input.send_keys(passGen())

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(3)

# TODO: add something to check if the username is taken
# try:
#     sleep
#     l = browser.find_element_by_css_selector('input[id="ssfErrorAlert"]')
#     s = l.text
#     print("Element exist -" + s)
#     browser.close()
# except NoSuchElementException:
#     print("Error does not exist\n")

birthMonth = browser.find_element_by_xpath("//select[@title='Month:']") # find select button
drop = Select(birthMonth)                                               # actully select it
drop.select_by_value(str(random.randint(1, 12)))                        # choose option based on value

birthDay = browser.find_element_by_xpath("//select[@title='Day:']")
drop = Select(birthDay) 
drop.select_by_value(str(random.randint(1, 28))) 

birthYear = browser.find_element_by_xpath("//select[@title='Year:']")
drop = Select(birthYear) 
drop.select_by_value(str(1900 + random.randint(20, 100))) 

signup_button = browser.find_element_by_xpath("//button[@type='button']")
signup_button.click()

# TODO: add something to print credentials to instaToFile.txt

sleep(10)
browser.close()
