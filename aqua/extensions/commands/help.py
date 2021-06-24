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

from aqua.checks import authorize
from aqua.utils import logged_send_message


@authorize
def help(update: Update, context: CallbackContext) -> None:
    msg = 'Hello! Here are the commands I am able to run:\n\n'

    msg += '/help - display this message\n\n'

    msg += '/lorem - generate one paragraph of Lorem Ipsum text\n\n'

    msg += '/remindme <time> <time_unit> <message> - get yourself a reminder about <message> '
    msg += 'after the specified time\n\n'

    msg += '/sort <list of elements> - sort your elements, either alphabetically or numerically '
    msg += 'depending on their type. For example: `/sort 1 5 2` or `/sort myword1 second_word`\n\n'

    msg += '/start - send a welcome message\n\n'

    msg += '/whatis <search query> - gives you a brief summary about your search. '
    msg += 'For example: /whatis linux kernel\n\n'

    msg += 'Learn more at: https://github.com/Guilherme-Vasconcelos/Aqua'

    logged_send_message(update, context, msg)
