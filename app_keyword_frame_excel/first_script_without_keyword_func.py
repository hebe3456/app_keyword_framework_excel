from appium import webdriver
import time

from util.get_desired_caps import *

# does not use keyword func

desired_caps = get_desired_caps_info()
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(8)
id_exp1 = ""
id_exp2 = ""
expect_result1 = "点击登录"
expect_result2 = "短信登录"

driver.find_element_by_id(id_exp1).click()
time.sleep(2)
assert expect_result1 in driver.page_source
driver.find_element_by_id(id_exp2).click()
assert expect_result2 in driver.page_source