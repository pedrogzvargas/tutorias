import os
import logging


def get_logger(file_path):
    logging.basicConfig()
    log = logging.getLogger(os.path.basename(file_path))
    log.setLevel(logging.DEBUG)
    return log
