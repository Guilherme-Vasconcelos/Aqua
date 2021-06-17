import asyncio
import logging

from typing import Callable


def add_to_event_loop_before_start(func: Callable) -> None:
    logging.debug(f'Adding \'{func.__name__}\' to event loop.')
    event_loop = asyncio.get_event_loop()
    if event_loop.is_running():
        logging.critical(f'Could not add \'{func.__name__}\' to event loop: it is already running.')
    else:
        event_loop.create_task(func())


def start_event_loop() -> None:
    logging.info('Started event loop.')
    event_loop = asyncio.get_event_loop()
    event_loop.run_forever()
