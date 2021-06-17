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

### Adding new commands
Check out the README located at `aqua/extensions/commands`.

### License
By contributing, you agree that all your modifications and additions will be
licensed under the GNU Affero General Public License, either version 3 or
ANY later versions.
