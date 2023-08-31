from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


####################### pytest html report ###########################
# hook for adding environment info to html report
def pytest_configure(config):
    config._metadata = {"Project Name": "Hybrid Framework Practice",
                        "Tester": "Ismail",
                        "Module name": "Customers"
                        }


## hook for delete/modify environment info to html report  ##

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
