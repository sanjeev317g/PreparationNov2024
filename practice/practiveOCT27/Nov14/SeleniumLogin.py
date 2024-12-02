from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def selenium():
    
    
    driver = webdriver.Chrome()
    url = "https://practice.expandtesting.com/login"
    driver.get(url)
    driver.implicitly_wait(2)
    driver.maximize_window()



    element_login = driver.find_element(By.XPATH, "//button[.='Login']")
    element_usernmae = driver.find_element(By.XPATH,"//input[@id='username']")
    element_password = driver.find_element(By.XPATH,"//input[@id='password']")
    driver.execute_script("arguments[0].scrollIntoView();", element_usernmae)
    driver.implicitly_wait(2)
    element_usernmae.send_keys("practice")
    element_password.send_keys("SuperSecretPassword!")
    element_login.click()
    element_logged = driver.find_element(By.XPATH,"//b[.='You logged into a secure area!']")
    # element = WebDriverWait(driver.10).unti
    time.sleep(5)

selenium()