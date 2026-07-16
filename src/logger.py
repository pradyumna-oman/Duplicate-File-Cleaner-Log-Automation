import logging
import os
from datetime import datetime


def setup_logger():

    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    log_path = os.path.join(
        "logs",
        f"scan_{timestamp}.log"
    )

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return log_path