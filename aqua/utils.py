from sys import argv


def has_flag(full_flag: str) -> bool:
    if '--' + full_flag in argv:
        return True

    return '-' + full_flag[0] in argv
