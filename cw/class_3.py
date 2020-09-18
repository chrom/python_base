import math


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


def area_of_circle(r) -> float:
    a = r ** 2 * math.pi
    return a


def area_of_triangle(a: int, b: int, c: int) -> int:
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def area_of_rectangle(width: int, length: int) -> int:
    area = width * length
    return area


def choice():
    print('Calc circle: 1')
    print('Calc triangle: 2')
    print('Calc rectangle: 3')
    inp = get_input('Select:')
    if (3 == inp):
        print(area_of_rectangle(get_input('width: '), get_input('length: ')))
    elif (2 == inp):
        print(area_of_triangle(get_input('a: '), get_input('b: '), get_input('c: ')))
    elif (1 == inp):
        print(area_of_circle(get_input('Set radius: ')))


if __name__ == '__main__':
    # choice()
    print("Name: % s\nNumber: % s\nString: % s" % ('myclass.name', 3, 3 * "-"))

#
# import math
#
#
def get_input(label):
    try:
        int_value = input(label)
        if not int_value:
            raise ValueError('You mast enter value.')

        else:
            int_value = float(int(int_value))

    except ValueError:
        print('Wrong input type, must be int.')
    return int_value
#
#
# if __name__ == '__main__':
#     try:
#         print("ax^2 + bx + c = 0:")
#         a = get_input("a = ")
#         b = get_input("b = ")
#         c = get_input("c = ")
#
#         discr = b ** 2 - 4 * a * c
#         print("Дискриминант D = {0:f}".format(discr))
#
#         if discr > 0:
#             x1 = (-b + math.sqrt(discr)) / (2 * a)
#             x2 = (-b - math.sqrt(discr)) / (2 * a)
#             print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
#         elif discr == 0:
#             x = -b / (2 * a)
#             print("x = %.2f" % x)
#         else:
#             print("Корней нет")
#     except Exception:
#         print('Something was wrong.')
