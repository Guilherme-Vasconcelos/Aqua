from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! This is the start command")  # type: ignore
