from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located 
from selenium.common.exceptions import *
from data.helpers import *

class Page:

    # Static driver for each class inheriting from Page so each page accesses the same session
    path = 'http://www.neopets.com/'
    options = webdriver.ChromeOptions().add_experimental_option('excludeSwitches', ['enable-logging'])      # exclude error caused by a bug in Chromedriver
    driver = webdriver.Chrome(options=options)

    def nav_to_page(self):
        self.driver.get(self.path)
        wait(3, self.driver)

