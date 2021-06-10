from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\\Browser Executable File\\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_link_text("Shop").click()

# Implicit Wait
driver.implicitly_wait(2)
print(driver.current_url)

Mobiles = driver.find_elements_by_xpath("//div[@class='card h-100']")
for mobile in Mobiles:
    Name = mobile.find_element_by_xpath("div/h4/a").text
    # Page Scroll Down Using JS
    driver.execute_script("window.scrollBy(0, 10000);")
    if Name == "Blackberry":
        # //div[@class='card h-100']/div/h4/a/parent::h4/parent::div/parent::div/div[2]/button
        mobile  .find_element_by_xpath("div/h4/a/parent::h4/parent::div/parent::div/div[2]/button").click()
        break

# Page Scroll Up Using JS
driver.execute_script("window.scrollTo(5000,0)")
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()

driver.find_element_by_css_selector("button[class*='success']").click()
driver.find_element_by_id("country").send_keys("Ind")

# Explicit Wait to handel DropDown
wait = WebDriverWait(driver, 20)

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))
Country = driver.find_elements_by_xpath("//div[@class='suggestions']/ul/li/a")
for country in Country:
    if country.text == "India":
        country.click()
        break
driver.find_element_by_xpath("//label[@for='checkbox2']").click()
driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
Success = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(Success)

assert "Success! Thank you! " in Success

# Taking Screenshot in Selenium
driver.get_screenshot_as_file("Screenshot.png")

driver.quit()





