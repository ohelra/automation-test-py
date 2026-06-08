import configparser
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(ROOT_DIR, 'configurations', 'config.ini')
config = configparser.RawConfigParser()
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_urls():
        return config.get('common', 'urls')

    @staticmethod
    def get_email():
        return config.get('credentials', 'email')

    @staticmethod
    def get_password():
        return config.get('credentials', 'password')