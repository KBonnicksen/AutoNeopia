from page import *

class Bank(Page):

    path_ext = 'bank.phtml'

    def __init__(self):
        self.path += self.path_ext

        