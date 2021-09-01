import sys

from loguru import logger


def setup():
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")
    logger.add("log/file_{time:YYYY-MM-DD}.log", rotation="00:00", compression="zip", backtrace=True, diagnose=True)
