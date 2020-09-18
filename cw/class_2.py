def calc(first: int, second: int) -> int:
    print('First number: {0:d}  \nSecond number {1:d} '.format(first, second))
    return first * second


def get_input(label):
    try:
        int_value = input(label);
        if not int_value:
            raise ValueError('You mast enter value.')
        else:
            int_value = int(int_value)

    except ValueError:
        print('Wrong input type, must be int.')
    return int_value


if __name__ == '__main__':
    check = calc(
        get_input('Input First  [number]: '),
        get_input('Input Second [number]: ')
    )

    value = get_input('Enter answer [number]: ')
    if check == value:
        print('Right')
    else:
        print('Wrong')
