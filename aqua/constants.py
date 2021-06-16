import json

with open('config/bot.json', 'r') as f:
    raw_bot_data = f.read()

bot_data = json.loads(raw_bot_data)

BOT_TOKEN = bot_data['token']

_user_chat_id = bot_data.get('user_chat_id')
if _user_chat_id:
    USER_CHAT_ID = int(_user_chat_id)
else:
    USER_CHAT_ID = None
