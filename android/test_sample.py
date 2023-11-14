
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy

# @pytest.mark.usefixtures('android_driver')  # Run on local
@pytest.mark.usefixtures('setWebdriver')  # Run on BrowserStack Backend
class TestSample:

    def test_health_check(self, android_driver):
        profile_name = android_driver.find_element(AppiumBy.ID, "com.showmax.app.staging.debug:id/customTitle")
        assert profile_name.text == "Title"


