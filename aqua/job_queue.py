import asyncio
import logging

from queue import Queue
from time import time
from typing import Callable


class JobQueue:
    def __init__(self):
        self._queue = Queue()
        logging.debug('Job queue initialized successfully.')

    def append_job(self, job: Callable, schedule: float) -> None:
        # Schedule comes from time.time, which gives a date in milisseconds.
        logging.debug(
            f'Appending job \'{job.__name__}\', which is scheduled to {schedule}.'
        )

        self._queue.put({
            'job': job,
            'schedule': schedule
        })

    async def begin_executing(self) -> None:
        while True:
            if self._queue.empty():
                logging.debug(
                    'Job queue attempted to execute available jobs, but there are none. '
                    'Attempting again in 60 seconds.'
                )
            else:
                logging.debug('Executing available jobs in job queue.')
                new_queue: Queue = Queue()
                while not self._queue.empty():
                    now = time()
                    job = self._queue.get()
                    if now >= job['schedule']:
                        job['job']()
                    else:
                        new_queue.put(job)
                self._queue = new_queue

            await asyncio.sleep(60)
