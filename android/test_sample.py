
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('android_driver')
class TestSample:

    def test_start_app(self):
        time.sleep(10)

