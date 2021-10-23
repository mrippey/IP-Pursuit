import configparser

CONFIG = []


def load_yml_config() -> None:
    global CONFIG
    conf_file = ".example.yml"
    CONFIG = configparser.ConfigParser()
    CONFIG.read(conf_file)


load_yml_config()
