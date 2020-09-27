def get_input(label) -> int:
    try:
        int_value = input(label)
        if not int_value:
            raise ValueError('You mast enter value.')

        else:
            int_value = int(int_value)

    except ValueError:
        print('Wrong input type, must be int.')
    return int_value
