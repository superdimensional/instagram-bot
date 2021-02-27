from time import sleep

from selenium import webdriver


browser = webdriver.Firefox()

browser.implicitly_wait(5)


browser.get('https://www.instagram.com/')


sleep(2)


username_input = browser.find_element_by_css_selector("input[name='username']")

password_input = browser.find_element_by_css_selector("input[name='password']")


username_input.send_keys("Array_in_a_matrix")

password_input.send_keys("yATM4JG9Jj5NZKQ")


login_button = browser.find_element_by_xpath("//button[@type='submit']")

login_button.click()


sleep(5)


browser.close()
