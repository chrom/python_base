from lib import get_input


class Rectangle:
    @staticmethod
    def calc() -> int:
        width, length = get_input('width: '), get_input('length: ')
        return width * length

    def hi(self):
        print('Calc rectangle: {}'.format(self.get_id()))

    def get_id(self) -> int:
        return 3