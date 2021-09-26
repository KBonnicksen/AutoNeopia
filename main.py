from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located 
from selenium.common.exceptions import *
import json, subprocess
from data.account import *
from data.login import *


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

# bring in list of accounts + info
accts = read_acct_info_from_json_file(neo_accounts_filepath)

# Iterate over accounts
for i in accts:
    neo_acct = Account(i["username"], i["password"], i["state"])

    # TODO: Navigate NordVPN to location associated with account
        # nord_output = subprocess.Popen(nord_vpn_exe)
        # status = re.split("[\r \n :]", nord_output.communicate()[0].decode("utf-8"))[-2]

        # if status != "Disconnected":
        #     subprocess.call(["nordvpn", "disconnect"])

    # Log in to account
    login_pg = Login(neo_acct)  # Nav to page
    login_pg.login_to_site()

    # Run Dailies
    
    # flag account as having dailies complete account r




