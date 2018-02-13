import unittest
from unittest.mock import Mock, call
from inputparser import InputParser
from toyrobotinterpreter import ToyRobotInterpreter


toy_robot_interpreter_attrs = {'RE_INPUT_LINE' : ToyRobotInterpreter.RE_INPUT_LINE}

class Test(unittest.TestCase):


    def testName01(self):
        """ Testing all commands """
        mock = Mock(spec=ToyRobotInterpreter, **toy_robot_interpreter_attrs)
        ip = InputParser(mock)
        ip.process_line('PLACE 1,2,NORTH MOVE LEFT RIGHT REPORT')
        expected = [call.cmd_PLACE_handler('1,2,NORTH'),
                    call.cmd_MOVE_handler(None),
                    call.cmd_LEFT_handler(None),
                    call.cmd_RIGHT_handler(None),
                    call.cmd_REPORT_handler(None)]
        self.assertEqual(mock.method_calls, expected,"method_calls not initialised correctly")

    def testName02(self):
        """ Testing PLACE called multiple times """
        mock = Mock(spec=ToyRobotInterpreter, **toy_robot_interpreter_attrs)
        ip = InputParser(mock)
        ip.process_line('PLACE 1,2,EAST MOVE PLACE 11,12,WEST REPORT')
        expected = [call.cmd_PLACE_handler('1,2,EAST'),
                    call.cmd_MOVE_handler(None),
                    call.cmd_PLACE_handler('11,12,WEST'),
                    call.cmd_REPORT_handler(None)]
        self.assertEqual(mock.method_calls, expected,"method_calls not initialised correctly")

    def testName03(self):
        """ Testing invalid commands """
        mock = Mock(spec=ToyRobotInterpreter, **toy_robot_interpreter_attrs)
        ip = InputParser(mock)
        ip.process_line('PLACE 5,6,NORTH SPAM REPORT EGG')
        expected = [call.cmd_PLACE_handler('5,6,NORTH'),
                    call.unhandled_keyword('SPAM'),
                    call.cmd_REPORT_handler(None),
                    call.unhandled_keyword('EGG')]
        self.assertEqual(mock.method_calls, expected,"method_calls not initialised correctly")

    def testName04(self):
        """ Testing invalid arguments in PLACE command """
        mock = Mock(spec=ToyRobotInterpreter, **toy_robot_interpreter_attrs)
        ip = InputParser(mock)
        ip.process_line('PLACE x,y,NORTH REPORT')
        mock.cmd_PLACE_handler.assert_called_once_with(None)

if __name__ == "__main__":
    unittest.main()
