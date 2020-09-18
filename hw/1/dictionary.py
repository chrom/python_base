def dictionary_uah(value):
    if 4 < value < 21 or 5 <= value % 10 < 10 or value % 10 == 0:
        return 'гривен'
    elif value % 10 == 1 or value == 1:
        return 'гривна'
    elif 1 < value % 10 < 5:
        return 'гривны'


def dictionary_uah_kopiyky(value):
    if 4 < value < 21 or 5 <= value % 10 < 10 or value % 10 == 0:
        return 'копеек'
    elif value % 10 > 1:
        return 'копейки'
    elif 0 < value % 10 < 5:
        return 'копейка'
