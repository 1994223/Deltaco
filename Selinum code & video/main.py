from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('file:///C:/xampp/htdocs/orders/Deltaco-master/register.html')
action = webdriver.ActionChains(browser)
fname = browser.find_element_by_id('registration-fullname')
fname.send_keys("sannithgmail")
email = browser.find_element_by_id('registration-email')
email.send_keys("sannith@gmail.com")
phone = browser.find_element_by_id('registration-phone')
phone.send_keys("1234567890")
passw = browser.find_element_by_id('registration-password')
passw.send_keys("sannith@g")


#browser.get('https://accounts.google.com/ServiceLogin?         service=mail&continue=https://mail.google.com/mail/#password')

browser.find_element_by_id('register').click()

email = browser.find_element_by_id('email')
email.send_keys("sannith@gmail.com")


passw = browser.find_element_by_id('passw')
passw.send_keys("sannith@g")

browser.find_element_by_id('login').click()

browser.find_element_by_class_name("btn_prod").click()

browser.close()