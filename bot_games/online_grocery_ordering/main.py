"""This module is the main file that contains the logic for solving the
Online Grocery Ordering Challange from Automation Anywhere - Bot Games. """

# Inernal Python imports
import sys
import os
import time

# External libraries imports
from dotenv import load_dotenv
import pandas as pd
from pandas import DataFrame
from selenium.webdriver.remote.webdriver import WebDriver

# Paths configuration
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared', '.env'))

# Project internal modules imports
from shared.utils.utils import start_challange, send_keys_by_xpath, click_element_by_xpath
from shared.config.config import URLS, XPATHS, CREDENTIALS

# Functions
def order_groceries(driver: WebDriver, grocery_list: DataFrame) -> None:
	"""Logic that solves the online grocery ordering challange, ordering all the groceries
	from the list.

	Args:
		driver (WebDriver): Logged in WebDriver where the challange wil be completed.
		grocery_list (DataFrame): List of all the groceries that will be ordered."""
	grocery_ordering_locators = XPATHS['EXERCISES']['GROCERY_ORDERING']
	for _, row in grocery_list.iterrows():
		send_keys_by_xpath(driver, grocery_ordering_locators['GROCERY_INPUT'], row['Favorite Food'])
		click_element_by_xpath(driver, grocery_ordering_locators['ADD_ITEM'])
	click_element_by_xpath(driver, grocery_ordering_locators['AGREE_TERMS'])
	click_element_by_xpath(driver, grocery_ordering_locators['SUBMIT_ORDER'])

def main() -> None:
    """Execute the online grocery ordering automation."""
    driver = start_challange(
    challange_url=URLS['CHALLANGES']['GROCERY_ORDERING'],
    locators=XPATHS,
    username=os.getenv('EMAIL'),
    password=os.getenv('PASSWORD')
	)
    grocery_list = pd.read_csv('bot_games/online_grocery_ordering/data/shopping-list.csv')
    order_groceries(driver, grocery_list)
    time.sleep(10) # Wait for the results

if __name__ == '__main__':
	load_dotenv(dotenv_path)
	main()
