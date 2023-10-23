from browserstack.local import Local
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('driver')
class TestSample:

    def test_health_check(self, driver):
        assert driver.find_element("id", "Showmax")

