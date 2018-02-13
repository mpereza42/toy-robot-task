import unittest
from unittest.mock import Mock, call
from inputparser import InputParser
from toyrobotinterpreter import ToyRobotInterpreter
from toyrobot import ToyRobot


class Test(unittest.TestCase):

    def testName01(self):
        """ Testing ToyRobotInterpreter place() handler """
        toy = ToyRobot()
        toy.place = Mock()
        tri = ToyRobotInterpreter(toy)

        tri.cmd_PLACE_handler('1,2,NORTH')
        toy.place.assert_called_once_with(1, 2, 'NORTH')
        

    def testName02(self):
        """ Testing multiple ToyRobotInterpreter place() calls """
        toy = ToyRobot()
        toy.place = Mock()
        tri = ToyRobotInterpreter(toy)
        tri.cmd_PLACE_handler('1,2,NORTH')
        tri.cmd_PLACE_handler('3,4,EAST')

        expected = [call(1,2,'NORTH'), call(3,4,'EAST')]
        self.assertEqual(toy.place.call_args_list, expected,"method_calls not initialised correctly")


    def testName03(self):
        """ Testing correct ToyRobot calls """
        robot_attrs = {'TRANSITIONS': ToyRobot.TRANSITIONS, 'FACINGS': ToyRobot.FACINGS}
        toy = Mock(**robot_attrs)
        ip = InputParser(ToyRobotInterpreter(toy))
        ip.process_line('PLACE 1,2,NORTH MOVE LEFT PLACE 3,4,EAST RIGHT REPORT')

        expected = [call.place(1, 2, 'NORTH'),
                    call.move(),
                    call.rotate_left(),
                    call.place(3, 4, 'EAST'),
                    call.rotate_right(),
                    call.report()]

        self.assertEqual(toy.method_calls, expected, "methods not invoked correctly")


if __name__ == "__main__":
    unittest.main()
