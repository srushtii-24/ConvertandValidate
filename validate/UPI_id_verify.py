import re
def UPIV(input):
    regex = r'[a-zA-Z0-9_]{3,}@[a-zA-Z]{3,}'
    if re.fullmatch(regex, input):
        return True

    return False