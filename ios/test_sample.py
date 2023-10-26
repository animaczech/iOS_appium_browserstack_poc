import pytest
import Locators

@pytest.mark.usefixtures('ios_driver')
class TestSample_iOS:
    def is_element_visible(self, ios_driver, element_id):
        try:
            element = ios_driver.find_element("id", element_id)
            return element.is_displayed()
        except:
            return False

    def test_home_screen_displayed(self, ios_driver):
        home_id = Locators.Locators.Home.screen
        assert self.is_element_visible(ios_driver, home_id)

    def test_health_check(self, ios_driver):
        assert ios_driver.find_element("id", "Showmax")