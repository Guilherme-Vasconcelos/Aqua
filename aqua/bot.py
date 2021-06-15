import glob
import logging

from os.path import dirname, basename, isfile, join

from telegram.ext import CommandHandler, Updater

# Dynamically importing all command extensions
command_extensions_files = glob.glob(join(dirname(__file__) + '/extensions/commands', "*.py"))
command_extensions = [
    basename(f)[:-3] for f in command_extensions_files if isfile(f) and not f.endswith('__init__.py')
]

imports = ''
for command_extension in command_extensions:
    imports += f'from aqua.extensions.commands.{command_extension} import {command_extension}\n'

exec(imports)


class Bot:
    def __init__(self, token: str) -> None:
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

    def start_polling(self):
        for command in command_extensions:
            handler = CommandHandler(command, globals()[command])
            self.dispatcher.add_handler(handler)

            logging.info(f'Successfully loaded command \'{command}\'')
        self.updater.start_polling()
