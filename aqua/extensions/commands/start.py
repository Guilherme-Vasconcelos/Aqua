from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize
from aqua.utils import logged_send_message


@authorize
def start(update: Update, context: CallbackContext) -> None:
    message_to_send = 'Welcome!'
    logged_send_message(update, context, message_to_send)
