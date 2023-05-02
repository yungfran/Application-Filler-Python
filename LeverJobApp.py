
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import json

import sys

with open('user_info.json') as f:
    # Load the contents of the file
    user_info = json.load(f)

    

# Do something with the data
print(data["name"])
#https://boards.greenhouse.io/evolutioniq/jobs/4716493004?source=LinkedIn#app


class Browser:

    driver = None

    def __init__ (self):
        option = Options()
        s = Service('/Library/Frameworks/Python.framework/Versions/3.7/binchromedriver.exe')
        self.driver = webdriver.Chrome(service=s)  
    
    def goto(self,url):
        self.driver.get(url)
    
    def apply(self):
        self.input_required_data()
        self.input_optional_data()
    
    def input_required_data(self):
        self.upload_resume()
        self.input_name()
        self.input_email()
        self.input_phone()
        self.input_company()
    
    def input_optional_data(self):
        self.input_linkedin()
        self.input_twitter()
        self.input_github()
        self.input_other_website()
        self.input_portfolio()
        self.input_additional_data()

    """ Required Inputs """
    def upload_resume(self):
        resume_elem = self.driver.find_element(By.ID, "resume-upload-input")
        resume_elem.send_keys("/Users/francis/Desktop/ApplicationScript/RB_Resume.pdf")
        
    def input_name(self):
        name_elem = self.driver.find_element(By.NAME, "name")
        name_elem.send_keys(user_info["name"])
    
    def input_email(self):
        email_elem = self.driver.find_element(By.NAME, "email")
        email_elem.send_keys(user_info["email"])
    
    def input_phone(self):
        phone_elem = self.driver.find_element(By.NAME, "phone")
        phone_elem.send_keys(user_info["phone"])

    def input_company(self):
        company_elem = self.driver.find_element(By.NAME, "org")
        company_elem.send_keys(user_info["current_company"])
        

    """ Optional Inputs"""
    def input_linkedin(self):
        try:
            linkedin_elem = self.driver.find_element(By.NAME, "urls[LinkedIn]")
            linkedin_elem.send_keys(user_info["linkedin"])
        except:
            print("No LinkedIn Found")

    def input_twitter(self):
        try:
            twitter_elem = self.driver.find_element(By.NAME, "urls[Twitter]")
            twitter_elem.send_keys(user_info["twitter"])
        except:
            print("No Twitter Found")    

    def input_github(self):
        try:
            github_elem = self.driver.find_element(By.NAME, "urls[GitHub]")
            github_elem.send_keys(user_info["github"])
        except:
            print("No GitHub Found")

    def input_portfolio(self):
        try:
            portfolio_elem = self.driver.find_element(By.NAME, "urls[Portfolio]")
            portfolio_elem.send_keys(user_info["portfolio"])
        except:
            print("No portfolio Found")
    
    def input_other_website(self):
        try:
            other_website_elem = self.driver.find_element(By.NAME, "urls[Other]")
            other_website_elem.send_keys(user_info["other_website"])
        except:
            print("No other website Found")    
    
    def input_additional_data(self):
        try:
            additional_data_elem = self.driver.find_element(By.NAME, "comments")
            additional_data_elem.send_keys(user_info["additional_data"])
        except:
            print("No other website Found")    
            


if __name__ == "__main__":
    browser = Browser()
    browser.goto("https://jobs.lever.co/broadwaytechnology/5f8b6736-f326-44fa-b005-e2835b6956e2/apply")
    time.sleep(2)
    browser.apply()
    time.sleep(10)

"""
/* Pronouns

He/him

She/her

They/them

Xe/xem

Ze/hir

Ey/em

Hir/hir

Fae/faer

Hu/hu */

/*  Race

Hispanic or Latino
<div>White (Not Hispanic or Latino)</div>
<div>Black or African American (Not Hispanic or Latino)</div>
<div>Two or More Races (Not Hispanic or Latino)</div>
<div>Asian (Not Hispanic or Latino)</div>
<div>Two or More Races (Not Hispanic or Latino)</div>


*/

/*Veteran
Yes
No
Decline to identify

*/

"""