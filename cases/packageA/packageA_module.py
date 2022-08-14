import logging
from cases.packageA import logger


def call():
    logger.error(f"Error: {__name__}")
    logger.warning(f"Warning: {__name__}")
    logger.info(f"Info: {__name__}")
    logger.debug(f"Debug: {__name__}")


class ClassA:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def method(self):
        self.logger.error(f"Error: {self.__class__.__name__}")
        self.logger.warning(f"Warning: {self.__class__.__name__}")
        self.logger.info(f"Info: {self.__class__.__name__}")
        self.logger.debug(f"Debug: {self.__class__.__name__}")

