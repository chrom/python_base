p = [
    {'id': 1, 'name': 'Ноутбук Acer Aspire 5 A515-54G-502N (NX.HVGEU.006) Pure Silver', 'price': 10, 'qty': 10},
    {'id': 2, 'name': 'Ноутбук Asus ROG Strix G15 G512LI-HN057 (90NR0381-M01640) Black', 'price': 20, 'qty': 20},
    {'id': 3, 'name': 'Ноутбук HP Pavilion Notebook 15-cw1011ua (8RW14EA) Mineral Silver', 'price': 30, 'qty': 30},
    {'id': 4, 'name': 'Ноутбук HP Pavilion Notebook 16', 'price': 40, 'qty': 40},
    {'id': 5, 'name': 'Ноутбук Lenovo Yoga S730-13IWL (81J000AHRA) Iron Grey', 'price': 50, 'qty': 50},
]


def show_product_list():
    print('Products list:')
    for item in p:
        print('* ID: {:d} {} \t\nprice:{:03.2f} qty:{:2d}'.format(item.get('id'),
                                                                  item.get('name'),
                                                                  item.get('price'),
                                                                  item.get('qty')))


if __name__ == '__main__':
    while True:
        show_product_list()
        print('*' * 40)
        print('FOR EXIT ENTER NOT EXIST ID!')
        item = int(input('\tFor change QTY enter product ID: '))
        print('*' * 40)

        for i in p:
            if i.get('id') == item:
                qty = int(input('\tEnter QTY for product with ID: {} current QTY:{}: '.format(item, i.get('qty'))))
                p[item-1]['qty'] = qty
                break
        else:
            print("Item {} not exist in List.".format(item))
            break


