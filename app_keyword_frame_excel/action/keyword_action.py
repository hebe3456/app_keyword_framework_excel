import time
from appium import webdriver

from util.get_desired_caps import get_desired_caps_info
from util.object_map import *
from util.gen_dir_and_time import *

driver = ""

def open_app():
    global driver
    try:
        desired_caps = get_desired_caps_info()
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    except Exception as e:
        raise e


def open_start_activity(app_name, start_activity_name):
    global driver
    try:
        driver.start_activity(app_name, start_activity_name)
    except Exception as e:
        raise e


def quit_server():
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e


def input_string(locate_type, locate_exp, input_content):
    # input content
    global driver
    try:
        get_element(driver, locate_type, locate_exp).send_keys(input_content)
    except Exception as e:
        raise e


def clear_input_field(locate_type, locate_exp, *args):           #
    # clear the input field
    global driver
    try:
        get_element(driver, locate_type, locate_exp).clear()
    except Exception as e:
        raise e


def click(locate_type, locate_exp, *args):
    # click a button
    global driver
    try:
        get_element(driver, locate_type, locate_exp).click()
    except Exception as e:
        raise e


def assert_in_pagesource(assert_content, *args):
    # assert page source exists expect content
    global driver
    try:
        assert assert_content in driver.page_source, "%s not found in page source" % assert_content
    except Exception as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


def sleep(sleep_second, *args):
    # wait
    try:
        time.sleep(int(sleep_second))
    except Exception as e:
        raise e


def screen_capture(*args):                 #
    # screen capture
    global driver
    # get current time, s
    current_time = get_current_time()
    screen_capture_file_path = create_current_date_dir() + "\\" + current_time + ".png"
    try:
        # save the screen capture to local
        driver.get_screenshot_as_file(screen_capture_file_path)
    except Exception as e:
        raise e
    else:
        return screen_capture_file_path


def assert_app_list(locate_type, locate_exp, assert_content):
    global driver
    try:
        assert_content_list = assert_content.split(",")
        elements = get_elements(driver, locate_type, locate_exp)
        for element in elements[:3]:
            assert element.text in assert_content_list
    except Exception as e:
        raise AssertionError(e)
    except Exception as e:
        raise e
