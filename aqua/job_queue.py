import logging

from queue import Queue


class JobQueue:
    def __init__(self):
        self._queue = Queue()
        logging.info('Job queue initialized successfully')
