"""This module is the main file that contains the logic for solving
the Basic Login Challange from Automation Anywhere - Bot Games. """

# Internal Python imports
import sys
import os
import time

# External libraries imports
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# Paths configuration
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared', '.env'))

# Project internal modules imports
from shared.config.config import URLS, XPATHS, CREDENTIALS
from shared.utils.utils import start_challange, click_element_by_xpath, send_keys_by_xpath

# Functions
def login(driver: WebDriver) -> None:
    """Logic that solves the basic challange, loging in succesfully.
    Waits 10 seconds to show the results.

    Args:
        driver (WebDriver): Logged in WebDriver where the challange wil be completed."""
    send_keys_by_xpath(driver, XPATHS['EXERCISES']['BASIC_LOGIN']['LOGIN'], CREDENTIALS['BASIC_LOGIN']['EMAIL'], timeout=30)
    send_keys_by_xpath(driver, XPATHS['EXERCISES']['BASIC_LOGIN']['PASSWORD'], CREDENTIALS['BASIC_LOGIN']['PASSWORD'])
    click_element_by_xpath(driver, XPATHS['EXERCISES']['BASIC_LOGIN']['SIGN_IN'])

def main() -> None:
    """Execute the basic login automation."""
    driver = start_challange(
        challange_url=URLS['CHALLANGES']['BASIC_LOGIN'],
        locators=XPATHS,
        username=os.getenv('EMAIL'),
        password=os.getenv('PASSWORD')
    )
    login(driver)
    time.sleep(10) # Wait for the results

if __name__ == "__main__":
    load_dotenv(dotenv_path)
    main()
