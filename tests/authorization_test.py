from selenium import webdriver
import time

# Укажите существующие логин и пароль от VK
USERNAME = '+996555980821'
PASSWORD = '1991701323'


class Authorization:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.close()

    def log_in(self):
        self.driver.implicitly_wait(10)
        self.driver.get('https://vk.com/')
        self.driver.find_element_by_id('index_email').send_keys(USERNAME)
        self.driver.find_element_by_id('index_pass').send_keys(PASSWORD)
        self.driver.find_element_by_id('index_login_button').click()


class TestAuthorization(Authorization):
    def test_login_success(self):
        self.log_in()
        time.sleep(3)
        assert self.driver.current_url == 'https://vk.com/feed'

    def test_login_unsuccess(self):
        self.driver.implicitly_wait(10)
        self.driver.get('https://vk.com/')
        self.driver.find_element_by_id('index_email').send_keys(USERNAME)
        self.driver.find_element_by_id('index_pass').send_keys('qwerty')
        self.driver.find_element_by_id('index_login_button').click()
        self.driver.implicitly_wait(10)
        error_message = self.driver.find_element_by_class_name('msg_text')
        message = error_message.find_elements_by_tag_name('b')[0]
        assert message.text == 'Не удаётся войти.'
