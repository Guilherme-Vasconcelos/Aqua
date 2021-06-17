import logging

from sys import argv

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


def has_flag(full_flag: str) -> bool:
    if '--' + full_flag in argv:
        return True

    return '-' + full_flag[0] in argv


def logged_send_message(update: Update, context: CallbackContext, message: str) -> None:
    chat_id = update.effective_chat.id
    logging.info(f'Sending message \'{message}\' to user \'{chat_id}\'.')

    context.bot.send_message(chat_id=chat_id, text=message)
