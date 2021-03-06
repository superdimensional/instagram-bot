import json
import random
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from accCred import emailGen, nameGen, passGen

# with open('credentials/botCred.json') as input_file:
#     json_array = json.load(input_file)
#     store_list = []

# for item in json_array[1]:
#     store_details = {"username":None, "email":None, "password":None}
#     store_details['username'] = item['username']
#     # store_details['email'] = item['email']
#     # store_details['password'] = item['password']
#     store_list.append(store_details)
#     print(store_list)

input_file = open ('credentials/botCred.json')
json_array = json.load(input_file)
store_list_username = []
store_list_password = []

for item in json_array:
    stored_username = {"username":None}
    stored_password = {"password":None}
    stored_username['username'] = item['username']
    stored_password['password'] = item['password']
    store_list_username.append(stored_username)
    store_list_password.append(stored_password)

username_login = str(store_list_username[1])
password_login = str(store_list_password[1])
print(username_login.translate({ord(i): None for i in "{'username': '"}).translate({ord(i): None for i in "'}"}))
print(password_login.translate({ord(i): None for i in "{'password': '"}).translate({ord(i): None for i in "'}"}))


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

email_input.send_keys(emailGen())
fullname_input.send_keys(nameGen())
username_input.send_keys(nameGen())
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
