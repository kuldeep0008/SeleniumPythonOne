from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from TestCases.ExcelRead import Excelread
import pandas as pd
import time
import unittest


class Recruitement_Page(unittest.TestCase):
    def __init__(self, driver):
        self.driver= driver
        self.Recruitment_Section_id='menu_recruitment_viewRecruitmentModule'
        self.job_Title_dropDown_id= 'candidateSearch_jobTitle'
    
    
    
    
    #def click_On_Recruitement_Page(self):
        self.driver.find_element_by_id(self.Recruitment_Section_id).click()
    
    
    def get_DropDown_Values(self):
        self.driver.find_element_by_id(self.job_Title_dropDown_id).click()
        select = Select(self.driver.find_element_by_xpath('//*[@id="candidateSearch_jobTitle"]'))
        select.select_by_value("9")
        options = [o.text for o in select.options] ;
        return pd.DataFrame(options)
        
    
    def get_Calendar_Date(self):
        datefield = self.driver.find_element_by_id('candidateSearch_fromDate')
        datefield.click()
        datefield.send_keys("2011-01-01")
        
    def fill_form(self):
        #JobTitle Dropdowns selection
        self.driver.find_element_by_id(self.job_Title_dropDown_id).click()
        select = Select(self.driver.find_element_by_xpath('//*[@id="candidateSearch_jobTitle"]'))
     
        select.select_by_value("9")
         
         
        #Status Dropdwons selection
        self.driver.find_element_by_id(self.job_Title_dropDown_id).click()
     
        select = Select(self.driver.find_element_by_xpath('//*[@id="candidateSearch_status"]'))
        select.select_by_value("SHORTLISTED")
 
 
        #Selecting Candidate name

            
        exlrd = Excelread()
        data1 = exlrd.readExcelData()
        for a in data1:
            for b in range(0,1):
                self.driver.find_element_by_xpath('//*[@id="candidateSearch_candidateName"]').send_keys(a[b])
                
                self.driver.find_element_by_xpath('//*[@id="candidateSearch_keywords"]').send_keys(a[b+1])
                #self.driver.find_elements_by_xpath('//*[@id="candidateSearch_keywords"]').send_keys(Keys.ENTER)
                
                #self.driver.find_element_by_xpath('//*[@id="candidateSearch_fromDate"]').clear()
                
                #self.driver.find_element_by_xpath('//*[@id="candidateSearch_fromDate"]').click()
                
                time.sleep(2)
                
                fromDate=self.driver.find_element_by_id('candidateSearch_fromDate')
                fromDate.click()
                fromDate.send_keys(a[b+2])
                
                #self.driver.find_element_by_xpath('//*[@id="candidateSearch_toDate"]').clear()
                
                
                
                time.sleep(2)
                
                toDate=self.driver.find_element_by_id('candidateSearch_toDate')
                toDate.click()
                toDate.send_keys(a[b+3])
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        