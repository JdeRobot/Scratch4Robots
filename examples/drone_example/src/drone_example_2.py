#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import config
import sys
import os
import yaml
import math

from drone import Drone
from robot import Robot

def execute(robot):
    try:
        mylist = []
        myvelocity = []
        robot.take_off()
        while True:
            mylist.insert(0, robot.detect_object("red"))
            size = mylist[0][0]
            x = mylist[0][1]
            y = mylist[0][2]
            if size > 0:
                if size > 700:
                    velx = '-2'
                else:
                    velx = '2'
                
                if x > 165:
                    velyaw = '-2'
                else:
                    velyaw = '2'
                
                if y > 110:
                    velz = '-1'
                else:
                    velz = '1'
                
            else:
                robot.stop()
                velx = '0'
                velz = '0'
                velyaw = '2'
            
            myvelocity.insert(0, velx)
            myvelocity.insert(1, velz)
            myvelocity.insert(2, velyaw)
            robot.move_vector(myvelocity)
        
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
            #TODO
            robot = Drone(cfg)

            break
        elif section == 'robot':
            robot = Robot(cfg)

            break
    # executing the scratch program
    execute(robot)

