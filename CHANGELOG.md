# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Commands can now be abbreviate if the abbreviation is unambiguous (e.g. `/l` or `/lo` instead of `/lorem`).
- New command: `whatis`.
- Moved most of docs to `docs` directory.
- For development: removed the old pre-commit hook and replaced it with tests (which were also added to Actions
workflow).
- For development: added the `ensure_context_number_args` to easily specify the number of arguments a command
should have.

## [0.1.0] - 2021-06-20
### Added
- First release.
- 3 main commands: `lorem`, `remindme` and `sort`.
- Support to easily add new commands and handle user texts.
- Authentication to ensure Aqua will only answer to bot's owner.
- For development: Git pre-commit script hook and nodemon.
- READMEs with basic installation instructions.
- GitHub workflows for linting, pre-commit and security checks.
- GitHub issue templates.
