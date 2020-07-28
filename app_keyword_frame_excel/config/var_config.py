import os

# get the abs path of the project
pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# get the abs path 0f desired_caps_config.ini
desired_caps_file_path = pro_path + "\\config\\desired_caps_config.ini"

# gen the abs path of screen capture
screen_capture_dir_path = pro_path + "\\screen_capture\\"

# the abs path of test case file
test_case_file_name = "test_data_for_appium.xlsx"
test_case_file_path = pro_path + "\\test_data\\" + test_case_file_name

# logger file path
logger_file_path = pro_path + "\\config\\logger.conf"


# 测试数据文件中，测试用例表中部分列对应的数字序号，
# 按照excel中显示的，从1开始，但是数组里从0开始，因此要-1
case_name_col=1
case_framework_col=3
case_step_sheet_name_col=4
case_data_sheet_name_col=5
case_to_execute_col=6
case_time_col=7
case_result_col=8

# 用例步骤表中，部分列对应的数字序号
step_description_col=1
step_keyword_function_col=2
step_locate_type_col=3
step_locate_exp_col=4
step_operate_value_col=5
step_time_col=6
step_result_col=7
step_err_msg_col=8
step_err_pic_path_col=9

# 数据源表中，是否执行列对应的数字编号
data_app_name_col=1
data_assert_expect_result_col=2
data_to_execute_col=3
data_time_col=4
data_result_col=5

if __name__ == "__main__":
    print(pro_path)
    print(desired_caps_file_path)
    print(screen_capture_dir_path)
    print(test_case_file_path)
    print(logger_file_path)

