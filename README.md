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
All commands below can be abbreviated (e.g. you can use `/lo` instead of `/lorem`) as long as your
abbreviation is not ambiguous.

- `/lorem`: generates one paragraph of Lorem Ipsum text. 
- `/remindme <time> <time_unit> <message>`: reminds you about \<message> after the given amount of
time. Example: `/remindme 10 minute Get pizza in the oven` will remind you about the pizza in
about 10 minutes.
- `/sort <list of elements>`: sorts your list. If all the elements are numbers, they will be sorted
numerically, else alphabetically. Example: `/sort 5 2 1` or `/sort myword1 second_word`.
- `/start`: sends a "welcome" message. This can be useful to check if you have set up everything
correctly.
- `/whatis <search query>`: Gives you a brief summary about your search. Example: `/whatis linux kernel`.

More commands will be added soon!

### License
Copyright 2021 Guilherme-Vasconcelos

Aqua is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Aqua is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Aqua.  If not, see <https://www.gnu.org/licenses/>.
