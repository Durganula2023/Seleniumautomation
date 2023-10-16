## Valid user registration

from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string

import time

logout_element = '/html/body/div/div[2]/div/div[2]/main/article/div/div/nav/ul/li[6]/a'

driver = webdriver.Chrome()

driver.implicitly_wait(10)

time.sleep(2)
driver.get("http://demostore.supersqa.com/my-account/")

register = driver.find_element(By.ID,'reg_email')

letter = string.ascii_lowercase

rand_string = ''.join(random.choice(letter) for i in range(15))

random_email = rand_string + '@supersqa.com'

register.send_keys(random_email)

time.sleep(2)
password = driver.find_element(By.ID,'reg_password')

password.send_keys('mynewpassword@2023')
time.sleep(2)
register_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/main/article/div/div/div[2]/div[2]/form/p[3]/button')

register_button.click()

time.sleep(2)

logout_button = driver.find_element(By.XPATH,logout_element)

if logout_button.is_displayed():
    print('pass')
else:
    raise Exception('user not logged in after registration')

time.sleep(5)