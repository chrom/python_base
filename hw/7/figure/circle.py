from math import pi
from lib import get_input


class Circle:
    def calc(self) -> float:
        radius = get_input('Set radius: ')
        return radius ** 2 * pi

    def hi(self):
        print('Calc circle:  {}'.format(self.get_id()))

    def get_id(self) -> int:
        return 1
