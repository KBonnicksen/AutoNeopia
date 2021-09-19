class Account:
    # self.username = ''
    # self.password = ''
    def __init__(self, username, password, location):

        self.username = username
        self.password = password
        self.location = location 

        self.neopoints = 0
        self.neopets = []
        self.curr_neopet = ''
        self.driver = ''
        self.active_neopet = ''

    def set_driver(self, driver):
        self.driver = driver

    def get_curr_neopoints():

        raise NotImplementedError

    def get_curr_neopet():

        raise NotImplementedError


    