import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTittle(self, setup):
        self.logger.info("************ Test_001_Login ************")
        self.logger.info("************ Verifying Home Page Tittle ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title1 = self.driver.title
        if act_title1 == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************ Home Page Tittle Test is Passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTittle.png")
            self.driver.close()
            self.logger.error("************ Home Page Tittle Test is Failed ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************ Verifying Login test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.lp.clickLogout()   ## log outs here
            time.sleep(2)
            self.driver.close()
            self.logger.info("************ Login Test is Passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************ Login Test is Failed ************")
            self.driver.close()
            assert False


### To run this test type as follows in terminal window
### pytest -v --html=Reports\report.html testCases/test_login.py --browser chrome
##  --html=Reports\report.html    This line will generates html reports

### To run this test as samity or regression type as follows in terminal window
##### pytest -v -m "sanity or regression" --html=Reports\report.html testCases  --browser chrome      or
####  pytest -v -m "sanity and regression" --html=Reports\report.html testCases --browser chrome
