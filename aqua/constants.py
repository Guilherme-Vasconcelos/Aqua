# Copyright 2021 Guilherme-Vasconcelos
# This file is part of Aqua.
#
# Aqua is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Aqua is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Aqua.  If not, see <https://www.gnu.org/licenses/>.

import json
import logging
from typing import Optional

with open("config/bot.json", "r") as f:
    _raw_bot_data = f.read()

_bot_data = json.loads(_raw_bot_data)

BOT_TOKEN = _bot_data["token"]

_user_chat_id = _bot_data.get("user_chat_id")
if _user_chat_id:
    try:
        USER_CHAT_ID: Optional[int] = int(_user_chat_id)
    except ValueError:
        logging.warn(
            f"Your user_chat_id '{_user_chat_id}' could not be casted to an integer. "
            "Bot is assumed to be public, so everyone will be able to message Aqua. "
            "If you want to change this behaviour, ensure you have a valid user_chat_id."
        )
        USER_CHAT_ID = None
else:
    USER_CHAT_ID = None
