import logging


def initialize_logger():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
