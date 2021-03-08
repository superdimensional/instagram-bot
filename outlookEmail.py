import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select, WebDriverWait 

from accCred import emailGen, emailToFile, nameGen, passGen, credToJSON

accPasswd = passGen()
accUsername = nameGen()
print(accUsername)
print(accPasswd)
# credToJSON(accUsername, accPasswd) # ! remove when finished 

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('https://signup.live.com/signup?lcid=1033&wa=wsignin1.0&rpsnv=13&ct=1614639399&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26signup%3d1%26RpsCsrfState%3d3a30b6f4-ee09-ca31-da8e-a3c6ff4cfa7c&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&lic=1&uaid=f7f6a20df93149dab6001b5324b81fb5')
sleep(5)

# accPasswd = passGen()
# accUsername = nameGen()
# print(accUsername)
# print(accPasswd)



username_input = browser.find_element_by_css_selector('input[id="MemberName"]')
username_input.send_keys(accUsername, Keys.ENTER)

sleep(3)

password_input = browser.find_element_by_css_selector('input[id="PasswordInput"]')
password_input.send_keys(accPasswd, Keys.ENTER)

sleep(3)

firstName_input = browser.find_element_by_css_selector("input[id='FirstName']")
firstName_input.send_keys("XX")

lastName_input = browser.find_element_by_css_selector("input[id='LastName']")
lastName_input.send_keys("XX", Keys.ENTER)

sleep(3)

country_input = browser.find_element_by_xpath("//select[@id='Country']")
drop = Select(country_input) 
drop.select_by_value("AF") 

birthMonth_input = browser.find_element_by_xpath('//select[@id="BirthMonth"]')
drop = Select(birthMonth_input)                                              
drop.select_by_value(str(random.randint(1, 12)))                        

birthDay_input = browser.find_element_by_xpath('//select[@id="BirthDay"]')
drop = Select(birthDay_input) 
drop.select_by_value(str(random.randint(1, 28))) 

birthYear_input = browser.find_element_by_xpath('//select[@id="BirthYear"]')
drop = Select(birthYear_input) 
drop.select_by_value(str(1900 + random.randint(20, 100))) 

button_input = browser.find_element_by_css_selector('input[id="iSignupAction"]')
button_input.send_keys(Keys.ENTER)

sleep(120) # time to solve captcha manually will be removed in the future? 

# TODO: add something to automatically do the funCaptcha

credToJSON(accUsername, accPasswd) # this is over here to make sure the account is actually valid before dumping it into the file
    
# TODO:  make it find an element if the element exists then do whats under this comment
# TODO:  write <email>:<password> combo into a file if the account was successfully created

sleep(3)
browser.close()


