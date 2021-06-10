from selenium import webdriver

# Signup to a WebPage
driver = webdriver.Chrome("C:\\Browser Executable File\\chromedriver.exe")

Expected_Url = "https://courses.rahulshettyacademy.com/"

# Syntax for Css:
# "tagname[attribute='value']"

# Syntax for Xpath:
# "//tagname[@attribute='value']"

driver.maximize_window()
driver.get("https://sso.teachable.com/secure/9521/users/sign_up?flow_school_id=9521")

driver.find_element_by_name("user[name]").send_keys("Automation_User")
driver.find_element_by_name("user[email]").send_keys("lamamor136@goqoez.com")
driver.find_element_by_name("user[password]").send_keys("Qwerty@123")
driver.find_element_by_id("user_password_confirmation").send_keys("Qwerty@123")
driver.find_element_by_css_selector("input[type='checkbox']").click()
driver.find_element_by_xpath("//input[@id='user_agreed_to_terms']").click()
driver.find_element_by_xpath("//input[@name='commit']").click()

# Current_Url = print("Landing Url Post Sign_Up : " + driver.current_url)
Current_Url = driver.current_url
if Current_Url == Expected_Url:
    print("Registration Success!")
else:
    print("Registration Failed")

driver.quit()
