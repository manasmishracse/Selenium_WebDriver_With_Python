# Import for the Selenium
from selenium import webdriver

# To Invoke the Browser
driver = webdriver.Chrome(executable_path="C:\\Browser Executable File\\chromedriver.exe")

# TO Maximize the Window(Always use above the get call)
driver.maximize_window()
driver.get("https://automate.io")

# To find the Title of the Page we have Landed
print("Title of the URL is: " + driver.title)

driver.get("https://automate.io/integrations")

# To find the Current URL we are present
print("{} {}".format("URL of Page 2 is ", driver.current_url))

# To go back to the previous Url we were on
driver.back()

# To Refresh the URL Or page
driver.refresh()

# To Minimise
driver.minimize_window()

driver.close()

# To Quit (Closes Current and Child Window as well)
# driver.quit()

