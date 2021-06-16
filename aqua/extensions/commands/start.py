from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize


@authorize
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome!")
