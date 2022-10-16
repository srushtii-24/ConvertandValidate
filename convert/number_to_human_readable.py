import math

millnames = ['', 'k', ' Million', ' Billion', ' Trillion']


def NTHR(input):
    n = float(input)
    millidx = max(0, min(len(millnames) - 1,int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))
    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])
