from unittest import TestCase, main
from unittest.mock import patch

from io import StringIO
from toyrobot import ToyRobot


def coord(toy_robot):
    return (toy_robot.curr_x, toy_robot.curr_y, toy_robot.curr_facing)


class Test(TestCase):


    @patch('sys.stdout', new_callable=StringIO)
    def testName01(self, mock_stdout):
        """ Testing report formatting """
        toy_robot = ToyRobot()
        toy_robot.place(1, 2, 'NORTH')
        toy_robot.report()
        self.assertEqual(mock_stdout.getvalue().rstrip('\r\n'), '1, 2, NORTH')

    def testName02(self):
        """ Testing place between bounds """
        toy_robot = ToyRobot()
        toy_robot.place(1, 2, 'NORTH')
        self.assertEqual(coord(toy_robot), (1, 2, 'NORTH'))

        toy_robot.place(6, 7, 'NORTH')
        self.assertEqual(coord(toy_robot), (5, 5, 'NORTH'))

        toy_robot.place(-6, -7, 'NORTH')
        self.assertEqual(coord(toy_robot), (0, 0, 'NORTH'))

    def testName03(self):
        """ Testing rotate """
        toy_robot = ToyRobot()
        toy_robot.place(1, 1, 'NORTH')
        self.assertEqual(toy_robot.curr_facing, 'NORTH')
    
        for f in ('WEST', 'SOUTH', 'EAST', 'NORTH'):
            toy_robot.rotate_left()
            self.assertEqual(toy_robot.curr_facing, f)
    
        for f in ('EAST', 'SOUTH', 'WEST', 'NORTH'):
            toy_robot.rotate_right()
            self.assertEqual(toy_robot.curr_facing, f)

    def testName04(self):
        """ Testing move around upper right border """
        toy_robot = ToyRobot()
        toy_robot.place(4, 4, 'NORTH')
        self.assertEqual(coord(toy_robot), (4, 4, 'NORTH'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (4, 5, 'NORTH'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (4, 5, 'NORTH'))
        toy_robot.rotate_right()
        self.assertEqual(coord(toy_robot), (4, 5, 'EAST'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (5, 5, 'EAST'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (5, 5, 'EAST'))

    def testName05(self):
        """ Testing move around lower left border"""
        toy_robot = ToyRobot()
        toy_robot.place(1, 1, 'SOUTH')
        self.assertEqual(coord(toy_robot), (1, 1, 'SOUTH'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (1, 0, 'SOUTH'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (1, 0, 'SOUTH'))
        toy_robot.rotate_right()
        self.assertEqual(coord(toy_robot), (1, 0, 'WEST'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (0, 0, 'WEST'))
        toy_robot.move()
        self.assertEqual(coord(toy_robot), (0, 0, 'WEST'))

if __name__ == "__main__":
    main()
