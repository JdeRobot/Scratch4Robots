#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import config
import sys
import os
import yaml
import math

from drone import Drone

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


    topicArming = cfg.getProperty("drone.Extra.TopicArming")
    topicLand = cfg.getProperty("drone.Extra.TopicLand")
    topicSetMode = cfg.getProperty("drone.Extra.TopicSetMode")
    topicVel = cfg.getProperty("drone.Extra.TopicVel")
    topicPose = cfg.getProperty("drone.Pose3D.Topic")
    # topicCameraVentral = cfg.getProperty("drone.")
    topicCameraFrontal = cfg.getProperty("drone.Camera.Topic")


    robot = Drone(topicArming, topicLand, topicSetMode, topicVel, topicPose, "cv", topicCameraFrontal)
    # print "rotacion-"
    # robot.sendCMDVel(0,0,0,0,0,-2)
    # time.sleep(3)
    # print "rotacion-"
    # robot.sendCMDVel(0,0,0,0,0,1)
    # time.sleep(3)
    # print "rotacion-"
    # robot.sendCMDVel(0,0,0,0,0,-7)
    # time.sleep(3)
    # print "frente"
    # robot.sendCMDVel(-2,0,0,0,0,0)
    # time.sleep(3)
    # print "back"
    # robot.sendCMDVel(2,0,0,0,0,0)
    # time.sleep(3)
    # print "rotacion"
    # robot.sendCMDVel(0,0,0,0,0,2)
    # time.sleep(3)
    for _ in range(20):
        print "getting images"
        print robot.detect_object("red")
        time.sleep(0.2)
