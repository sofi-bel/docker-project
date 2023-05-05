from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

URL = "docker-projects-app-1:5000"


class TestSelenium:
    def setup_method(self):
        option = webdriver.FirefoxOptions()
        option.binary_location = "/firefox/firefox"
        driver_service = Service("/geckodriver")
        self.driver = webdriver.Firefox(service=driver_service, options=option)

    def test_upload_file(self):
        self.driver.get(f"http://{URL}/upload")
        self.driver.find_element(By.ID, "uploading-file").send_keys(
            "/devops-examples/EXAMPLE_APP/tests/test_file.txt"
        )
        self.driver.find_element(
            By.XPATH, "//input[@type='submit' and @value='Upload']"
        ).click()

        assert "test_file.txt uploaded" in self.driver.page_source

    def test_get_file(self):
        self.driver.get(f"http://{URL}/download/test_file.txt")

        assert "Hello Artem Azarevich" in self.driver.page_source

    def teardown_method(self):
        self.driver.close()
