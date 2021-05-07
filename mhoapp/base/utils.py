import math
import os


def remove_extension(value):
    return os.path.splitext(value)[0]    


def truncate_float(value):
    if value.is_integer():
        return math.trunc(value)
    return value


def currency(value):
    return "${:,}".format(value)