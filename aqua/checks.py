import logging

from functools import wraps
from typing import Callable

from telegram import Update, Chat

from aqua.constants import USER_CHAT_ID


def is_authorized(update: Update) -> bool:
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
