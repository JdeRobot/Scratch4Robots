#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import config
import sys
import comm
import os
import yaml
import math

from drone import Drone
from robot import Robot

def execute(robot):
    try:
        mylist2 = []
        mylist = []
        mylist2.append('0')
        mylist2.append('0')
        mylist2.append('-2')
        mylist.append('0')
        mylist.append('0')
        mylist.append('2')
        robot.take_off()
        time.sleep(1)
        robot.move_vector(mylist)
        time.sleep(3)
        robot.stop()
        time.sleep(1)
        robot.move_vector(mylist2)
        time.sleep(3)
        robot.stop()
        time.sleep(1)
        robot.land()
        time.sleep(1)
    except KeyboardInterrupt:
        raise

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = os.getcwd()
        open_path = path+'/'
        filename = sys.argv[1]

    else:
        sys.exit("ERROR: Example:python my_generated_script.py cfgfile.yml")

    # loading parameters
    if os.path.isabs(filename):
        stream = open(filename, "r")
        cfg = config.load(filename)
    else:
        stream = open(open_path + filename, "r")
        cfg = config.load(open_path + filename)
    yml_file = yaml.load(stream)

    for section in yml_file:
        if section == 'drone':
            # creating the object
            robot = Drone(cfg)

            break
        elif section == 'robot':
            # creating the object

            robot = Robot(cfg)

            break
    # executing the scratch program
    execute(robot)

