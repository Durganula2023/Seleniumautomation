from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

## pass the email
class Verifycoupoun:
    url = 'http://demostore.supersqa.com/my-account/'
    email = 'xyz@gmail.com'
    password = 'password@2023#$'
    email_ID = 'username'
    password_Id = 'password'
    gotohome_selector = '//html/body/div/div[1]/div/nav/a'
    select_the_product_selector = '/html/body/div[2]/div/div/div[2]/main/ul/li[4]/a[1]/img'

    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_url(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def login(self):
        self.driver.find_element(By.ID,self.email_ID ).send_keys(self.email)

    def enter_pass(self):
        self.driver.find_element(By.ID,self.password_Id).send_keys(self.password)

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()

    def gotohome(self):
        self.driver.find_element(By.XPATH,self.gotohome_selector).click()

    def select_the_product(self):
        self.driver.find_element(By.XPATH,self.select_the_product_selector).click()

    def add_to_cart(self):
        self.driver.find_element(By.NAME,'add-to-cart').click()

    def view_cart(self):
        self.driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/a').click()

    def find_coupoun_code(self):
        self.driver.find_element(By.NAME,'coupon_code').send_keys('SSQA100')

    def apply_coupoun(self):
        self.driver.find_element(By.CLASS_NAME,'button').click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[2]/main/article/div/div/div[2]/div/div/a').click()

    def main(self):
        self.go_to_url()
        time.sleep(2)
        self.login()
        time.sleep(2)
        self.enter_pass()
        time.sleep(2)
        self.click_login()
        time.sleep(2)
        self.gotohome()
        time.sleep(2)
        self.select_the_product()
        time.sleep(2)
        self.add_to_cart()
        time.sleep(2)
        self.view_cart()
        time.sleep(2)
        self.find_coupoun_code()
        time.sleep(2)
        self.apply_coupoun()
        time.sleep(2)
        self.proceed_to_checkout()
        time.sleep(5)


if __name__ == '__main__':
    obj = Verifycoupoun()
    obj.main()