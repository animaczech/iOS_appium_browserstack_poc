import pytest
from appium.webdriver.common.mobileby import MobileBy
import Locators

@pytest.mark.usefixtures('ios_driver')
class TestSample_iOS:
    def test_health_check(self, ios_driver):
        item = Helpers_iOS().scrollToElement(ios_driver, "home_row")
        assert item.is_displayed()

@pytest.mark.usefixtures('ios_driver')
class Helpers_iOS:
    def getElement(self, ios_driver, accessibilityID):
        return ios_driver.find_element(MobileBy.ACCESSIBILITY_ID, accessibilityID)

    def isElementVisible(self, ios_driver, accessibilityID):
        element = self.getElement(ios_driver, accessibilityID)
        return element.is_displayed()

    def scrollToElement(self, ios_driver, accessibilityID, maxCount = 10):
        # Find the element by accessibility ID
        element = self.getElement(ios_driver, accessibilityID)
        # Check if the element is visible on the screen
        if not element.is_displayed():
            # If not, use the driver's swipe method to perform a swipe gesture until the element is visible
            # Get the screen size
            size = ios_driver.get_window_size()
            # Calculate the start and end coordinates for the swipe gesture
            start_x = size["width"] // 2
            start_y = size["height"] * 0.8
            end_x = start_x
            end_y = size["height"] * 0.2
            # Perform the swipe gesture until the element is visible or a maximum of 10 times
            count = 0
            while not element.is_displayed() and count < maxCount:
                ios_driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
                count += 1
        # Return the element
        return element