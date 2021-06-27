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
from typing import Callable, Literal

from telegram import Update, Chat
from telegram.ext.callbackcontext import CallbackContext

from aqua.constants import USER_CHAT_ID
from aqua.utils import logged_send_message


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


def ensure_context_number_args(number_args: int, comparison_method: Literal['min', 'exact', 'max']) -> Callable:
    """
    Ensures the correct number of arguments were passed to the command's context.

    Parameters
    ----------
    number_args : int
        The number of arguments.
    comparison_method: Literal['min', 'exact', 'max']
        The method which will be used to check if the number of arguments are enough. For
        example, if `comparison_method` is 'min' and `number_args` is 5, then the user must pass AT
        LEAST 5 arguments, otherwise function will not be executed.

    Returns
    -------
    Callable
        A function that executes the original function if `number_args` is enough according
        to `comparison_method`, else a function that does nothing.
    """
    message_join = {'min': 'at least ', 'exact': '', 'max': 'at most '}[comparison_method]

    def decorator(function: Callable):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for arg in args:
                if type(arg) == Update:
                    update = arg
                if type(arg) == CallbackContext:
                    context = arg
                    len_args = len(arg.args)
                    if (
                        (comparison_method == 'min' and len_args >= number_args)
                        or (comparison_method == 'exact' and len_args == number_args)
                        or (comparison_method == 'max' and len_args <= number_args)
                    ):
                        return function(*args, **kwargs)

            logging.warn(
                f'Function {function.__name__} was called with {len_args} arguments, but expected {number_args}. '
                f'Comparison method used was {comparison_method} - Not executing function.'
            )
            logged_send_message(
                update, context,
                f'Sorry, this command expects {message_join}{number_args} arguments, '
                f'but received {len(context.args)} instead.'
            )
        return wrapper
    return decorator
