from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Gokul_Data
from Test_Locators.locators import Gokul_Locators
from selenium.webdriver.support.ui import Select


class Gokul:
   
    def __init__(self, url):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)
   
    def login_Pim(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().username_input_box).send_keys(Gokul_Data().username)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().password_input_box).send_keys(Gokul_Data().password)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().submit_button).click()
        print("login successfully")
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().PIM_button).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Add_Employee).click()
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().FirstName_input_box).send_keys(Gokul_Data().FirstName)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().MiddleName_input_box).send_keys(Gokul_Data().MiddleName)
        self.driver.find_element(by=By.NAME, value=Gokul_Locators().LastName_input_box).send_keys(Gokul_Data().LastName)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Create_login_details).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().username_login_input_box).send_keys(Gokul_Data().username_login)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().password_login_input_box).send_keys(Gokul_Data().password_login)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Confirm_password_login_input_box).send_keys(Gokul_Data().Confirm_password_login)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Save_button).click()
        print("New employee addition Successfully")
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Nickname).send_keys(Gokul_Data().Nicename)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Employee_ID).clear().send_keys(Gokul_Data().Employee_ID)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Other_id).send_keys(Gokul_Data().Other_id)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Driver_license_number).send_keys(Gokul_Data().Driver_license_number)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().License_Expiry_Date).send_keys(Gokul_Data().License_Expiry_Date)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().SSN_Number).send_keys(Gokul_Data().SSN_Number)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().SIN_Number).send_keys(Gokul_Data().SIN_Number)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Nationality).find_elements(Gokul_Data().Nationality_tabindex).click
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Personal_details_save).click



        


s = Gokul(Gokul_Data().url)


s.login_Pim()



