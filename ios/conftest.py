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
    options['platformVersion'] = '17.0'  # Update this to your iOS version
    options['deviceName'] = 'CI iPhone 11'  # Update this to your device
    options['automationName'] = 'XCUITest'
    options['app'] = '/Users/davidaldorf/Desktop/showmax_bs/showmax_main.app'  # Update this to your app path
    options['newCommandTimeout'] = 360
    options['autoAcceptAlerts'] = "true"
    options['autoDismissAlerts'] = "true"
    return options

## Remote BrowserStack - uncomment this if you want to run tests on BS
# @pytest.fixture(scope='function')
# def ios_driver(request, session_capabilities):
#     remoteURL = "https://hub.browserstack.com/wd/hub"
#     driver = webdriver.Remote(remoteURL, session_capabilities)
#     request.instance.driver = driver
#     request.node._driver = driver
#     yield driver
#     driver.quit()

# Local Simulator - uncomment this if you want to run tests on iOS Simulator
@pytest.fixture(scope='function')
def ios_driver():
    appium_service = AppiumService()
    appium_service.start()

    # configure port on localHost to match running Appium server e.g. 127.0.0.1/4723
    driver = webdriver.Remote(command_executor='http://localhost:4723', desired_capabilities=appium_options_ios())

    yield driver

    driver.quit()
    appium_service.stop()



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
def android_driver():
    appium_service = AppiumService()
    appium_service.start()

    driver = webdriver.Remote(command_executor='http://localhost:4723', desired_capabilities=appium_options_android())

    yield driver

    driver.quit()
    appium_service.stop()