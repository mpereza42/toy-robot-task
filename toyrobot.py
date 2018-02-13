
from collections import namedtuple

Transition = namedtuple('Transition', ['left', 'right', 'x', 'y'])

MAX_X = 5
MAX_Y = 5


class ToyRobot(object):
    TRANSITIONS = {
        'WEST': Transition('SOUTH', 'NORTH', -1, 0),
        'NORTH': Transition('WEST', 'EAST', 0, 1),
        'EAST': Transition('NORTH', 'SOUTH', 1, 0),
        'SOUTH': Transition('EAST', 'WEST', 0, -1)
        }
    FACINGS = TRANSITIONS.keys()

    def __init__(self):
        self.curr_facing = None
        self.curr_x = 0
        self.curr_y = 0

    def place(self, x, y, facing):
        if facing not in self.FACINGS:
            raise ValueError('Invalid facing: '+facing)

        self._set_position(x, y)
        self.curr_facing = facing


    def move(self):
        if self.curr_facing is None:
            return

        self._set_position(self.curr_x + self._transition.x, self.curr_y + self._transition.y)


    def rotate_left(self):
        if self.curr_facing is None:
            return

        self.curr_facing = self._transition.left


    def rotate_right(self):
        if self.curr_facing is None:
            return

        self.curr_facing = self._transition.right


    def report(self):
        print( '{}, {}, {}'.format(self.curr_x, self.curr_y, self.curr_facing) )

    @property
    def _transition(self):
        return self.TRANSITIONS[self.curr_facing]

    def _set_position(self, x, y):
        x = MAX_X if x > MAX_X else x
        x = 0 if x < 0 else x

        y = MAX_Y if y > MAX_Y else y
        y = 0 if y < 0 else y

        self.curr_x = x
        self.curr_y = y


if __name__ == '__main__':
    tr = ToyRobot()
    tr.report()
