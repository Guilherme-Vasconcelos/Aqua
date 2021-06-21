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
