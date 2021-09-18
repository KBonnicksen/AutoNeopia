from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located 
from staticVars import *
from selenium.common.exceptions import *
import time

# TODO: Create a class for each neo account

# instantiate driver with options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])      # exclude error caused by a bug in Chromedriver
driver = webdriver.Chrome(options=options)

def wait(numSeconds):
    print('Waiting ' + str(numSeconds) + ' seconds...')
    WebDriverWait(driver, numSeconds)

    while numSeconds > 0:
        time.sleep(1)
        print('.')
        numSeconds -= 1

    print('Finished waiting!')

##################################
def loginToSite(username, password):
    """Log in to Neopets with the given username and password."""

    # nav to login
    driver.get(neoPath_Login)

    try:
        # login with username and password
        driver.find_element_by_id('loginUsername').send_keys(username)
        driver.find_element_by_id('loginPassword').send_keys(password)
        print('Logging into account ' + username)
    except NoSuchElementException:
        print('Already logged into account. Moving on.')

    # click to login
    driver.find_element_by_id('loginButton').click()

##################################
def trudysSurprise():
    # TODO: Implement daily here
    # nav to Trudy
    driver.get(neopath_TrudysSurprise)
    # driver.find_element_by_id('closeButton').click()


# ##################################
def visitBank():
    
#     # nav to bank
    driver.get(neoPath_Bank)
    driver.find_element_by_xpath("//input[@type='submit' and @value='Collect Interest']").click()


# WORKS ##################################
def anchorManagement():
    
    # nav to page
    print('Starting Anchor Management')
    driver.get(neoPath_AnchorManagement)
    driver.find_element_by_id('btn-fire').click()

# WORKS ##################################
def graveDanger():
    
    # nav to page
    print('Starting Grave Danger')
    driver.get(neoPath_GraveDanger)

    # If your petPet is back with something, adventure again!
    if driver.find_element_by_xpath("//button[text()='Adventure again!']") is not None:
        driver.find_element_by_xpath("//button[text()='Adventure again!']").click()

    driver.find_element_by_xpath("//button[text()='Choose a Petpet!']").click()
    wait(3)
    driver.find_element_by_xpath("//button[normalize-space()='Yes, Send This Petpet!']").click()

    # TODO: include code for when your pet comes back

# ##################################
def wheelOfMediocrity():
    
    # nav to page
    print('Starting Wheel of Mediocrity')
    driver.get(neoPath_WOMediocrity)
    wait(3)
    driver.find_element_by_id('wheelCanvas').click()
    wait(5)
    

# ##################################
def wheelOfExcitement():
    
    # nav to page
    print('Starting Wheel of Excitement')
    driver.get(neoPath_WOExcitement)
    wait(3)
    driver.find_element_by_id('wheelButtonSpin').click()
    wait(10)
    # TODO: enable click to claim your prize

# ##################################
def wheelOfKnowledge():
    
    # nav to page
    print('Starting Wheel of Knowledge')
    driver.get(neoPath_WOKnowledge)
    wait(3)
    driver.find_element_by_id('wheelButtonSpin').click()
    wait(10)
    driver.find_element_by_id('wheelCanvas').click()
    
    #exit 
    wait(3)
    driver.find_elements_by_class_name("wheel-exit-icon")

###################################################################################################
###################################################################################################
def main():
    loginToSite(acct1_username, acct1_password)
    wait(4)
    # visitBank()
    # # trudysSurprise()
    # anchorManagement()
    # wait(4)
    graveDanger()
    wheelOfMediocrity()
    wheelOfKnowledge()
main()