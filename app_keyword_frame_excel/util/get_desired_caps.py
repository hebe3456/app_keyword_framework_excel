from config.var_config import *
from util.parse_ini_config import ParseConfig


def get_desired_caps_info():
    pc = ParseConfig(desired_caps_file_path)         # param
    section_option_dict = pc.get_all_section_option_dict("Desired_caps")
    # print(section_option_dict)
    # print(section_option_dict["platformname"])

    desired_caps = {
        "platformName": section_option_dict["platformname"],    # platformname lower_case; both "" and '' are ok
        'platformVersion': section_option_dict['platformversion'],
        'deviceName': section_option_dict['devicename'],
        'appPackage': section_option_dict['apppackage'],
        'appActivity': section_option_dict['appactivity'],
        'unicodeKeyboard': 'True',
        'autoAcceptAlerts': 'True',
        'resetKeyboard': 'True',
        'noReset': 'True',
        'newCommandTimeout': '6000'
    }
    return desired_caps


if __name__ == "__main__":
    print(get_desired_caps_info())