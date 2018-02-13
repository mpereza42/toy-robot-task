
class ToyRobotInterpreter(object):
    RE_INPUT_LINE = r'(?:^| )([A-Za-z]+)(\s+\d+,\d+,[A-Za-z]+)*'
    
    def __init__(self, toy_robot):
        self._toy_robot = toy_robot

    def cmd_PLACE_handler(self, arguments):
        if arguments is None:
            raise ValueError('No arguments in PLACE command')
        
        tokens = arguments.split(',')
        if len(tokens) != 3:
            raise ValueError('Invalid arguments in PLACE command')
        
        # these are already validated by regex, but include for completeness
        try:
            x = int(tokens[0])
            y = int(tokens[1])
        except ValueError:
            raise ValueError('Invalid coordinate in PLACE command')
        
        facing = tokens[2]
        if facing not in self._toy_robot.FACINGS:
            raise ValueError('Invalid facing:'+facing)

        self._toy_robot.place(x, y, facing)

    def cmd_MOVE_handler(self, arguments):
        self._toy_robot.move()

    def cmd_LEFT_handler(self, arguments):
        self._toy_robot.rotate_left()

    def cmd_RIGHT_handler(self, arguments):
        self._toy_robot.rotate_right()

    def cmd_REPORT_handler(self, arguments):
        self._toy_robot.report()

    def unhandled_keyword(self, keyword):
        raise Exception('unhandled keyword: '+ keyword)

