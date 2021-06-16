import logging

from aqua.constants import USER_CHAT_ID

from telegram import Update, Chat


def is_authorized(update: Update) -> bool:
    chat = update.effective_chat
    if not isinstance(chat, Chat):
        return False

    if chat.id == USER_CHAT_ID:
        return True

    logging.warn(f'Unauthorizing invalid user: {chat.id}')
    return False
