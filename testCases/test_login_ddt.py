import time

import pytest
import self
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************ Test_002_DDT_Login ************")
        self.logger.info("************ Verifying Login DDT test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in an excel:", self.rows)

        lst_status = []  ### Empty list variable
        time.sleep(2)

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_tittle = self.driver.title
            exp_tittle = "Dashboard / nopCommerce administration"

            if act_tittle == exp_tittle:
                if self.exp == "Pass":
                    self.logger.info("***** Passed *****")
                    time.sleep(2)
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***** Failed *****")
                    time.sleep(2)
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_tittle != exp_tittle:
                if self.exp == "Pass":
                    self.logger.info("***** Failed *****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("***** Passed *****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** Login DDT Test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT Test Failed *****")
            self.driver.close()
            assert False

        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("***** Completed TC_Login_DDT_002 *****")

### To run this test type as follows in terminal window
### pytest -v --html=Reports\report.html testCases/test_login_ddt.py --browser chrome