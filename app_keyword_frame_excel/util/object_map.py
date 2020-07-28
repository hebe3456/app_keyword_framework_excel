from selenium.webdriver.support.ui import WebDriverWait


def get_element(driver, locate_type, locate_exp):
    """
    get single page element object
    :return:
    """
    try:
        element = WebDriverWait(driver, 30).until(
            lambda x: x.find_element(by=locate_type, value=locate_exp))
        return element
    except Exception as e:
        raise e


# get some page elements
def get_elements(driver, locate_type, locate_exp):
    """
    get some page elements with same locate_type and locate_exp
    :return: list
    """
    try:
        elements = WebDriverWait(driver, 30).until(
            lambda x: x.find_elements(by=locate_type, value=locate_exp))
        return elements
    except Exception as e:
        raise e