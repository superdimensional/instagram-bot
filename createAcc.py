import json
import random
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from accCred import toEmail, JSONToUsername, JSONToPassword


username = JSONToUsername(0).translate({ord(i): None for i in "{'username': '"}).translate({ord(i): None for i in "'}"})
password = JSONToPassword(0).translate({ord(i): None for i in "{'password': '"}).translate({ord(i): None for i in "'}"})


# TODO: make it so it cycles between the entries in the json file
# TODO: import email credential json and use it to create accounts

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/accounts/emailsignup/')
sleep(2)

email_input = browser.find_element_by_css_selector("input[name='emailOrPhone']")
fullname_input = browser.find_element_by_css_selector("input[name='fullName']")
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

print("\nusername: " + username + "\npassword: " + password + "\n")

email_input.send_keys(toEmail(username))
fullname_input.send_keys(username)
username_input.send_keys(username)
password_input.send_keys(password)

login_button = browser.find_element_by_xpath('//button[@type="submit"]')            
login_button.click()                                                               
                                                                                    
sleep(3)

# TODO: add something to check if the username is taken
# TODO: if username taken, advance 1 entry from the json file and try again

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

# ? i give up

browser.find_element_by_xpath('//button[@type="button"]').click()
sleep(2)
# browser.find_element_by_xpath("//button[@type='button']").click()       # ? this just broke for no reason button literally just stopped working

x_button = browser.find_element_by_class_name('wpO6b  ')#.find_element_by_xpath("//button[@type='button']")
x_button.click()

birthYear.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)

# sleep(20)
# browser.close()
