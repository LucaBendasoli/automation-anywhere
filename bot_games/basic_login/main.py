"""This module is the main file that contains the logic for solving
the Basic Login Challange from Automation Anywhere - Bot Games. """

# Python imports
import sys
import os
import time
from typing import cast

# External libraries imports
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# Paths configuration
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared', '.env'))

# Project internal modules imports
from shared.config.config import URLS, XPATHS, CREDENTIALS
from shared.utils.utils import click_element_by_xpath, send_keys_by_xpath

def login_community(driver: WebDriver) -> None:
    """Log into the community to access the challange.

    Args:
        driver (WebDriver): Webdriver where the automation will occour."""
    click_element_by_xpath(driver, XPATHS['LANDING_PAGE']['ACCEPT_COOKIES'])
    click_element_by_xpath(driver, XPATHS['LANDING_PAGE']['COMMUNITY_LOGIN'])
    send_keys_by_xpath(driver, XPATHS['COMMUNITY_LOGIN']['EMAIL'], cast(str, os.getenv('EMAIL')), 30)
    click_element_by_xpath(driver, XPATHS['COMMUNITY_LOGIN']['SUBMIT_EMAIL'])
    send_keys_by_xpath(driver, XPATHS['COMMUNITY_LOGIN']['PASSWORD'], cast(str, os.getenv('PASSWORD')))
    click_element_by_xpath(driver, XPATHS['COMMUNITY_LOGIN']['SUBMIT_FORM'])

def start_challange() -> WebDriver:
    """Open the WebDriver, access the URL, and log into the community.
    Start the basic_login challenge, and once it starts, return the WebDriver.

    Returns:
		driver (WebDriver): WebDriver where the challange was started.
    """
    driver = webdriver.Chrome()
    driver.get(URLS['CHALLANGES']['BASIC_LOGIN'])
    login_community(driver)
    return driver

def do_challange(driver: WebDriver) -> None:
    """Logic that solves the basic challange, loging in succesfully.
    Waits 10 seconds to show the results.

    Args:
        driver (WebDriver): Logged in WebDriver where the challange wil be completed."""
    send_keys_by_xpath(driver, XPATHS['EXERCISES']['BASIC_LOGIN']['LOGIN'], CREDENTIALS['BASIC_LOGIN']['EMAIL'], 30)
    send_keys_by_xpath(driver, XPATHS['EXERCISES']['BASIC_LOGIN']['PASSWORD'], CREDENTIALS['BASIC_LOGIN']['PASSWORD'])
    click_element_by_xpath(driver, XPATHS['EXERCISES']['BASIC_LOGIN']['SIGN_IN'])
    time.sleep(10)

def main() -> None:
    """Execute the basic login automation."""
    driver = start_challange()
    do_challange(driver)

if __name__ == "__main__":
    load_dotenv(dotenv_path)
    main()
