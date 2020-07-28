import logging
import logging.config
from config.var_config import logger_file_path


logging.config.fileConfig(logger_file_path)
logger = logging.getLogger("example02")           # or example01


def debug(message):
    logger.debug(message)


def info(message):
    logger.info(message)


def warning(message):
    logger.warning(message)


def error(message):
    logger.error(message)


if __name__ == "__main__":
    warning("aaa")