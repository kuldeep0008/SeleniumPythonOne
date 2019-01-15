import unittest
from selenium import webdriver
import sys
import os
from TestCases.RecruitementPage import Recruitement_Page
from TestCases.ExcelRead import Excelread
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from TestCases.LoginPage import LoginPage
from TestCases.homePage import HomePage


import time

import HtmlTestRunner

class Test(unittest.TestCase):
     
    @classmethod    
    def setUpClass(self):
          
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\kpanwar\Documents\ChromeDriver\chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_01_Valid_Login(self):
        
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
         
        Login= LoginPage(driver)
         
        
        Login.enter_username("Admin")
        
        time.sleep(5)
        
        Login.enter_password("admin123")
        
        time.sleep(5)
         
        Login.click_login()
        
        time.sleep(5)
#         home=HomePage(driver)
#            
#         time.sleep(5)
#         home.click_welcome()
#         time.sleep(5)
#         home.click_logout()
#         time.sleep(10)
        recpage= Recruitement_Page(driver)
         
        recpage.click_On_Recruitement_Page()
        
        time.sleep(5)
        #recpage.get_Calendar_Date()
        recpage.fill_form()
        
#         vals=recpage.get_DropDown_Values()
#           
#         print(vals)
#           
#         recpage.get_Calendar_Date()
        
        time.sleep(5)
        
        print("all Done")
        
    
    def tearDown(self):
        #self.driver.close()
        #self.driver.quit()
        print("Test Completed")
        
        
        
        
    if __name__=='__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\kpanwar\eclipse-workspace\SeleniumPythonOne\src\reports\Test.html"))
        
        
        
        
        
        
        
        
        
        