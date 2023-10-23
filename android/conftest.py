import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

## Android
#
# Values based on documentation https://appium.readthedocs.io/en/stable/en/writing-running-appium/caps/
def appium_options_android():
    options = {
        "platformName": "android",
        "appium:deviceName": "Pixel_XL_API_34",  # Name of the Emulator
        "appium:automationName": "UiAutomator2",
        "appium:app": "/Users/tomaskral/Workspace/ShowMax/android-showmax-main/app/build/intermediates/apk/staging/debug/app-staging-debug.apk",
        "appium:allowTestPackages": "true",
    }
    return options

## Remote BrowserStack - uncomment this if you want to run tests on BS
# @pytest.fixture(scope='function')
# def android_driver(request, session_capabilities):
#     remoteURL = "https://hub.browserstack.com/wd/hub"
#     driver = webdriver.Remote(remoteURL, session_capabilities)
#     request.node._driver = driver
#     request.instance.driver = driver
#     yield driver
#     driver.quit()


# Local BrowserStack - uncomment this if you want to run tests on iOS Simulator
@pytest.fixture(scope='function')
def driver():
    appium_service = AppiumService()
    appium_service.start()

    driver = webdriver.Remote(command_executor='http://localhost:4723', desired_capabilities=appium_options_android())

    yield driver

    driver.quit()
    appium_service.stop()