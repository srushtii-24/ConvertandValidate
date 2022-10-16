import re
def PNV(input):
    regex = r'(\+91)?(-)?\s*?(91)?\s*?(\d{3})-?\s*?(\d{3})-?\s*?(\d{4})'
    if re.fullmatch(regex, input):
        return True

    return False
