from traceback import print_stack
from configparser import ConfigParser
from Logs import logs_file
import os

log = logs_file.get_logs()
cur_path = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(cur_path, r"../ConfigFiles/config.ini")


def load_properties_file():
    """
    This method loads the properties/ini file
    :return: this method returns config reader instance.
    """

    config = None
    try:
        # noinspection PyBroadException
        config = ConfigParser()
        config.read(config_path)

    except Exception as ex:
        log.error("Failed to load ini/properties file.", ex)
        print_stack()

    return config


def change_properties_file(section, property_name, property_value):
    """
    This method is used to change the property value
    :param section: property section in ini file
    :param property_name: property name to change
    :param property_value: property value to set
    :return: it returns boolean value for successful change property operation
    """
    try:
        config = load_properties_file()
        config[section][property_name] = property_value

        with open(config_path, 'w') as configfile:
            config.write(configfile)

        return True

    except Exception as ex:
        log.error("Failed to change ini/properties file.", ex)
        print_stack()
        return False
