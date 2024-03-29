import pytest
from appium import webdriver

import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

## iOS
def appium_options_ios():
    options = DesiredCapabilities.IPHONE
    options['platformName'] = 'iOS'
    options['platformVersion'] = '17.0' # Update this to your iOS version
    options['deviceName'] = 'SIMULATOR_NAME'  # Update this to your device
    options['automationName'] = 'XCUITest'
    options['app'] = '/PATH_TO_YOUR_APP/YOUR_APP_NAME.app'  # Update this to your app path
    options['launchTimeout'] = 8000 # Update this according to your app runtime
    options['autoAcceptAlerts'] = "true"

    return options

## Remote BrowserStack - uncomment this if you want to run tests on BS
@pytest.fixture(scope='function')
def ios_driver(request, session_capabilities):
    remoteURL = "https://hub.browserstack.com/wd/hub"
    session_capabilities['browserstack.autoDismissAlerts'] = True
    driver = webdriver.Remote(remoteURL, session_capabilities)
    request.instance.driver = driver
    request.node._driver = driver
    yield driver
    driver.quit()

# Local Simulator - uncomment this if you want to run tests on iOS Simulator
# @pytest.fixture(scope='function')
# def ios_driver():
#     appium_service = AppiumService()
#     appium_service.start()
#
#     # configure port on localHost to match running Appium server e.g. 127.0.0.1/4723
#     driver = webdriver.Remote(command_executor='http://localhost:4723', desired_capabilities=appium_options_ios())
#
#     yield driver
#
#     driver.quit()
#     appium_service.stop()
