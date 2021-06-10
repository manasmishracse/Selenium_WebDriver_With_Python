import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from PythonFrameWork.TestData import Testcase1
from PythonFrameWork.Utility.BaseClass import Base


class TestMethod(Base):
    def test_home(self, getdata):
        log = self.getLogger()
        self.driver.find_element_by_name("name").send_keys(getdata["first_name"])

        self.driver.find_element_by_name("email").send_keys(getdata["last_name"])

        self.driver.find_element_by_id("exampleInputPassword1").send_keys(getdata["email"])

        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("exampleCheck1").click()
        drop = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        drop.select_by_index(0)
        self.driver.find_element_by_id("inlineRadio2").click()
        self.driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
        self.driver.refresh()

    @pytest.fixture(params=Testcase1.testdata2.data)
    def getdata(self, request):
        return request.param

    def test_shop(self):
        log = self.getLogger()
        self.driver.find_element_by_link_text("Shop").click()
        # Implicit Wait
        self.driver.implicitly_wait(2)
        log.info("Landed URL is:" + self.driver.current_url)
        mobiles = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for mobile in mobiles:
            name = mobile.find_element_by_xpath("div/h4/a").text
            log.info("Mobile Name Fetched:" + name)
            # Page Scroll Down Using JS
            self.driver.execute_script("window.scrollBy(0, 10000);")
            if name == "Blackberry":
                # //div[@class='card h-100']/div/h4/a/parent::h4/parent::div/parent::div/div[2]/button
                mobile.find_element_by_xpath("div/h4/a/parent::h4/parent::div/parent::div/div[2]/button").click()
                break

        # Page Scroll Up Using JS
        self.driver.execute_script("window.scrollTo(5000,0)")
        self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

        self.driver.find_element_by_css_selector("button[class*='success']").click()
        self.driver.find_element_by_id("country").send_keys("Ind")

        # Explicit Wait to handle DropDown
        wait = WebDriverWait(self.driver, 20)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
        count = self.driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
        for country in count:
            if country.text == "India":
                country.click()
                break
        self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
        success = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
        log.info("Message received at UI:" + success)

        assert "Success! Thank you! " in success

        # Taking Screenshot in Selenium
        self.driver.get_screenshot_as_file("Screenshots/Screenshot.png")
