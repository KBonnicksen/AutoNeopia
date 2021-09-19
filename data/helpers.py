import time
from selenium.webdriver.support.ui import WebDriverWait


# helper function to tell python to wait any given # seconds
def wait(numSeconds, driver):
    print('Waiting ' + str(numSeconds) + ' seconds...')
    WebDriverWait(driver, numSeconds)

    while numSeconds > 0:
        time.sleep(1)
        print('.')
        numSeconds -= 1

    print('Finished waiting!')