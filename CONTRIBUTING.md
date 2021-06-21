# Contributing
Hello! Here you will find extra installation instructions for development.

### Development installation
1. First you should install Aqua as described in [README.md](README.md).
2. In order to set up the git hooks, execute `$ sh prepare_git_hooks.sh` in your
terminal, which will copy the hooks (such as pre-commit) to the correct git directory.
3. When executing aqua, it is recommended that you:
    1. Install [yarn](https://yarnpkg.com/), a node.js package manager, and
    then run `$ yarn install` in Aqua's root directory.
    2. Execute `$ yarn aqua` instead of `$ aqua`. The only difference is that
    with the first command [nodemon](https://github.com/remy/nodemon) will be
    used to automatically restart Aqua whenever there are source code changes.
    3. Optionally, you may use the `--debug` (`-d` for short) flag, which will
    display extra information.
4. When you are done with your feature, please remember to add it to
[CHANGELOG.md](CHANGELOG.md).

### What kind of ideas am I allowed to suggest or add?
Any ideas that would be good for a personal utility. If you have some problem that
you think could be solved with a Telegram bot, feel free to suggest or implement it!

### Adding new commands
Check out the README located at `aqua/extensions/commands`.

### Adding new talk options
Check out `aqua/talk/talk.py`.

### See also
1. Docstring conventions: https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard

### License
By contributing, you agree that all your modifications and additions will be
licensed under the GNU Affero General Public License, either version 3 or
ANY later versions.
