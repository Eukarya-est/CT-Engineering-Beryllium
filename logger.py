import logging
from logging.handlers import RotatingFileHandler

# Info logger   
INFO_LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
INFO_LOG_LEVEL = logging.INFO

INFO_LOG_FILE = "./logs/INFO.log"

info_logger_formatter = logging.Formatter(INFO_LOG_FORMAT)
info_logger = logging.getLogger("string_changer.info")
info_logger.setLevel(INFO_LOG_LEVEL)
info_logger_file_handler = RotatingFileHandler(INFO_LOG_FILE, maxBytes=1024 * 1024, backupCount=1)
info_logger_file_handler.setFormatter(info_logger_formatter)
info_logger.addHandler(info_logger_file_handler)

# Warning logger
WARNING_LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
WARNING_LOG_LEVEL = logging.WARNING

WARNING_LOG_FILE = "./logs/WARNING.log"

warning_logger_formatter = logging.Formatter(WARNING_LOG_FORMAT)
warning_logger = logging.getLogger("string_changer.waring")
warning_logger.setLevel(WARNING_LOG_LEVEL)
warning_logger_file_handler = RotatingFileHandler(WARNING_LOG_FILE, maxBytes=1024 * 1024)
warning_logger_file_handler.setFormatter(warning_logger_formatter)
warning_logger.addHandler(warning_logger_file_handler)

# Error logger
ERROR_LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
ERROR_LOG_LEVEL = logging.ERROR

ERROR_LOG_FILE = "./logs/ERROR.log"

error_logger_formatter = logging.Formatter(ERROR_LOG_FORMAT)
error_logger = logging.getLogger("string_changer.error")
error_logger.setLevel(ERROR_LOG_LEVEL)
error_logger_file_handler = RotatingFileHandler(ERROR_LOG_FILE, maxBytes=1024 * 1024)
error_logger_file_handler.setFormatter(error_logger_formatter)
error_logger.addHandler(error_logger_file_handler)