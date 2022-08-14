import logging
from cases.packageA.packageA_module import ClassA

# define logging level to be used in this module
logging.getLogger().setLevel(logging.INFO)
logging.warning(f"Warning: {__name__}")
logging.info(f"Info: {__name__}")
logging.debug(f"Debug: {__name__}")  # not printed - the level of root logger is still INFO

logging.info("-" * 50)
# define logging level to be used within packageA
logging.info(f'ClassA logger: {logging.getLogger("ClassA")}')
logging.getLogger("ClassA").setLevel(logging.DEBUG)
logging.info(f"Info: {__name__}")
logging.debug(f"Debug: {__name__}")  # not printed - the level of root logger is still INFO
logging.info(f'ClassA logger: {logging.getLogger("ClassA")}')
cls = ClassA()
cls.method()
logging.debug(f"Debug: {__name__}")  # not printed - the level of root logger is still INFO

logging.info("-" * 50)
logging.getLogger("ClassA").setLevel(logging.ERROR)
logging.info(f'ClassA logger: {logging.getLogger("ClassA")}')
cls.method()  # only ERROR logged now
