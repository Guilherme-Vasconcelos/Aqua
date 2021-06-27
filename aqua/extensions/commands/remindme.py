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

from time import time

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.async_utils import add_to_event_loop_before_start
from aqua.checks import authorize, ensure_telegram_number_args
from aqua.job_queue import JobQueue
from aqua.utils import logged_send_message

remindme_job_queue = JobQueue(15)

add_to_event_loop_before_start(remindme_job_queue.begin_executing)


@authorize
@ensure_telegram_number_args(3, 'min')
def remindme(update: Update, context: CallbackContext) -> None:
    args = context.args
    delay_amount, delay_unit, *reminder = args

    multiply_factors = {'minute': 60, 'hour': 60 * 60, 'day': 60 * 60 * 24}
    multiply_factor = multiply_factors.get(delay_unit)

    if multiply_factor is None:
        logged_send_message(
            update,
            context,
            'Unsupported unit! Please pick between "minute", "hour" or "day".'
        )

        return

    try:
        when_to_execute_task = time() + multiply_factor * float(delay_amount)
    except ValueError:
        logged_send_message(
            update,
            context,
            f'Sorry, I could not understand what the value \'{delay_amount}\' means.'
            ' Try again!'
        )

        return

    def job():
        text_to_send = f'Hello! Here is your reminder: {" ".join(reminder)}'
        logged_send_message(update, context, text_to_send)

    remindme_job_queue.append_job(job, when_to_execute_task)
    logged_send_message(
        update, context, f'Okay! I will remind you in {delay_amount} {delay_unit}(s).'
    )
