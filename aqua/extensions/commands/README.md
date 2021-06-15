For new commands added, it is important that they follow the conventions:
- Each file will export a single command to be used by the bot.
- The function which will be executed by the bot (and therefore must be inside
your file) must have the same name as your file (without extension).

For instance, if your file is called `start.py`, then the bot will look for
a function called `start`.
