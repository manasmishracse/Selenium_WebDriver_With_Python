from selenium import webdriver

driver = webdriver.Chrome("C:\\Browser Executable File\\chromedriver.exe")

# Syntax for Css:
# "tagname[attribute='value']"

# Syntax for Xpath:
# "//tagname[@attribute='value']"

# Syntax for Reg-ex CSS:
# "tagname[attribute*='value']"

# Syntax for Reg-ex Xpath:
# //*[contains(@attribute,'value']

driver.get("https://automate.io")

# To get Text DATA
print(driver.find_element_by_css_selector("div[class='banner_left']").text)