import logging

import click

from aqua.async_utils import add_to_event_loop_before_start, start_event_loop
from aqua.bot import Bot
from aqua.constants import BOT_TOKEN


@click.command()
@click.option('--debug', '-d', default=False, help='Debug mode', is_flag=True)
def main(debug: bool) -> None:
    bot = Bot(BOT_TOKEN)
    logging.debug('Setting up event loop for Job Queue and Bot.')

    add_to_event_loop_before_start(bot.start_polling)

    logging.debug('Starting to run event loop tasks.')
    start_event_loop()


if __name__ == '__main__':
    main()
