import logging
from pathlib import Path

def setup_logger(log_file):
    logger = logging.getLogger('DataSplitLogger')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(fh)
    return logger

def make_dirs(*folders):
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
