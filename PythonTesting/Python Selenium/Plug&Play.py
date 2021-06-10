from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Browser Executable File\\chromedriver.exe")

driver.get("https://www.servetel.in/")
driver.maximize_window()
driver.find_element_by_xpath("//ul[contains(@id,'header')]/parent::nav [@class='header-menu desk-menu nz-clearfix']/ul/li[7]/a/span[2]").click()

driver.implicitly_wait(3)

Login_Id = driver.find_element_by_xpath("//input[@id='login_id']")


Action = ActionChains(driver)
Action.move_to_element(Login_Id).click().key_down(Keys.SHIFT).send_keys("manas").key_up(Keys.SHIFT).perform()




#Action = ActionChains(driver)
#driver.implicitly_wait(2)
#Action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#driver.get_cookies()
#driver.delete_cookie()
#driver.add_cookie()
#driver.delete_cookie("manas")
#driver.get_cookies()



#Action.send_keys(Keys.CONTROL).send_keys("a").perform()
#Action.key_down(Keys.SHIFT).key_down(Keys.ALT).send_keys("z").perform()
#Action.double_click()
#Action.context_click()
