# Toy robot

## Description
The application is a simulation of a toy robot moving on a square tabletop, of dimensions 5 units x 5 units. There are no other obstructions on the table surface.

The robot is free to roam around the surface of the table, but must be prevented from falling to destruction. Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.


Create an application that can read in commands of the following form:
* PLACE X,Y,F
* MOVE
* LEFT
* RIGHT
* REPORT


PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner. The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed. 


MOVE will move the toy robot one unit forward in the direction it is currently facing. 


LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without changing the position of the robot. 

REPORT will announce the X,Y and orientation of the robot. 

A robot that is not on the table can choose to ignore the MOVE, LEFT, RIGHT and REPORT commands. 

Provide test data to exercise the application.

## Constraints:
The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any move that would cause the robot to fall must be ignored.


Example Input and Output:
a) PLACE 0,0,NORTH MOVE REPORT Output: 0,1,NORTH

b) PLACE 0,0,NORTH LEFT REPORT Output: 0,0,WEST

c) PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT Output: 3,3,NORTH


## Implementation
Input language handling is implemented in two classes: InputParser and ToyRobotInterpreter.
InputParser iterate over input line using regex provided from ToyRobotInterpreter and, for every matched command, calls its implementation in ToyRobotInterpreter.

Rationale for this design is to easily support different versions of robot with slightly different command set or syntax dialect.
If new robot version is introduced, the only necessary change to input parsing is to provide new ToyRobotInterpreter class.
Also, this simplify unit testing.

ToyRobotInterpreter must comply with these contracts:

 * must define regex provided in member variable `RE_INPUT_LINE`
 * regex match must return two groups: keyword and arguments
 * regex must be iterable (matching can start at every input offset and must consume least amount of input)
 * for every keyword, interpreter class must contain method named `cmd_XX_handler`, where XX is the keyword name
 * optionally, class can contain method `unhandled_keyword` which will be called when appropriate handler is not found, so it is possible to gracefully ignore some commands


## Usage

The best way to invoke application is to make start.py script executable. Alternativelly use python 3.x interpreter.

    python3 start.py

start.py supports input from stdin. For example:

    ./start.py < test_cmd.txt

if start.py is invoked without additional arguments it is assumed to type commands in console.

To exit application in this mode, type :q in empty line.





