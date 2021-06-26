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

import importlib
import logging

from collections import Counter
from os.path import dirname, basename, isfile
from typing import Callable, List

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from aqua.extensions.talk.talk import talk as talk_handler_command
from aqua.utils import collect_python_files_at, has_flag, prefix_substrings

if not has_flag('help'):
    logging_level = logging.DEBUG if has_flag('debug') else logging.INFO
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Dynamically importing all command extensions
command_extensions_files = collect_python_files_at(dirname(__file__) + '/extensions/commands')
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
        """
        Generates aliases for all command abbreviations that are unambiguous.
        Ambiguous abbreviations will all execute the _invalid command.

        Parameters
        ----------
        command_functions : dict[str, Callable]
            A dict in which keys are the commands names (e.g. 'start', 'help'),
            and the values are the functions to be executed (e.g. aqua.extensions.commands.start)

        Returns
        -------
        dict[str, Callable]
            A dict with the same structure that was described for `command_functions`, however with
            added keys (which are the aliases).
        """

        invalid_command = command_functions['_invalid']

        # Step 1: generate the dict of commands and their respective aliases
        potentially_ambiguous_commands: dict[str, List[str]] = {}
        for command_trigger, command in command_functions.items():
            if command_trigger.startswith('_'):
                # Internal commands (which begin with '_') do not have aliases.
                list_of_aliases = [command_trigger]
            else:
                list_of_aliases = prefix_substrings(command_trigger)
            potentially_ambiguous_commands[command_trigger] = list_of_aliases

        # Step 2: collect ambiguous values, these will point to _invalid
        seen_aliases = []
        for list_of_aliases in potentially_ambiguous_commands.values():
            for alias in list_of_aliases:
                seen_aliases.append(alias)
        ambiguous_aliases = [item for item, count in Counter(seen_aliases).items() if count > 1]

        # Step 3: generate the actual dict of commands
        _command_functions: dict[str, Callable] = {}
        for command_trigger, list_of_aliases in potentially_ambiguous_commands.items():
            for alias in list_of_aliases:
                if alias in ambiguous_aliases:
                    _command_functions[alias] = invalid_command
                else:
                    _command_functions[alias] = command_functions[command_trigger]

        return _command_functions

    async def start_polling(self) -> None:
        """Start polling Telegram for bot updates."""
        for command_trigger, command in self.commands_with_aliases(command_functions).items():
            handler = CommandHandler(command_trigger, command)
            self.dispatcher.add_handler(handler)

            logging.debug(f'Successfully loaded command trigger \'{command_trigger}\' to \'{command.__name__}\'')

        talk_handler = MessageHandler(Filters.text & (~Filters.command), talk_handler_command)
        self.dispatcher.add_handler(talk_handler)
        logging.debug('Successfully loaded the talk handler.')

        logging.info('Starting bot.')
        self.updater.start_polling()
