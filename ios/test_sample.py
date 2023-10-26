import pytest
import Locators

@pytest.mark.usefixtures('ios_driver')
class TestSample_iOS:
    def is_element_visible(self, driver, element_id):
        try:
            element = driver.find_element("id", element_id)
            return element.is_displayed()
        except:
            return False

    def test_home_screen_displayed(self, driver):
        home_id = Locators.Locators.Home.screen
        assert self.is_element_visible(driver, home_id)

    def test_health_check(self, driver):
        assert driver.find_element("id", "Showmax")