from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Gokul_Data
from Test_Locators.locators import Gokul_Locators
import pytest

class Test_Gokul:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield self.driver


    def test_login(self, boot):
        boot.get(Gokul_Data().url)
        boot.implicitly_wait(10)
        boot.find_element(by=By.NAME, value=Gokul_Locators().username_input_box).send_keys(Gokul_Data().username)
        boot.find_element(by=By.NAME, value=Gokul_Locators().password_input_box).send_keys(Gokul_Data().password)
        boot.find_element(by=By.XPATH, value=Gokul_Locators().submit_button).click()
        print("The user is logged in successfully")
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().PIM_button).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Employee_List).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Employee_ID).send_keys(Gokul_Data().Employee_ID)
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Search_button).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Employee_ID_Delete).click()
        self.driver.find_element(by=By.XPATH, value=Gokul_Locators().Delete_button).click()
        print('employee delete successfully')