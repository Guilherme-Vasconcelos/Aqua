import asyncio
import logging

from queue import Queue


class JobQueue:
    def __init__(self):
        self._queue = Queue()
        logging.debug('Job queue initialized successfully.')

    async def begin_executing(self):
        while True:
            if self._queue.empty():
                logging.debug(
                    'Job queue attempted to execute available tasks, but there are none. '
                    'Attempting again in 60 seconds.'
                )
            else:
                logging.debug('Executing available tasks in job queue.')

            await asyncio.sleep(60)
