import time, os

from config.var_config import screen_capture_dir_path


def get_current_date():
    # get current date via strftime
    current_date = time.strftime("%Y-%m-%d")
    return current_date


def get_current_time():
    # get current time via strftime
    current_time = time.strftime("%H-%M-%S")
    return current_time


def create_current_date_dir():
    # create directory to save screencapture
    dir_name =os.path.join(screen_capture_dir_path, get_current_date())
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name




