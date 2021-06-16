import logging

import click

from aqua.bot import Bot
from aqua.constants import BOT_TOKEN


@click.command()
@click.option('--debug', '-d', default=False, help='Debug mode', is_flag=True)
def main(debug: bool = False) -> None:
    logging_level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    bot = Bot(BOT_TOKEN)
    bot.start_polling()


if __name__ == '__main__':
    main()
