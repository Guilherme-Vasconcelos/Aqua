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
from typing import Callable, NoReturn

from aqua.exceptions import AquaInterruptedError


def add_to_event_loop_before_start(func: Callable) -> None:
    """
    Adds a function to the event_loop BEFORE it starts running.

    Parameters
    ----------
    func : Callable
        Your function to be indefinitely executed by the event_loop.

    Notes
    -----
    If you call this function after the event loop already started, it will not add the function,
    though it will not raise an exception (but will log a critical event in console).

    See Also
    --------
    aqua.async_utils.start_event_loop
    """
    logging.debug(f"Adding '{func.__name__}' to event loop.")
    event_loop = asyncio.get_event_loop()
    if event_loop.is_running():
        logging.critical(
            f"Could not add '{func.__name__}' to event loop: it is already running."
        )
    else:
        event_loop.create_task(func())
        logging.debug(f"Successfully added '{func.__name__}' to event loop.")


def start_event_loop() -> NoReturn:
    """
    Starts asyncio event_loop. Under normal circumstances, this function should never stop.

    Raises
    ------
    AquaInterruptedError
        If for some reason the event_loop did stop.
    """
    logging.info("Started event loop.")
    event_loop = asyncio.get_event_loop()
    event_loop.run_forever()

    raise AquaInterruptedError("Aqua's main event loop was terminated.")
