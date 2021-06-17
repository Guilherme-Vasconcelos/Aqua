# Aqua
Aqua is a Telegram bot for personal utilities.

### Installation
1. Prerequisites: Install Poetry for managing dependencies and fork/clone the repository.
All commands and files below will assume you are at the project's root directory.
2. Create your Telegram bot by [speaking to Botfather](https://t.me/botfather).
3. Rename `config/db.example.json` and `config/bot.example.json` respectively to
`config/db.json` and `config/bot.json`. Also, replace the data in those files with
your actual data:
    - `config/db.json` is not currently used for anything, though that may change
    in the future.
    - In `config/bot.json`: The token is provided to you by the Botfather.
    - In `config/bot.json`: The user_chat_id is optional and you may delete it completely
    if you don't want Aqua to perform authorization checks, in which case she will answer
    to anyone who messages her. If you do want Aqua to only answer to you but you don't know
    your user_chat_id, perform the next steps and you will be instructed on how to find it out.
4. Create a virtual environment and install dependencies by running `$ python3 -m venv .venv`
and `$ poetry install`.
5. Ensure you are using the local Python with `$ poetry shell` and then run `$ aqua` to start
the bot.
6. Coming back to step 3, if you don't yet know your user_chat_id, run Aqua as described in
step 5 and send her a `/start` message, then check your terminal. You should see a message
that begins like this: `WARNING - Received a message from 'XYZ', but user_chat_id is None`.
XYZ is your user_chat_id.

As far as using Aqua, that's all there is to installation. If you are interested in modifying
the source code, check extra development instructions in [CONTRIBUTING.md](CONTRIBUTING.md) file.

### Available commands
- `/start`: sends a "welcome" message. This can be useful to check if you have set up everything
correctly.
- `/remindme <time> <time_unit> <message>`: reminds you about \<message> after the given amount of
time. For example: `/remindme 10 minute Get pizza in the oven` will remind you about the pizza in
about 10 minutes.

More commands will be added soon!

### License
Copyright 2021 Guilherme-Vasconcelos

Aqua is licensed under the GNU Affero General Public License, either version 3
or any later versions. Please refer to LICENSE for more details.
