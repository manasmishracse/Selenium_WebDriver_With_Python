import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\\Browser Executable File\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Radio Button Example:

# Generic CSS for all Radio Button and clicking one of those:
Radio_buttons = driver.find_elements_by_css_selector("input[class='radioButton']")
Radio_buttons[2].click()

# Selecting Radio Button Specifically anyone:
driver.find_element_by_xpath("//input[@value='radio1']").click()

# DropBox Example (Auto-Suggestive):

driver.find_element_by_id("autocomplete").send_keys("Ind")
time.sleep(2)
Countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] div")
print("{} {}".format("Number of Countries Fetched from DropDown: ", len(Countries)))

for country in Countries:
    if country.text == 'India':
        country.click()
        break

# Static DropDown by 2 Means:

Obj1 = Select(driver.find_element_by_name("dropdown-class-example")).select_by_index(1)
time.sleep(2)
Obj2 = Select(driver.find_element_by_name("dropdown-class-example")).select_by_visible_text("Option3")

# CheckBox Example:

# Selecting CheckBox specifically anyone:

# driver.find_element_by_id("checkBoxOption2").click()

# Selecting All CheckBox present:

Checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
print("{} {}".format("Number of Checkbox Fetched:", len(Checkbox)))

for check in Checkbox:
    check.click()
    assert check.is_selected()

time.sleep(1)

# Handling Java/JS Alert:

driver.find_element_by_css_selector("input#name").send_keys("Manas")
driver.find_element_by_xpath("//input[@class='btn-style'][1]").click()
alert = driver.switch_to.alert
Alert_Msg = alert.text
assert "Manas" in Alert_Msg
alert.accept()

time.sleep(1)

driver.find_element_by_css_selector("input#name").send_keys("Manas")
driver.find_element_by_xpath("//input[@class='btn-style'][2]").click()
alert = driver.switch_to.alert
Alert_Msg = alert.text
assert "Manas" in Alert_Msg

alert.dismiss()

# Handling Window Switch:
driver.find_element_by_id("openwindow").click()

Parent_ID = driver.window_handles[0]
Child_ID = driver.window_handles[1]

driver.switch_to.window(Child_ID)
C_Url = driver.current_url

assert "http://www.qaclickacademy.com/" == C_Url

driver.close()
driver.switch_to.window(Parent_ID)

# Applying Some Wait to Load:
driver.implicitly_wait(3)

# Switch Tab Example:
driver.find_element_by_link_text("Open Tab").click()

Parent_ID_tab = driver.window_handles[0]
Child_ID_tab = driver.window_handles[1]

driver.switch_to.window(Child_ID_tab)
C_Url_tab = driver.current_url

assert C_Url_tab == "https://www.rahulshettyacademy.com/#/index"
driver.close()
driver.switch_to.window(Parent_ID_tab)

# Web Table Example:

Table_Price = driver.find_elements_by_xpath("//tr/td[3]/parent::tr/parent::tbody/parent::table/parent::fieldset/table"
                                            "/tbody/tr/td[3]")
Sum_Price = 0
for price in Table_Price:
    Sum_Price = Sum_Price + int(price.text)

print("{} {}".format("Sum of Price for Web Table Example:", Sum_Price))

# Scroll Down Using JS:
driver.execute_script("window.scrollBy(0,1200);")

# Web Table Fixed Header:

Table_Amount = driver.find_elements_by_xpath("//tr/td[3]/parent::tr/parent::tbody/parent::table/parent::div/parent"
                                             "::fieldset/div[1]/table/tbody/tr/td[4]")
Total_Actual = 0
for amount in Table_Amount:
    Total_Actual = Total_Actual + int(amount.text)

print("{} {}".format("Sum of Amount in Web Table Fixed Header:", Total_Actual))

# Fetching Original Total Amount from UI
Total_Exp = driver.find_element_by_xpath("//div[text() = ' Total Amount Collected: 296 ']").text

# Making SubString
Total_Sub = Total_Exp[24:29]
print("{}{}".format("Actual Amount Fetched from UI: ", Total_Sub))

assert Total_Sub in Total_Exp

# Mouse Hover:
MouseHover = driver.find_element_by_id("mousehover")
action = ActionChains(driver)
action.move_to_element(MouseHover).perform()

# For Clicking Top
Top = driver.find_element_by_link_text("Top")
action.click(Top).perform()


time.sleep(3)
# For Clicking Reload
action.move_to_element(MouseHover).perform()
Reload = driver.find_element_by_link_text("Reload")
action.click(Reload).perform()

# Scroll Down
driver.execute_script("window.scrollBy(12000,12500);")

# Frame Handling:
Frame = driver.switch_to.frame("courses-iframe")
driver.switch_to.default_content()

# Taking ScreenShot:
driver.get_screenshot_as_file("ScreenShots/ScreenShot_Practice.png")

# Driver Quit
driver.quit()

