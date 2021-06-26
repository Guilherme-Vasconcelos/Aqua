# Installation
Whether you'd like to modify Aqua's source code or just use the program, all the steps
below are required.

### Prerequisites
1. Install [Poetry](https://python-poetry.org/docs/#installation) for managing dependencies.

2. Create your own Telegram bot by [speaking to Botfather](https://t.me/botfather).

### Setting up Aqua
After the prerequisites:

1. Clone the repository and `cd` into it. From here all commands will assume you are at the
project's root directory.

2. Make a copy of `config/db.example.json` called `config/db.json`. This file is currently not
used for anything, though this may change in the future.

3. Make a copy of `config/bot.example.json` called `config/bot.json`, then replace the contents
of `config/bot.json` with your actual data:
    - token: This is the value provided to you by Botfather after you spoke to him and created your bot.
    - user_chat_id: This is the value which Aqua will use to check whether she must reply to a
    message or not. It is optional and you may delete it completely if you don't want Aqua to perform
    authorization checks (in which case she will answer to **anyone** who messages her). If you DO
    want Aqua to perform authorization checks but you don't know your user_chat_id, go to the next
    steps and you will be instructed on how to find it out.

4. Create a virtual environment and install dependencies by running `$ python3 -m venv .venv`
and then `$ poetry install`.

5. Ensure you are using the local Python (which was created after you ran `$ python3 -m venv .venv`
during step 4) with the command: `$ which python3`, which should output something like this:
`/home/your_user/path/to/aqua/.venv/bin/python3`. If your output does not contain `.venv`, then
it means the local Python is not sourced (you can activate it with `$ poetry shell`).

6. Run aqua with the `$ aqua` command. Alternatively, you may use `$ poetry run aqua` too, which
may be required if you have installed aqua globally in your system.

7. Coming back to step 3, if you don't yet know your user_chat_id, run Aqua as described in step 6
and send her a `/start` message, then check your terminal. You should see a message that begins
like this: `WARNING - Received a message from 'XYZ', but user_chat_id is None`. XYZ is your user_chat_id.

As far as using Aqua, that's all there is to installation. If you are interested in modifying
the source code, check extra development instructions in [CONTRIBUTING.md](CONTRIBUTING.md) file.
