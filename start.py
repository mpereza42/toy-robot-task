#!/usr/bin/env python3

from sys import stdin

from toyrobot import ToyRobot
from toyrobotinterpreter import ToyRobotInterpreter
from inputparser import InputParser


if __name__ == '__main__':
    toy_robot = ToyRobot()
    inputparser = InputParser(ToyRobotInterpreter( toy_robot ))
    
    for line in stdin:
        line = line.rstrip()
        if line == ':q':
            print('exiting..')
            break
        inputparser.process_line(line)
