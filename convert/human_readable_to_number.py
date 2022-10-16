import math


def HRTN(number):
    x = number[-1]
    number = number.replace(x, '')
    x = x.upper()
    final = float(number)
    units = {
        'K': 1000,
        'M': 1000000,
        'B': 1000000000,
        'T': 1000000000000,
        'Q': 1000000000000000
    }
    y = units[x]
    return int(final * y)
