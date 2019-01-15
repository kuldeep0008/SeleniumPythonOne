from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from TestCases.ExcelRead import Excelread
import pandas as pd

class Recruitement_Page():
    def __init__(self, driver):
        self.driver= driver
        self.Recruitment_Section_id='menu_recruitment_viewRecruitmentModule'
        self.job_Title_dropDown_id= 'candidateSearch_jobTitle'
    
    
    
    
    def click_On_Recruitement_Page(self):
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
        select.select_by_value("9")
 
 
        #Selecting Candidate name

            
        exlrd = Excelread()
        data1 = exlrd.readExcelData()
        for a in data1:
            for b in range(len(a)):
                self.driver.find_element_by_xpath('//*[@id="candidateSearch_candidateName"]').send_keys(a[b])
                
                self.driver.find_element_by_xpath('//*[@id="candidateSearch_keywords"]').send_keys(a[b])
                
                #self.driver.find_element_by_xpath('//*[@id="candidateSearch_fromDate"]').clear()
                
                self.driver.find_element_by_xpath('//*[@id="candidateSearch_fromDate"]').send_keys(a[b])
                
                #self.driver.find_element_by_xpath('//*[@id="candidateSearch_toDate"]').clear()
                
                self.driver.find_element_by_xpath('//*[@id="candidateSearch_toDate"]').send_keys(a[b])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        