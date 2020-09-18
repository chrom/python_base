import dictionary


def print_price(uah, uah_kopiyky):
    try:
        result = 'Цена: '
        if uah > 0:
            result += '{0:d} {1:s} '.format(uah, dictionary.dictionary_uah(uah))
        if uah_kopiyky > 0:
            result += '{0:d} {1:s}'.format(uah_kopiyky, dictionary.dictionary_uah_kopiyky(uah_kopiyky))
        if uah == 0 and uah_kopiyky == 0:
            result = 'Данные о цене не доступны.'

        print(result)

    except Exception:
        print('execute print_price.')


def get_input(label):
    try:
        int_value = input(label);
        if not int_value:
            int_value = 0
        else:
            int_value = int(int_value)

    except ValueError:
        print('Wrong input type, must be int.')
    return int_value


if __name__ == '__main__':
    try:
        print_price(
            get_input('Input UAH [₴ number]: '),
            get_input('Input UAH kopiyky [number]: ')
        )
    except Exception:
        print('Something was wrong.')
