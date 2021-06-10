import pytest
from selenium.webdriver.support.select import Select
from PythonFrameWork.TestData import Testcase2
from PythonFrameWork.Utility.BaseClass import Base


class TestManas(Base):

    def test_home(self, getData):
        log = self.getLogger()
        self.driver.find_element_by_name("name").send_keys(getData["first_name"])

        self.driver.find_element_by_name("email").send_keys(getData["last_name"])

        self.driver.find_element_by_id("exampleInputPassword1").send_keys(getData["email"])

        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id("exampleCheck1").click()
        drop = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        drop.select_by_index(0)
        self.driver.find_element_by_id("inlineRadio2").click()
        self.driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
        self.driver.refresh()
        log.critical("UI REFRESHED!!")

    @pytest.fixture(params=Testcase2.testdata.data)
    def getData(self, request):
        return request.param
