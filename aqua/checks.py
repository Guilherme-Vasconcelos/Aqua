import logging

from functools import wraps
from typing import Callable

from telegram import Update, Chat

from aqua.constants import USER_CHAT_ID


def is_authorized(update: Update) -> bool:
    chat = update.effective_chat
    if not isinstance(chat, Chat):
        return False

    if chat.id == USER_CHAT_ID or USER_CHAT_ID is None:
        logging.info(f'Authorizing user: {chat.id}.')
        return True

    logging.warn(f'Unauthorizing invalid user: {chat.id}.')
    return False


def authorize(command: Callable) -> Callable:
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
