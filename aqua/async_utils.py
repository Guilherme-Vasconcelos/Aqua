import asyncio
import logging

from typing import Callable


def add_to_event_loop_before_start(func: Callable):
    logging.debug(f'Adding \'{func.__name__}\' to event loop.')
    event_loop = asyncio.get_event_loop()
    event_loop.create_task(func())


def start_event_loop():
    logging.info('Started event loop.')
    event_loop = asyncio.get_event_loop()
    event_loop.run_forever()
