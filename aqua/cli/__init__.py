import asyncio
import logging

from sys import argv

import click

from aqua.bot import Bot
from aqua.constants import BOT_TOKEN
from aqua.job_queue import JobQueue


def has_flag(full_flag: str):
    if '--' + full_flag in argv:
        return True

    return '-' + full_flag[0] in argv


if not has_flag('help'):
    logging_level = logging.DEBUG if has_flag('debug') else logging.INFO
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    job_queue = JobQueue()
    bot = Bot(BOT_TOKEN)


@click.command()
@click.option('--debug', '-d', default=False, help='Debug mode', is_flag=True)
def main(debug: bool) -> None:
    logging.debug('Setting up event loop for Job Queue and Bot.')

    event_loop = asyncio.get_event_loop()
    event_loop.create_task(job_queue.begin_executing())
    event_loop.create_task(bot.start_polling())

    logging.debug('Starting to run event loop tasks.')

    event_loop.run_forever()


if __name__ == '__main__':
    main()
