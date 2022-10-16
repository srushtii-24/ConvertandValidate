def VP(input):
    SpecialSym = ['$', '@', '#', '%']

    if len(input) <= 8:
        return 'length should be at least 6'

    if len(input) > 20:
        return 'length should be not be greater than 8'

    if not any(char.isdigit() for char in input):
        return 'Password should have at least one numeral'

    if not any(char.isupper() for char in input):
        return 'Password should have at least one uppercase letter'

    if not any(char.islower() for char in input):
        return 'Password should have at least one lowercase letter'

    if not any(char in SpecialSym for char in input):
        return 'Password should have at least one of the symbols $@#'

    return True