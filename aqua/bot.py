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

import glob
import importlib
import logging

from os.path import dirname, basename, isfile, join
from typing import Callable

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from aqua.extensions.talk.talk import talk as talk_handler_command
from aqua.utils import has_flag

if not has_flag('help'):
    logging_level = logging.DEBUG if has_flag('debug') else logging.INFO
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Dynamically importing all command extensions
command_extensions_files = glob.glob(join(dirname(__file__) + '/extensions/commands', "*.py"))
command_extensions = [
    basename(f)[:-3] for f in command_extensions_files if isfile(f) and not f.endswith('__init__.py')
]

command_functions = {}
for command_extension in command_extensions:
    module = importlib.import_module(f'aqua.extensions.commands.{command_extension}')
    command_function = getattr(module, command_extension)
    command_functions[command_extension] = command_function


class Bot:
    def __init__(self, token: str) -> None:
        logging.debug('Creating bot instance.')
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

    def commands_with_aliases(self, command_functions: dict[str, Callable]) -> dict[str, Callable]:
        return command_functions

    async def start_polling(self) -> None:
        """Start polling Telegram for bot updates."""
        for command_trigger, command in self.commands_with_aliases(command_functions).items():
            handler = CommandHandler(command_trigger, command)
            self.dispatcher.add_handler(handler)

            logging.info(f'Successfully loaded command trigger \'{command_trigger}\' to \'{command.__name__}\'')

        talk_handler = MessageHandler(Filters.text & (~Filters.command), talk_handler_command)
        self.dispatcher.add_handler(talk_handler)
        logging.debug('Successfully loaded the talk handler.')

        logging.info('Starting bot.')
        self.updater.start_polling()
