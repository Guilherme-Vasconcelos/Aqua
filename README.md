# Aqua
Aqua is a Telegram bot for personal utilities.

### Installation
1. Prerequisites: Install Poetry for managing dependencies and fork/clone the repository.
All commands and files below will assume you are at the project's root directory.
2. Create your Telegram bot by [speaking to Botfather](https://t.me/botfather).
3. Rename `config/db.example.json` and `config/bot.example.json` respectively to
`config/db.json` and `config/bot.json`. Also, replace the data in those files with
your actual data. The user_chat_id is optional, but since this is a bot meant for personal
usage, if you do not supply a user_chat_id Aqua will answer to anyone who messages her.
4. Create a virtual environment and install dependencies by running `python3 -m venv .venv`
and `poetry install`.
5. Ensure you are using the local Python with `poetry shell` and then run `aqua` to start
the bot. Optionally, you may use the `--debug` flag.
6. (OPTIONAL) After everything is set up, you can execute the `prepare_git_hooks.sh` script
to create the Git hooks. This is only useful for development, so you should probably not need
to do that if you only want to run Aqua.
7. (OPTIONAL) For development, instead of executing `aqua` directly, run `yarn install`
(requires [yarn](https://yarnpkg.com/)) and then `yarn aqua`. This way nodemon will automatically
restart the server when changes are detected.

### Adding new commands
Check out the README located at `aqua/extensions/commands`.

### License
Aqua is licensed under the GNU Affero General Public License, either version 3
or any later versions. Please refer to LICENSE for more details.
