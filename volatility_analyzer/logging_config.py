"""
# @ Author: Meet Patel
# @ Create Time: 2026-01-01 11:43:04
# @ Modified by: Meet Patel
# @ Modified time: 2026-01-01 13:21:59
# @ Description: Centralized logging configuration
"""

import logging
import sys
from logging import handlers


def setup_logging(level=logging.INFO, stream=sys.stdout):
    """
    Set up logging for the application.

    Args:
        level: The logging level to set for the root logger.
        stream: The output stream for the logs (e.g., sys.stdout, sys.stderr).
    """

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create a handler and set the formatter
    handler = logging.StreamHandler(stream)
    handler.setFormatter(formatter)

    # Add the handler to the logger
    # Clear existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)


def get_logger(name):
    """
    Get a logger with the specified name.

    Args:
        name: The name of the logger.

    Returns:
        A logger instance.
    """
    return logging.getLogger(name)


# Example usage:
if __name__ == "__main__":
    setup_logging(level=logging.DEBUG)

    logger = get_logger(__name__)

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
