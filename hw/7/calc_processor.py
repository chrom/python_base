import figure
from lib import get_input


class Processor:
    def __init__(self, pull):
        self.pull = pull

    def execute(self):
        for id in self.pull:
            self.get_from_pull(id).hi()

        figure = self.get_from_pull(get_input('Select:'))
        print(figure.calc())

    def get_from_pull(self, id: int):
        return self.pull.get(id)

