import pytest
import os
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


# Values based on documentation https://appium.readthedocs.io/en/stable/en/writing-running-appium/caps/
def appium_options_android():
    options = {
        "platformName": "android",
        "appium:deviceName": "EMULATOR_NAME",  # Name of the Emulator
        "appium:automationName": "UiAutomator2",
        "appium:app": "/PATH_TO_APK/APK_NAME.apk",
        "appium:allowTestPackages": "true",
        "appium:autoGrantPermissions": "true",
    }
    return options


@pytest.fixture(scope='function')
def android_driver():
    appium_service = AppiumService()
    appium_service.start()

    driver = webdriver.Remote(command_executor='http://localhost:4723', desired_capabilities=appium_options_android())

    yield driver

    driver.quit()
    appium_service.stop()


@pytest.fixture(scope='function')
def setWebdriver(request, session_capabilities):
    remoteURL = "https://hub.browserstack.com/wd/hub"
    driver = webdriver.Remote(remoteURL, session_capabilities)
    request.node._driver = driver
    request.instance.driver = driver
    yield driver
    driver.quit()
