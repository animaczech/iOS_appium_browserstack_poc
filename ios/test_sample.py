import pytest
from appium.webdriver.common.mobileby import MobileBy
import Locators

@pytest.mark.usefixtures('ios_driver')
class TestSample_iOS:
    def test_health_check(self, ios_driver):
        logo = Helpers_iOS().getElement(ios_driver, "logo_image")
        assert logo.is_displayed()

    def test_login_screen(self, ios_driver):
        elements = ["welcome_message", "username_input", "password_input", "login_button", "login_button_for_debug"]

        for element in elements:
            assert Helpers_iOS().getElement(ios_driver,element).is_displayed()

    def test_successful_login(self, ios_driver):
        username_field = Helpers_iOS().getElement(ios_driver, "username_input")
        password_field = Helpers_iOS().getElement(ios_driver, "password_input")
        login_button = Helpers_iOS().getElement(ios_driver, "login_button")

        username_field.send_keys("apple")
        password_field.send_keys("laxative98d#2")

        login_button.click()

        assert Helpers_iOS().isElementVisible(ios_driver, "current_time")


@pytest.mark.usefixtures('ios_driver')
class Helpers_iOS:
    def getElement(self, ios_driver, accessibilityID):
        try:
            return ios_driver.find_element(MobileBy.ACCESSIBILITY_ID, accessibilityID)
        except:
            return None

    def isElementVisible(self, ios_driver, accessibilityID):
        element = self.getElement(ios_driver, accessibilityID)
        return element.is_displayed()

    def scrollToElement(self, ios_driver, accessibilityID, maxCount = 10):
        # Find the element by accessibility ID
        element = self.getElement(ios_driver, accessibilityID)
        # Check if the element is visible on the screen
        if element is None or not element.is_displayed():
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
            while True:
                element = self.getElement(ios_driver, accessibilityID)
                if element is not None and element.is_displayed() or count > maxCount:
                    return element
                ios_driver.swipe(start_x, start_y, end_x, end_y, duration=1000)
                count += 1
        # Return the element
        return element
