from cases.packageB import logger


def call():
    logger.error(f"Error: {__name__}")
    logger.warning(f"Warning: {__name__}")
    logger.info(f"Info: {__name__}")
    logger.debug(f"Debug: {__name__}")
