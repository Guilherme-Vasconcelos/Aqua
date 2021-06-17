import logging

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize


@authorize
def start(update: Update, context: CallbackContext) -> None:
    message_to_send = 'Welcome!'
    chat_to_send = update.effective_chat.id
    logging.info(f'Sending message \'{message_to_send}\' to authorized user \'{chat_to_send}\'')
    context.bot.send_message(chat_id=chat_to_send, text=message_to_send)
