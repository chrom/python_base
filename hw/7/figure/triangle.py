from lib import get_input


class Triangle:
    def calc(self):
        a, b, c = get_input('a: '), get_input('b: '), get_input('c: ')
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def hi(self):
        print('Calc triangle: {}'.format(self.get_id()))

    def get_id(self) -> int:
        return 2
