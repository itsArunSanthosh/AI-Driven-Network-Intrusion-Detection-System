import logging

logging.basicConfig(level=logging.INFO)

class Logger:
    def info(self, message: str):
        logging.info(message)

    def error(self, message: str):
        logging.error(message)