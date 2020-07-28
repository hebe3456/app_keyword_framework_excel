import traceback

from util.parse_excel import ParseExcel
from config.var_config import *
from action.keyword_action import *
from util.write_result import *
from util.log import *


def main():
    try:
        pe = ParseExcel()
        pe.load_workbook(test_case_file_path)
        case_sheet_obj = pe.get_sheet_by_name("测试用例")
        # get total case number
        total_case_num = pe.get_end_row(case_sheet_obj) - 1
        to_execute_case_col_obj = pe.get_column_obj(case_sheet_obj, case_to_execute_col)
        # define need to execute case number
        to_execute_case_num = 0
        # define sucessful case num
        sucess_case_num = 0
        for idx, to_execute_case_cell in enumerate(to_execute_case_col_obj[1:], 2):  #
            # to_execute_case_col[1:] 去掉字段行，列表是0，excel是2
            case_name = pe.get_cell_value(case_sheet_obj, row_no=idx, col_no=case_name_col)
            info("case_name: %s" % case_name)
            if to_execute_case_cell.value.lower() == "y":                    # .value
                # y, need to execute, to execute case num +1
                to_execute_case_num += 1
                case_row_obj = pe.get_row_obj(case_sheet_obj, idx)
                # case_row_obj type is list, starts with 0, so need to -1
                case_framework = case_row_obj[case_framework_col - 1].value
                case_step_sheet_name = case_row_obj[case_step_sheet_name_col - 1].value
                info("case_framework: %s, case_step_sheet_name: %s" % (case_framework, case_step_sheet_name))

                if case_framework == "关键字框架":
                    info("****************call keyword****************")
                    # get step sheet object via sheet name, all the steps must be executed
                    step_sheet_obj = pe.get_sheet_by_name(case_step_sheet_name)
                    # get total step number: max_row - 1
                    total_step_num = pe.get_end_row(step_sheet_obj) - 1
                    # define sucessful step number
                    sucess_step_num = 0

                    for step_idx in range(2, total_step_num + 2):     # ?
                        # since the first row is title, starts from the second row, so range(2, ...)
                        step_row_obj = pe.get_row_obj(step_sheet_obj, step_idx)
                        # get step description
                        step_description = step_row_obj[step_description_col - 1].value               # 数组[idx]
                        # get function name
                        step_keyword_function = step_row_obj[step_keyword_function_col - 1].value
                        # get locate type
                        step_locate_type = step_row_obj[step_locate_type_col - 1].value
                        # get locate expression
                        step_locate_exp = step_row_obj[step_locate_exp_col - 1].value
                        # get parameters
                        step_operate_data = step_row_obj[step_operate_value_col - 1].value
                        info("step_description: %s, step_keyword_function: %s, step_locate_type: %s, "
                              "step_locate_exp: %s, step_operate_data: %s"
                              % (step_description, step_keyword_function, step_locate_type, step_locate_exp,
                                 step_operate_data))

                        if isinstance(step_operate_data, int):
                            # if step operate data is int, transfer to ttr
                            step_operate_data = str(step_operate_data)

                        # contact command and execute
                        if step_keyword_function and step_locate_type and step_locate_exp and step_operate_data:
                            command = step_keyword_function + "('%s', '%s', '%s')" % (step_locate_type, step_locate_exp, step_operate_data)
                        elif step_keyword_function and step_locate_type and step_locate_exp:
                            command = step_keyword_function + "('%s', '%s')" % (step_locate_type, step_locate_exp,)
                        elif step_keyword_function and step_operate_data:
                            command = step_keyword_function + "('%s')" % step_operate_data
                        elif step_keyword_function:
                            command = step_keyword_function + "()"      # "()"

                        try:
                            info(command)
                            eval(command)
                            sucess_step_num += 1
                            write_result(pe, step_sheet_obj, "Pass", step_idx, "test_step")
                            info("step [%s] pass" % step_description)
                        except Exception as e:
                            err_pic_path = screen_capture()
                            err_msg = traceback.format_exc()
                            write_result(pe, step_sheet_obj, "Fail", step_idx, "test_step", err_msg, err_pic_path)
                            info("step [%s] fail, error msg: %s" % (step_description, err_msg))

                    # test result statistics, 缩进！！！
                    if sucess_step_num == total_step_num:
                        sucess_case_num += 1
                        write_result(pe, case_sheet_obj, "Pass", idx, "test_case")
                        info("case [%s] pass" % case_name)
                    else:
                        write_result(pe, case_sheet_obj, "Fail", idx, "test_case")
                        info("case [%s] fail" % case_name )

                elif case_framework == "数据":
                    # 可扩展
                    info("****************call data****************")
                    pass

                else:
                    write_result(pe, case_sheet_obj, "", idx, "test_case")
                    info("case [%s] does not need to execute" % case_name)

            else:
                # does not need to execute, clear the time and result column
                write_result(pe, case_sheet_obj, "", idx, "test_case")
                info("total case number: %s, need to execute %s, pass: %s" % (total_case_num, to_execute_case_num, sucess_case_num))

    except Exception as e:
        raise e


if __name__ == "__main__":
    main()