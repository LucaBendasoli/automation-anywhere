"""This module contains custom utilitary functions to work with selenium."""

from typing import Callable, Tuple, cast

# Selenium
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ExpectedConditionType = Callable[[Tuple[str, str]], Callable[[WebDriver], WebElement | bool]]

# 1 ------------------------------------------------------------------------------------------------
# WebDriver Function

def click_element_by_xpath(
	driver: WebDriver,
	locator: str,
	timeout: int = 5,
	condition: ExpectedConditionType = EC.element_to_be_clickable
) -> None:
    """
    **Wait until the element is clickable and the clicks it.**

    **The function expects the element to be available on the page according to the provided
    condition. If the element is not found within the specified time, an exception will be thrown.**

    **Note:**
        - This function does not handle exceptions internally to maintain reusability and cohesion.
        - Error handling should be implemented at the upper layer as needed.

Args:
        driver (WebDriver): Instance of the WebDriver where the element will be clicked.
        locator (str): The XPath of the element to be clicked.
        timeout (int, optional): Maximum wait time for the element. The default is 5 seconds.
        condition (ExpectedConditionType, optional):
            Wait condition for the element. The default is `EC.element_to_be_clickable`.

    Raises:
        TimeoutException: If the element is not found within the specified time.
        ElementClickInterceptedException: If another element intercepts the click.
        NoSuchElementException: If the provided XPath does not match any element on the page.
        StaleElementReferenceException: If the element becomes invalid before the click.
    """
    element = WebDriverWait(driver, timeout).until(condition((By.XPATH, locator)))
    element.click()

# 2 ------------------------------------------------------------------------------------------------
# WebDriver Function

def send_keys_by_xpath(
	driver: WebDriver,
	locator: str,
    text: str,
	timeout: int = 5,
	condition: ExpectedConditionType = EC.presence_of_element_located,
    clear: bool = True
) -> None:
    """
    **Wait for the element to be located and then sends a text.**

    **The function waits for the element to located using the specified condition,
    and then enters the provided text. Optionally, the content of the element can
    be cleared before sending the text. If the element is not found within the
    specified time, an exception will be thrown.**

    **Note:**
        - This function does not handle exceptions internally to maintain reusability and cohesion.
        - Error handling should be implemented at the upper layer as needed.

    Args:
        driver (WebDriver): Instance of the WebDriver where the element will receive the text.
        locator (str): The XPath of the element where the text will be inserted.
        text (str): The text to be sent to the element.
        timeout (int, optional): Maximum wait time for the element. The default is 5 seconds.
        condition (ExpectedConditionType, optional):
            Wait condition for the element. The default is `EC.presence_of_element_located`.
        clear (bool, optional):
            If `True`, clears the current content of the element before inserting the new text.
            The default is `True`.

    Raises:
        TimeoutException: If the element is not found within the specified time.
        ElementNotInteractableException: If the element cannot receive text input.
        NoSuchElementException: If the XPath does not match any element on the page.
        StaleElementReferenceException: If the element becomes invalid before interaction.
    """
    element = WebDriverWait(driver, timeout).until(condition((By.XPATH, locator)))
    if clear:
        element.clear()
    element.send_keys(text)

# 3 ------------------------------------------------------------------------------------------------
# WebDriver Function

def find_element_by_xpath(
	driver: WebDriver,
    locator: str,
    timeout: int,
    condition: ExpectedConditionType = EC.presence_of_element_located
) -> WebElement | None:
    """
    **Wait for the element to be located and then returns it.**

    **The function attempts to find an element on the page as defined by the specified condition.
    If the element is not found within the given time, or if any exception related to the search
    occurs, the function returns None, allowing the execution flow to continue without propagating
    exceptions.**

    Args:
        driver (WebDriver): Instance of the WebDriver where the element will be located.
        locator (str): The XPath of the element to be located.
        timeout (int): Maximum wait time for the presence of the element.
        condition (ExpectedConditionType, optional):
            Wait condition for the element. The default is `EC.presence_of_element_located`.

    Returns:
        WebElement or None: The element if found within the time; otherwise, None.
    """
    try:
        element = cast(WebElement, WebDriverWait(driver, timeout).until(condition((By.XPATH, locator))))
        return element
    except (TimeoutException, NoSuchElementException):
        return None
