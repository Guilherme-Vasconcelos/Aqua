# Copyright 2021 Guilherme-Vasconcelos
# This file is part of Aqua.
#
# Aqua is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Aqua is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Aqua.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
import pickle

from queue import Queue
from time import time
from typing import Callable, NoReturn

JOB_QUEUE_DUMP_FILE = '.job_queue_cache'


class JobQueue:
    def __init__(self, job_queue_delay: int):
        self._queue: Queue = Queue()
        self._job_queue_delay = job_queue_delay
        logging.debug(f'Job queue initialized successfully with delay set to {self._job_queue_delay}.')

    def append_job(self, job: Callable, schedule: float) -> None:
        """
        Appends a job to be executed by the instance of JobQueue.

        Parameters
        ----------
        job: Callable
            The function which will be executed
        schedule: float
            When to execute the function. Precisely, this must be a time in milisseconds. Your job will be executed
            if a call to time.time() is greater than or equal to `schedule`.

        See Also
        --------
        time.time
        """
        logging.debug(
            f'Appending job \'{job.__name__}\', which is scheduled to {schedule}.'
        )

        self._queue.put({
            'job': job,
            'schedule': schedule
        })

    async def begin_executing(self) -> NoReturn:
        """Starts executing the Job Queue."""
        while True:
            if self._queue.empty():
                logging.debug(
                    'Job queue attempted to execute available jobs, but there are none. '
                    f'Attempting again in {self._job_queue_delay} seconds.'
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

                logging.debug('Finished executing available jobs. Creating .job_queue_cache.')
                self.dump_to_file()

            await asyncio.sleep(self._job_queue_delay)

    def dump_to_file(self):
        """Dumps the Job Queue to a file if it is not empty."""
        if not self._queue.empty():
            with open(JOB_QUEUE_DUMP_FILE, 'wb') as f:
                pickle.dump(self._queue, f)  # FIXME: pickle does not seem to be able to dump _queue.

    def __repr__(self) -> str:
        # FIXME: it would be better to show the entire function (to be executed) instead of
        # only its name. However, I could not get `inspect.getsource` to work here, so we
        # will have to go with only the function name for now.
        if self._queue.empty():
            return '[]'

        _repr = '[\n'

        for job in self._queue.queue:
            _repr += '    {\n'
            _repr += f'       job: {job["job"].__name__}\n'
            _repr += f'       schedule: {job["schedule"]}\n'
            _repr += '    }'

            _repr += ',\n'
        _repr += ']'

        return _repr
