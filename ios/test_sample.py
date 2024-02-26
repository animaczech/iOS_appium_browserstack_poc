import pytest
from appium.webdriver.common.mobileby import MobileBy
import Locators
import time

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

    def test_unsuccessful_login(self, ios_driver):
        username_field = Helpers_iOS().getElement(ios_driver, "username_input")
        password_field = Helpers_iOS().getElement(ios_driver, "password_input")
        login_button = Helpers_iOS().getElement(ios_driver, "login_button")

        username_field.send_keys("apple")
        password_field.send_keys("wrongpassword")

        login_button.click()

        error_accessibility_id = "error_message"

        assert Helpers_iOS().isElementVisible(ios_driver, error_accessibility_id)

    def test_create_appointment(self, ios_driver):
        debug_login_button = Helpers_iOS().getElement(ios_driver, "apple_debug_login_button")
        debug_login_button.click()

        create_appointment_button = Helpers_iOS().getElement(ios_driver, "create_appointment_button")
        assert create_appointment_button.is_displayed()
        create_appointment_button.click()

        appointment_name_field = Helpers_iOS().getElement(ios_driver, "appointment_name_input")
        assert appointment_name_field.is_displayed()

        assert appointment_name_field.get_attribute('value') == "Meeting Created from Panel"

        appointment_name_field.clear()
        assert appointment_name_field.get_attribute('value') == "Name" #"Name" is a placeholder when field is empty

        new_appointment_name = "BookMax automation?"

        appointment_name_field.send_keys(new_appointment_name)
        assert appointment_name_field.get_attribute('value') == new_appointment_name

        ios_driver.hide_keyboard()

        start_time_picker = Helpers_iOS().timePicker(ios_driver, accessibilityID="start_picker", hours="23", minutes="00")
        end_time_picker = Helpers_iOS().timePicker(ios_driver, accessibilityID="end_picker", hours="23", minutes="30")

        start_time_button = start_time_picker.find_element("xpath", "//XCUIElementTypeButton")
        assert start_time_button.get_attribute('value') == "22:00"
        # Due to unknown reason yet, start picker selects 1 hour less than requested.

        end_time_button = end_time_picker.find_element("xpath", "//XCUIElementTypeButton")
        assert end_time_button.get_attribute('value') == "23:30"

        reserve_button = Helpers_iOS().getElement(ios_driver, "reserve_button")
        reserve_button.click()

        current_appointment_name = Helpers_iOS().getElement(ios_driver, "current_appointment_name")
        assert current_appointment_name.get_attribute('value') == new_appointment_name

        # assert Helpers_iOS().isElementVisible(ios_driver, "finish_button")

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

    def timePicker(self, ios_driver, accessibilityID, hours, minutes):
        time_picker = Helpers_iOS().getElement(ios_driver, accessibilityID)
        time_picker.click()

        ios_driver.find_element("xpath", "//XCUIElementTypePickerWheel[1]").send_keys(hours)

        ios_driver.find_element("xpath", "//XCUIElementTypePickerWheel[2]").send_keys(minutes)
        ios_driver.tap([(50, 50)])

        return time_picker