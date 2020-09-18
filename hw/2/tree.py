def get_input(label):
    try:
        int_value = input(label)
        if not int_value:
            raise ValueError('You mast enter value.')
        else:
            int_value = int(int_value)

    except ValueError:
        print('Wrong input type, must be int.')
    return int_value


if __name__ == '__main__':
    rows = get_input('Rows qty: ')
    for i in range(1, rows+1):
        print('{:{align}{width}}'.format('^'*(i*2-1), align='^', width=str(rows*2-1)))
