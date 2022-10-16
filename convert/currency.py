from currency_converter import CurrencyConverter

def currency(value, fromcurr, tocurr):
    c = CurrencyConverter()
    value = int(value)
    convert_value = c.convert(value, fromcurr, tocurr)
    return round(convert_value,3)

