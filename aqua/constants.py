import json

with open('config/bot.json', 'r') as f:
    raw_bot_data = f.read()

bot_data = json.loads(raw_bot_data)

BOT_TOKEN = bot_data['token']
USER_CHAT_ID = int(bot_data['user_chat_id'])
