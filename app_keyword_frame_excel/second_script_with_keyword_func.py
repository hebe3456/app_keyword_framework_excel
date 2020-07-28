from action.keyword_action import *


id_exp1 = ""
id_exp2 = ""
expect_result1 = "点击登录"
expect_result2 = "短信登录"

desired_caps = get_desired_caps_info()
open_app()
sleep(8)
click("id", id_exp1)
sleep(2)
assert(expect_result1)
click("id", id_exp2)
assert(expect_result2)
