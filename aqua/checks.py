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

import logging

from functools import wraps
from typing import Callable

from telegram import Update, Chat

from aqua.constants import USER_CHAT_ID


def is_authorized(update: Update) -> bool:
    """
    Checks if a Telegram update came from an authorized user.

    Parameters
    ----------
    update: telegram.Update

    Returns
    -------
    bool
        Whether the user is authorized or not.

    Notes
    -----
    If user has not set their user_chat_id, this function will always return true, because in this
    case Aqua is assumed to be a public bot.

    See Also
    --------
    aqua.checks.authorize
    """
    chat = update.effective_chat
    if not isinstance(chat, Chat):
        return False

    if chat.id == USER_CHAT_ID:
        logging.info(f'Authorizing user: {chat.id}.')
        return True

    if USER_CHAT_ID is None:
        logging.warn(
            f'Received a message from \'{chat.id}\', but user_chat_id is None. '
            'Bot is assumed to be public, so user will be authorized. If you want '
            'to change this behaviour, set up a user_chat_id in config/bot.json.'
        )

        return True

    logging.warn(f'Unauthorizing invalid user: {chat.id}.')
    return False


def authorize(command: Callable) -> Callable:
    """
    A decorator meant to be used to easily authorize new functions.

    Parameters
    ----------
    command : Callable
        Your command function, which should receive as parameters a telegram.Update and
        a telegram.ext.callbackcontext.CallbackContext.

    Returns
    -------
    Callable
        A function that executes:
            - Your original command if the user is authorized; or
            - Nothing if the user is not authorized.

    See Also
    --------
    aqua.checks.is_authorized
    """
    @wraps(command)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == Update:
                if is_authorized(arg):
                    return command(*args, **kwargs)
                return
        logging.error(
            f'Could not find an Update in authorized function: \'{command.__name__}\'. '
            'Are you sure it is a valid Telegram command?'
            'Assuming user not authorized.'
        )
        return

    return wrapper
