import os


def remove_extension(value):
    return os.path.splitext(value)[0]    