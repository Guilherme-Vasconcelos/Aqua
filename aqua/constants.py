import json
import logging

with open('config/bot.json', 'r') as f:
    raw_bot_data = f.read()

bot_data = json.loads(raw_bot_data)

BOT_TOKEN = bot_data['token']

_user_chat_id = bot_data.get('user_chat_id')
if _user_chat_id:
    try:
        USER_CHAT_ID = int(_user_chat_id)
    except ValueError:
        logging.warn(
            f'Your user_chat_id \'{_user_chat_id}\' could not be casted to an integer. '
            'Bot is assumed to be public, so everyone will be able to message Aqua. '
            'If you want to change this behaviour, ensure you have a valid user_chat_id.'
        )
        USER_CHAT_ID = None
else:
    USER_CHAT_ID = None
