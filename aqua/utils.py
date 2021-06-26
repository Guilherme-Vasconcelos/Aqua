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

import glob
import logging
import secrets

from os.path import join
from sys import argv
from typing import List

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


def prefix_substrings(s: str) -> List[str]:
    """
    Generates a list of substrings, all of which have the same beginning as `s`.
    For example, if s is 'foo', this function will generate ['f', 'fo', 'foo'].
    Substrings that do not share the same beginning are not generated here.

    Parameters
    ----------
    s : str
        The string to generate substrings from.

    Returns
    -------
    List[str]
        The list of substrings.
    """

    _substrings = []
    current_substring = ''
    for character in s:
        current_substring += character
        _substrings.append(current_substring)

    return _substrings


def has_flag(full_flag: str) -> bool:
    """
    Checks whether a given flag was passed to the program when executing it.

    Parameters
    ----------
    full_flag : str
        The full version of the flag. For example: '--debug'.

    Returns
    -------
    bool
        Whether `full_flag`, or a shortened version of it, was passed to the program.

    Notes
    -----
    The shortened version of the full_flag is always assumed to be a dash, then its first character.
    """
    if '--' + full_flag in argv:
        return True

    return '-' + full_flag[0] in argv


def logged_send_message(update: Update, context: CallbackContext, message: str) -> None:
    """
    Sends a Telegram message and logs it into the terminal.

    Parameters
    ----------
    update : telegram.Update
    context : telegram.ext.callbackcontext.CallbackContext
    message : str
        The message which will be sent.
    """
    chat_id = update.effective_chat.id
    logging.info(f'Sending message \'{message}\' to user \'{chat_id}\'.')

    context.bot.send_message(chat_id=chat_id, text=message)


def safe_randint(lower_bound: int, upper_bound: int) -> int:
    """
    Generates a cryptographically safe random integer.

    Parameters
    ----------
    lower_bound : int
        The inclusive lower bound for the random number.
    upper_bound : int
        The inclusive upper bound for the random number.

    Returns
    -------
    A cryptographically safe random integer in the interval [lower_bound, upper_bound].

    Notes
    -----
    Although you shouldn't need to always use this function, a random.randint secret will
    probably not pass the CI security check (by Bandit).
    Because of that, it is recommended to use `safe_randint` even if your code is not related to
    cryptography.
    """
    return secrets.choice(range(lower_bound, upper_bound + 1))


def collect_python_files_at(path: str, include_init: bool = False) -> List[str]:
    """
    Collects a list of Python files at a given directory.

    Parameters
    ----------
    path : str
        The directory in which search will be performed.
    include_init : bool
        Whether to include the __init__.py file.

    Returns
    -------
    A list of strings with the full path for each file.
    """
    files = glob.glob(join(path, '*.py'))
    if include_init:
        return files

    return list(filter(lambda f: '__init__.py' not in f, files))
