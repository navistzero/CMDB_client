import logging
from lib.conf.config import settings

class Logger():

    def __init__(self, name, path, level=logging.DEBUG):
        file_handler = logging.FileHandler(path, 'a', encoding='utf-8')
        fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
        file_handler.setFormatter(fmt)

        self.logger = logging.Logger(name, level=level)
        self.logger.addHandler(file_handler)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)


logger = Logger(settings.LOG_NAME, settings.LOG_FILE_PATH)