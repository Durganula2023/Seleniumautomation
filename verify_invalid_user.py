from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


class InvalidUserLoginError:
    invalid_email = "abc@supersqa.com"
    url = 'http://demostore.supersqa.com/my-account/'
    EXPECTED_MESSAGE = "The password you entered for the email address "

    def __int__(self):
        self.driver = webdriver.Chrome()
        time.sleep(2)

    def go_to_my_account(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID,'username')
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID,'password')
        field.send_keys('abcdefg')

    def click_login(self):
        self.driver.find_element(By.NAME,'login').click()

    def verify_error_message(self):
        error_message = self.driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/ul/li/a').text
        assert error_message == self.EXPECTED_MESSAGE, "The displayed error is not expected"
        print("pass")


    def main(self):
        self.go_to_my_account()
        self.input_email()
        time.sleep(2)
        self.input_password()
        time.sleep(2)
        self.click_login()
        time.sleep(2)
        self.verify_error_message()

if __name__ == "__main__":
    obj = InvalidUserLoginError()
    obj.main()

