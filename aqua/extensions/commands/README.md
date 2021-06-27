All commands in this directory are automatically loaded by Aqua provided
that they follow the conventions:
- Each file will export a single command to be used by Aqua.
- The function which will be executed by Aqua (and therefore must be inside
your file) must have the same name as your file (without extension).

For example, if your file is called `start.py`, then Aqua will look for
a function called `start`.

Remember to place an `@authorize` decorator before the function that will
be automatically loaded:
```python
@authorize
def start(...):
    ...
```

Optionally, you may also use the decorator `@ensure_context_number_args`
to easily specify how many arguments your command must have, though this
one is not mandatory and will not be checked by CI:
```python
@authorize
@ensure_context_number_args(5, 'max')
def my_command_that_takes_up_to_five_arguments(...):
    ...
```
