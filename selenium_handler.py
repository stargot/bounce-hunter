from time import sleep
from selenium import webdriver
import settings

driver = webdriver.Firefox()

driver.get(settings.START_URL)
sleep(2)

login_field = driver.find_element_by_id("vb_login_username")
password_field = driver.find_element_by_id("vb_login_password")
submit_form = driver.find_element_by_xpath("//input[@type='submit']")
sleep(2)

user_field.send_keys(settings.AUTH_LOGIN)
password_field.send_keys(settings.AUTH_PASSWORD)
submit_form.submit()
sleep(2)

with open("urls.txt") as f:
    lines = f.readlines()

for x in lines:
    driver.get(f"{x}")
    sleep(2)

driver.close()
