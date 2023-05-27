from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import testify

SERVICE_URL = "http://py-srv:5000/"

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    @testify.setup
    def connect(self):
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities['acceptInsecureCert'] = True
        self.driver = webdriver.Remote("http://selenium:4444/wd/hub", capabilities)

    @testify.teardown
    def disconnect(self):
        self.driver.quit()

    def test_title(self):
        self.driver.get(SERVICE_URL)
        title = self.driver.title
        testify.assert_truthy('Python' in title)

    def test_visits_id(self):
        self.driver.get(SERVICE_URL)
        self.driver.implicitly_wait(5)
        element = self.driver.find_element(By.ID, "visits")
        testify.assert_truthy(element.is_displayed())
    
if __name__ == '__main__':
    testify.run()
