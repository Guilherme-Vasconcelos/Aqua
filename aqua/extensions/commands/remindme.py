from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize


@authorize
def remindme(update: Update, context: CallbackContext):
    print(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Reminding :D!")
