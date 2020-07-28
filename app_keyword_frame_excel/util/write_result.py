import traceback

from util.parse_excel import *
from util.log import *


def write_result(pe, sheet_obj, test_result, row_no, col_no, err_msg=None, err_pic_path=None):
    # write test result:
    # if pass, font color is green; if fail, font color is red
    color_dict = {"pass": "green", "fail": "red", "": None}
    # there are time col and result col if the following three sheet, but are different
    cols_dict = {
        "test_case": [case_time_col, case_result_col],
        "test_step": [step_time_col, step_result_col],
        "test_data": [data_time_col, data_result_col]
    }

    try:
        # write test time and test result in the sheet
        if test_result == "":
            # if empty, means does not execute, clear the time and result
            info("clear the time and result column")
            pe.write_cell(sheet_obj,
                          row_no=row_no, col_no=cols_dict[col_no][0], content=test_result, style=color_dict[test_result.lower()])
            pe.write_cell(sheet_obj,
                          row_no=row_no, col_no=cols_dict[col_no][1], content=test_result, style=color_dict[test_result.lower()])
        else:
            # if not empty, write the time and result
            info("write the time and result column")
            pe.write_cell_current_time(sheet_obj, row_no=row_no, col_no=cols_dict[col_no][0], style=color_dict[test_result.lower()])
            pe.write_cell(sheet_obj, row_no=row_no, col_no=cols_dict[col_no][1], content=test_result, style=color_dict[test_result.lower()])

        if col_no == "test_step":
            # only test_step need to execute this branch
            # test step fail, need to write error msg and screencapture file path in step sheet.
            if err_msg and err_pic_path:
                # test fail, write err_msg and err_pic_path
                info("write the err_msg and err_pic_path column")
                pe.write_cell(sheet_obj, row_no=row_no, col_no=step_err_msg_col, content=err_msg, style=color_dict[test_result.lower()])
                pe.write_cell(sheet_obj, row_no=row_no, col_no=step_err_pic_path_col, content=err_pic_path, style=color_dict[test_result.lower()])

            else:
                # test pass, clear err_msg and err_pic_path
                info("clear the err_msg and err_pic_path column")
                pe.write_cell(sheet_obj, row_no=row_no, col_no=step_err_msg_col, content="", style=color_dict[test_result.lower()])
                pe.write_cell(sheet_obj, row_no=row_no, col_no=step_err_pic_path_col, content="", style=color_dict[test_result.lower()])

    except Exception as e:
        info("write excel fail: %s" % str(traceback.format_exc()))           # str()


if __name__=="__main__":
    from config.var_config import *
    pe = ParseExcel()
    pe.load_workbook(test_case_file_path)
    print(pe)
    sheet_obj = pe.get_sheet_by_name("退出")
    # write_result(pe, )
    write_result(pe, sheet_obj, "", 5, "test_step", err_msg=None, err_pic_path=None)
    # write_result(pe, sheet_obj, "pass", 5, 3, err_msg=None, err_pic_path=None)
