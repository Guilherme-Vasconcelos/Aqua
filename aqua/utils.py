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

import logging

from sys import argv

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext


def has_flag(full_flag: str) -> bool:
    if '--' + full_flag in argv:
        return True

    return '-' + full_flag[0] in argv


def logged_send_message(update: Update, context: CallbackContext, message: str) -> None:
    chat_id = update.effective_chat.id
    logging.info(f'Sending message \'{message}\' to user \'{chat_id}\'.')

    context.bot.send_message(chat_id=chat_id, text=message)
