#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import config
import rospy

from JDRros.listenerPose3d import ListenerPose3d
from JDRros.listenerLaser import ListenerLaser
from JDRros.publisherMotors import PublisherMotors

from jderobotTypes import CMDVel


class Robot():

    """
    Robot class.
    """

    def __init__(self, cfg):
        """
        Init method.

        @param cfg:
        """

        # ymlNode = cfg.getProperty("robot") # return dict with properties from yml
        # get node
        self.__node = rospy.init_node("robot", anonymous=True)

        # get clients
        prefix = "robot.Pose3D"
        print("Receiving " + prefix + " from ROS messages")
        topic = cfg.getProperty(prefix+".Topic")
        self.__pose3d_client = ListenerPose3d(topic)


        prefix = "robot.Motors"
        print("Publishing "+  prefix + " with ROS messages")
        topic = cfg.getProperty(prefix+".Topic")
        maxW = cfg.getPropertyWithDefault(prefix+".maxW", 0.5)
        if not maxW:
            maxW = 0.5
            print (prefix+".maxW not provided, the default value is used: "+ repr(maxW))

        maxV = cfg.getPropertyWithDefault(prefix+".maxV", 5)
        if not maxV:
            maxV = 5
            print (prefix+".maxV not provided, the default value is used: "+ repr(maxV))

        self.__motors_client =  PublisherMotors(topic, maxV, maxW)

        prefix = "robot.Laser"
        print("Receiving " + prefix + " from ROS messages")
        topic = cfg.getProperty(prefix+".Topic")
        self.__laser_client = ListenerLaser(topic)

        # variables

        self.__vel = CMDVel()

        # # get clients
        # self.__pose3d_client = jdrc.getPose3dClient("robot.Pose3D")
        # self.__motors_client = jdrc.getMotorsClient("robot.Motors")
        # self.__laser_client = ros.ListenerPose3d("robot.Laser")


    def __publish(self, vel):
        """
        .

        @param vel:
        """

        self.__motors_client.sendVelocities(vel)
        time.sleep(1)

    def __reset(self):
        """
        Reset the values to zero.
        """

        # reset velocities (m/s)
        self.__vel.vx = 0.0
        self.__vel.vy = 0.0
        self.__vel.vz = 0.0
        self.__vel.ax = 0.0
        self.__vel.ay = 0.0
        self.__vel.az = 0.0

    def get_pose3d(self):
        """
        Get the value of odometry sensor.

        @return: return the asked value.
        """

        return self.__pose3d_client.getPose3d()


    def detect_object(self, position, color):
        """
        Detect an object using the camera.

        @param position: data to return
        @param color: color to detect

        @return: size and center of the object detected in the frame
        """
        # define the lower and upper boundaries of the basic colors
        GREEN_RANGE = ((29, 86, 6), (64, 255, 255))
        RED_RANGE = ((139, 0, 0), (255, 160, 122))
        BLUE_RANGE = ((0, 128, 128), (65, 105, 225))

        # initialize the values in case there is no object
        x_position = 0
        y_position = 0
        size = 0

        # chose the color to find
        if color == "red":
            color_range = RED_RANGE
        if color == "green":
            color_range = GREEN_RANGE
        if color == "blue":
            color_range = BLUE_RANGE

        # get image type from camera
        image = self.__camera_client.getImage()

        # apply color filters to the image
        filtered_image = cv2.inRange(image.data, color_range[0], color_range[1])
        rgb = cv2.cvtColor(image.data, cv2.COLOR_BGR2RGB)


        # Apply threshold to the masked image
        ret,thresh = cv2.threshold(filtered_image,127,255,0)
        im,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        # Find the index of the largest contour
        for c in contours:
            if c.any != 0:
                areas = [cv2.contourArea(c) for c in contours]
                max_index = np.argmax(areas)
                cnt=contours[max_index]
                if max(areas) > 0.0:
                    x,y,w,h = cv2.boundingRect(cnt)
                    cv2.rectangle(rgb,(x,y),(x+w,y+h),(0,255,0),2)
                    x_position = (w/2)+x
                    y_position = (h/2)+y
                    size = w*h

        # show the frame to our screen
        cv2.imshow("Frame", rgb)
        key = cv2.waitKey(1) & 0xFF

        print x_position, y_position, size

        if position == "x position":
            return x_position
        if position == "y position":
            return y_position
        else:
            return size

    def get_laser_distance(self):
        """
        Get the average value for the values of the frontal laser.

        @return: the average measure of the frontal laser data.
        """

        # get laser values
        laser = self.__laser_client.getLaserData()

        # clean data (unranged values, e.g. nan)
        l = [x for x in laser.values if str(x) != 'nan' and x < 10]

        try:
            avg = sum(l) / len(l)
        except ZeroDivisionError:
            avg = 0

        return avg


    def move_vector(self, velocities):
        """
        Set the vector movement of the robot.

        @param velocities: a vector with velocities (vx,vz) in m/s.
        """

        vx = float(velocities[0])
        vz = float(velocities[1])
        print "velocities:",vx,vz
        # reset values
        self.__reset()

        self.__vel.vx = vx
        self.__vel.vz = vz
        if vz>0:
            self.turn("left",vz)
        if vz<0:
            self.turn("right",vz)

        self.__publish(self.__vel)



    def move(self, direction, vel=None):
        """
        Set the straight movement of the robot.

        @param direction: direction of the move. Options: forward (default), back.
        @param vel: a number with the velocity in m/s. Default: 0.2 m/s.
        """

        # reset values
        self.__reset()

        # set default velocity (m/s)
        self.__vel.vx = 0.2

        # set different velocity than default
        if vel != None:
            self.__vel.vx = vel

        # set different direction
        if direction == "back":
            self.__vel.vx = -self.__vel.vx

        # publish movement
        self.__publish(self.__vel)

    def turn(self, direction, vel=None):
        """
        Set the angular movement of the robot.

        @param direction: direction of the move. Options: left (default), right.
        @param vel: a number with the velocity in m/s. Default: 0.2 m/s.
        """

        # reset values
        # self.__reset()

        # set default velocity (m/s)
        self.__vel.az = 0.2

        # set different velocity
        if vel != None:
            self.__vel.az = vel

        # set different direction
        if direction == "right":
            self.__vel.az = -self.__vel.az

        # publish movement
        self.__publish(self.__vel)

    def stop(self):
        """
        Set all velocities to zero in order to stop any move.
        """

        # reset values
        self.__reset()

        # publish movement
        self.__publish(self.__vel)
