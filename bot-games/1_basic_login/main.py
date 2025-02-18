"""Este é o arquivo principal da solução do exercício "Basic Login" do automation anywhere bot games. """

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import URL

driver = webdriver.Chrome()
driver.get(URL)
driver.find_element(By.XPATH, '//*[contains(text(), "Aceitar cookies")]').click()
driver.find_element(By.XPATH, '//*[@aria-label="Community login"]').click()
driver.find_element(By.XPATH, '//*[@placeholder="*Email"]').send_keys("user@automationanywhere.com")
driver.find_element(By.XPATH, '//*[@placeholder="*Email"]/../../following-sibling::div[1]').click()
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Automation123")
driver.find_element(By.XPATH, "//input[@placeholder='Password']/../../following-sibling::div[1]/div/div/button").click()