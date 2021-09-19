from page import *

class Login(Page):

    path_ext = '/login'

    def __init__(self, account):
        self.path += self.path_ext
        self.account = account

        return self.driver

    ##################################
    def login_to_site(self):    
        """Log in to Neopets with this account username and password."""

        try:
            # login with username and password
            self.driver.find_element_by_id('loginUsername').send_keys(self.account.username)
            self.driver.find_element_by_id('loginPassword').send_keys(self.account.password)

            # click to login
            self.driver.find_element_by_id('loginButton').click()

            print('Logging into account ' + self.account.username)
        except NoSuchElementException:
            print('Already logged into account. Moving on.')

        
