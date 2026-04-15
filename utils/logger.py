import logging
import os

def get_logger():
    # ✅ Create logs folder if not exists
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("framework")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger