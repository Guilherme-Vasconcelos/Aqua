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
from typing import NoReturn

import click

from aqua.async_utils import add_to_event_loop_before_start, start_event_loop
from aqua.bot import Bot
from aqua.constants import BOT_TOKEN


@click.command()
@click.option('--debug', '-d', default=False, help='Debug mode', is_flag=True)
def main(debug: bool) -> NoReturn:
    bot = Bot(BOT_TOKEN)
    logging.debug('Setting up event loop for Job Queue and Bot.')

    add_to_event_loop_before_start(bot.start_polling)

    logging.debug('Starting to run event loop tasks.')
    start_event_loop()


if __name__ == '__main__':
    main()
