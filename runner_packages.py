import logging

from cases.packageA import logger as packageA_logger, packageA_module
from cases.packageB import logger as packageB_logger, packageB_module

# define logging level to be used in this module
logging_level = logging.INFO
logging.getLogger().setLevel(logging_level)
logging.warning(f"Warning: {__name__}")
logging.info(f"Info: {__name__}")
logging.debug(f"Debug: {__name__}")  # not printed - the level of root logger is still INFO

logging.info("-" * 50)
# define logging level to be used within packageA
packageA_logger.setLevel(logging.DEBUG)
logging.info(f"Info: {__name__}")
logging.debug(f"Debug: {__name__}")  # not printed - the level of root logger is still INFO
packageA_module.call()
logging.debug(f"Debug: {__name__}")  # not printed - the level of root logger is still INFO

logging.info("-" * 50)
packageA_logger.setLevel(logging.ERROR)
packageA_module.call()  # only ERROR logged now

logging.info("-" * 50)
# define logging level to be used within packageB
logging_level = logging.INFO
packageB_logger.setLevel(logging_level)
logging.info(f"Info: {__name__}")
logging.debug(f"Debug: {__name__}")
# the last `logger.debug(f"Debug: {__name__}")` in the call() did not print
# because we have set the packageB logger to be of INFO
packageB_module.call()
