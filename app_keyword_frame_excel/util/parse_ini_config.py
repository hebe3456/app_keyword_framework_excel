from configparser import ConfigParser
from config.var_config import *

# get desired_caps_config.ini info


class ParseConfig(object):
    def __init__(self, file_path):
        self.cf = ConfigParser()
        self.cf.read(file_path)

    def get_all_section_option_dict(self, section_name):
        """
        get all sections and options
        :param section_name:
        :return: dict
        """
        all_section_option = self.cf.items(section_name)
        # print(all_section_option, type(all_section_option))
        # all the letters is lower_case !!!
        [('platformname', 'Android'), ('platformversion', '5.0.2'), ('devicename', 'A2JDU16825000046'),
         ('apppackage', 'com.xsteach.appedu'), ('appactivity', 'com.xsteach.appedu.StartActivity'),
         ('unicodekeyboard', 'True'), ('autoacceptalerts', 'True'), ('resetkeyboard', 'True'), ('noreset', 'True'),
         ('newcommandtimeout', '6000')]
        # <class 'list'>
        all_section_option_dict = dict(self.cf.items(section_name))      # !!!
        return all_section_option_dict
    {'platformname': 'Android', 'platformversion': '5.0.2', 'devicename': 'A2JDU16825000046',
     'apppackage': 'com.xsteach.appedu', 'appactivity': 'com.xsteach.appedu.StartActivity', 'unicodekeyboard': 'True',
     'autoacceptalerts': 'True', 'resetkeyboard': 'True', 'noreset': 'True', 'newcommandtimeout': '6000'}

    def get_option_value_of_one_section(self, section_name, option_name):
        option_value = self.cf.get(section_name, option_name)
        return option_value


if __name__ == "__main__":
    print(desired_caps_file_path)
    pc = ParseConfig(desired_caps_file_path)
    # print(pc)            ParseConfig object
    print(pc.get_all_section_option_dict("Desired_caps"))
    print(pc.get_option_value_of_one_section("Desired_caps", "platformVersion"))

# D:\专业技术\APPIUM\RLJ_DataKeywordDrivenFrameworkForApp\config\desired_caps_config.ini
# 5.0.2