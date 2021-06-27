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

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.checks import authorize, ensure_telegram_number_args
from aqua.utils import logged_send_message


@authorize
@ensure_telegram_number_args(0, 'exact')
def start(update: Update, context: CallbackContext) -> None:
    message_to_send = 'Welcome!'
    logged_send_message(update, context, message_to_send)
