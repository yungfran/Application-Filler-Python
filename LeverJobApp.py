
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

import sys

name = "Robert Barratheon"
email = "scriptapplicationtester@gmail.com"
Phone = "8327049932"
linkedin = "https://www.linkedin.com/in/lord-rob/"
github = "https://github.com/LordRob"
portfolio = "robbartheon.com"
veteran = False



class Browser:

    driver = None

    def __init__ (self):
        option = Options()
        s = Service('/Library/Frameworks/Python.framework/Versions/3.7/binchromedriver.exe')
        self.driver = webdriver.Chrome(service=s)  
    
    def goto(self,url):
        self.driver.get(url)
    
    def input_name(self):
        #email_locator = sel.driver.locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
        # email_locator = self.driver.locate_with(By.TAG_NAME, "input")
        # conclusion_div = browser.find_element(locate_with(By.TAG_NAME,  "input").below(decision_div))
        name_elem = self.driver.find_element(By.NAME, "name")
        name_elem.send_keys(name)
        #return self.driver.find_elements(By.CLASS, "application-question")
    
    def input_email(self):
        email_elem = self.driver.find_element(By.NAME, "email")
        email_elem.send_keys(email)
    
    def input_phone(self):
        

        


if __name__ == "__main__":
    browser = Browser()
    browser.goto("https://jobs.lever.co/scratch/11d8ae1f-5429-4f79-948d-c0fea02ee28c/apply")
    time.sleep(2)
    browser.inputName()
    browser.inputEmail()
    time.sleep(10)