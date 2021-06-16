from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.extensions.checks import is_authorized


def start(update: Update, context: CallbackContext):
    if not is_authorized(update):
        return

    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome!")
