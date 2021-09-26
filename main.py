from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located 
from selenium.common.exceptions import *
import json, subprocess
from data.account import *
from data.login import *
from data.bank import *
from data.anchor_management import *


neo_accounts_filepath = r'C:\Users\kelse\Documents\NeoLogins.json'
nord_vpn_exe = r'C:\Program Files\NordVPN\NordVPN.exe'

def read_acct_info_from_json_file(file):
    """Opens JSON file with login information and returns info in dictionary list."""

    accts = []
    acct_file = open(file,)                 # open json file
    acct_data = json.load(acct_file)        # put file contents into JSON variable

    for i in acct_data["accounts"]:         # put into list of accounts
        accts.append(i)

    acct_file.close()                       # close file
    return accts

def Run_dailies(Account):
    # Bank
    print('Running Bank Daily')
    bank = Bank()
    bank.collect_interest()

    # Bank
    print('Running Anchor Management')
    anchor_management = Anchor_Management()
    bank.collect_interest()



# main() #########################################################################################
##################################################################################################
# bring in list of accounts + info
accts = read_acct_info_from_json_file(neo_accounts_filepath)

# Iterate over accounts
for i in accts:
    neo_acct = Account(i["username"], i["password"], i["state"])


    # Log in to account
    login_pg = Login(neo_acct)  # Nav to page
    login_pg.login_to_site()    # login to account

    neo_acct.set_driver(login_pg.driver)    # Set account driver to curr driver being used by LoginPg
    curr_neopoints = neo_acct.get_curr_neopoints()
    print('Starting off the day with ' + str(curr_neopoints))

    # Run Dailies
    Run_dailies(neo_acct)
    # flag account as having dailies complete account r




