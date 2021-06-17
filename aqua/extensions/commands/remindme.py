from time import time

from telegram import Update
from telegram.ext.callbackcontext import CallbackContext

from aqua.async_utils import add_to_event_loop_before_start
from aqua.checks import authorize
from aqua.job_queue import JobQueue
from aqua.utils import logged_send_message

remindme_job_queue = JobQueue()

add_to_event_loop_before_start(remindme_job_queue.begin_executing)


@authorize
def remindme(update: Update, context: CallbackContext) -> None:
    args = context.args
    delay_amount, delay_unit, *reminder = args

    multiply_factor = None
    if delay_unit == 'minute':
        multiply_factor = 60
    elif delay_unit == 'hour':
        multiply_factor = 60 * 60
    elif delay_unit == 'day':
        multiply_factor = 60 * 60 * 24
    else:
        logged_send_message(
            update,
            context,
            'Unsupported unit! Please pick between "minute", "hour" or "day".'
        )

        return

    when_to_execute_task = time() + multiply_factor * float(delay_amount)

    def job():
        text_to_send = f'Hello! Here is your reminder: {" ".join(reminder)}'
        logged_send_message(update, context, text_to_send)

    remindme_job_queue.append_job(job, when_to_execute_task)
    logged_send_message(
        update, context, f'Okay! I will remind you in {delay_amount} {delay_unit}(s).'
    )
