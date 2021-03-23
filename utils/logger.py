import os
import logging
import datetime as dt
from logging.handlers import TimedRotatingFileHandler
from core import root


class Logger:
    def __init__(self, log_name, log_type='DATA'):
        self.logger = logging.getLogger(log_type)
        handler = TimedRotatingFileHandler(os.path.join(*[root.ROOT_DIR, 'logs', log_name]), when='midnight', interval=1)
        handler.suffix = '%Y%m%d'
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def log_info(self, msg):
        self.logger.info(msg)

    # print message with formatting (non-logging)
    def log_message(self, msg):
        print('>>> %s : <%s>' % (dt.datetime.now(), msg))


if __name__ == '__main__':
    logger = Logger('journal.log')
