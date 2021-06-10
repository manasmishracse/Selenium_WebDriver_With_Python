import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# Defining Some List:
BlIST = []
BlIST2 = []
EList = ["Cauliflower - 1 Kg", "Strawberry - 1/4 Kg", "Water Melon - 1 Kg", "Cashews - 1 Kg", "Walnuts - 1/4 Kg"]
AList = []

# Invoking Browser:
driver = webdriver.Chrome("C:\\Browser Executable File\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Verifying Search Page in Home:
driver.find_element_by_class_name("search-keyword").send_keys("w")
time.sleep(3)
Name = driver.find_elements_by_xpath("//div[@class='product-action']/button/parent::div/parent::div/h4")

for Veg in Name:
    AList.append(Veg.text)

print(AList)

assert AList == EList

# Clearing Value in Search Box
driver.find_element_by_class_name("search-keyword").clear()

# Going to Search a Veggies form Search
driver.find_element_by_class_name("search-keyword").send_keys("b")
# Taking out the Veggies Button(Add to Cart)
time.sleep(3)
Buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
# //div[@class='product-action']/button/parent::div/parent::div/h4

# Clicking all ADD TO CARD Button
for button in Buttons:
    button.click()
# Taking out Veggies Name
    BlIST.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)

print(len(BlIST))
print(BlIST)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# Moving to Next Page
driver.implicitly_wait(3)

# Making a List for Veggies in Page 2
# P_Veg = driver.find_elements_by_xpath("//p[@class='product-name']")

P_Veg = driver.find_elements_by_css_selector("p.product-name")
print(len(P_Veg))
for Veg in P_Veg:
    BlIST2.append(Veg.text)

print(BlIST2)

# Verifying both List
# assert BlIST == BlIST2

# Grabbing the Total Amount for Each Veggies and Summing the Price
Price = driver.find_elements_by_xpath("//tr/td[5]/p")
Sum = 0
for Veg in Price:
    Sum = Sum + int(Veg.text)

print(Sum)

# Verifying Sum of veggies and Total amount at UI
Total_Amount = int(driver.find_element_by_css_selector("[class='totAmt']").text)

assert Total_Amount == Sum

# Entering Promo Code
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("[class='promoBtn']").click()

# Applying Some Explicit wait for Promo code to apply
wait = WebDriverWait(driver, 5)
# 3 Import Apply here
wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))

# Verifying Discount as been Applied or not
Success_Msg = driver.find_element_by_class_name("promoInfo").text
print(Success_Msg)
Discount_Amt = driver.find_element_by_class_name("discountAmt").text
assert float(Discount_Amt) < Total_Amount


# Placing Order:
driver.find_element_by_xpath("//button[text()='Place Order']").click()

# DropBox to Select(Static)
Obj = Select(driver.find_element_by_xpath("//select[@style='width: 200px;']")).select_by_value("India")


# Clicking on Link(Terms and Condition)
driver.find_element_by_link_text("Terms & Conditions").click()

# Switching Window
Parent_Window_ID = driver.window_handles[0]
Child_Window_ID = driver.window_handles[1]

driver.switch_to.window(Child_Window_ID)

# Going Back to Home Page:
driver.find_element_by_link_text("Home").click()
driver.close()

# Go Back to T&C Page:
driver.switch_to.window(Parent_Window_ID)
# Clicking on CheckBox and Proceed:
driver.find_element_by_xpath("//input[@type='checkbox']").click()
driver.find_element_by_xpath("//button[text() = 'Proceed']").click()

C_URL = driver.current_url

assert C_URL == "https://rahulshettyacademy.com/seleniumPractise/#/country"

# Applying Wait for the URL to Move Home Page

wait = WebDriverWait(driver, 10)
wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@class='search-keyword']")))

# Once URL is moved to Home Page, Assert for the same

C2_URL = driver.current_url
assert C2_URL == "https://rahulshettyacademy.com/seleniumPractise/#/"

print("All Testcases Passed!")
driver.quit()
