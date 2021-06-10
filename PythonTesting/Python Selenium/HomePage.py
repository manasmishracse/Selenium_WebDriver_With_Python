from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Browser Executable File\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Manas")
driver.find_element_by_name("email").send_keys("mishra.manash0@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Qwerty@123")
driver.implicitly_wait(2)
driver.find_element_by_id("exampleCheck1").click()
Drop = Select(driver.find_element_by_id("exampleFormControlSelect1")).select_by_index(0)
driver.find_element_by_id("inlineRadio2").click()
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()

# Selecting Date:
#driver.find_element_by_name("bday").click()
#wait = WebDriverWait(driver,4)
#wait.until(expected_conditions.visibility_of_element_located(By.NAME, "bday"))