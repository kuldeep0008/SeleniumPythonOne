from Locators.Locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id= Locators.password_textbox_id
        self.LoginButton_id= Locators.LoginButton_id
        self.invalidUsername_message_xpath= Locators.invalidUsername_message_xpath
        
        
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)
            
    def enter_password(self, password):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)
        
        
    def click_login(self):
        elem= self.driver.find_element_by_id(Locators.LoginButton_id)
        elem.click()
        
        
    #def check_invalid_username_mesage(self):
        #msg = self.driver.find_element_by_xpath(Locators.invalidUsername_message_xpath).text
        #return msg
        