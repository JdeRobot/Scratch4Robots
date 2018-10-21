from camera import *
from cmdvel import *
from extra import *
from pose3d import *
import imutils
import cv2
import numpy as np
import time
import math
import config


class Drone:
    def __init__(self,cfg):

        # variables
        topicArming = cfg.getProperty("drone.Extra.TopicArming")
        topicLand = cfg.getProperty("drone.Extra.TopicLand")
        topicSetMode = cfg.getProperty("drone.Extra.TopicSetMode")
        topicVel = cfg.getProperty("drone.Extra.TopicVel")
        topicPose = cfg.getProperty("drone.Pose3D.Topic")
        topicCameraFrontal = cfg.getProperty("drone.Camera.Topic")
        # self.__cameraVentral = ListenerCamera(topicCameraVentral)
        self.__cameraFrontal = ListenerCamera(topicCameraFrontal)
        self.__extra = PublisherExtra(topicArming, topicLand, topicSetMode)
        self.__cmdvel = PublisherCMDVel(topicVel)
        self.__pose3d = ListenerPose3d(topicPose)


    # def getImageVentral(self):
    #     return self.__cameraVentral.getImage()
    #
    def getImageFrontal(self):
        return self.__cameraFrontal.getImage()

    def take_off(self):
        self.__extra.arming()
        self.__cmdvel.sendCMDVel(0,0,2,0,0,0)
        time.sleep(1)
        self.__cmdvel.sendCMDVel(0,0,0,0,0,0)

    def land(self):
        self.__extra.land()

    def toggleCam(self):
        self.__extra.toggleCam()

    def reset(self):
        self.__extra.reset()

    def record(self, record):
        self.__extra.record(record)

    def move_vector(self, velocities):
        pose = self.__pose3d.getPose3d()
        yaw = pose.yaw
        vx = float(velocities[0])
        vz = float(velocities[1])
        az = float(velocities[2])
        print vx, vz, az
        vxt = vx*math.cos(yaw) #- vy*math.sin(yaw)
        vyt = vx*math.sin(yaw) #+ vy * math.cos(yaw)
        self.__cmdvel.sendCMDVel(vxt,vyt,vz,0,0,az)

    def get_pose3d(self):
        return self.__pose3d.getPose3d()

    def stop(self):
        self.__pose3d.stop()
        # self.__cameraVentral.stop()
        self.__cameraFrontal.stop()

    def pause (self):
        self.__cmdvel.pause()

    def resume (self):
        self.__cmdvel.resume()


    def detect_object(self, color):
        """
        Detect an object using the camera.

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
        image = self.__cameraFrontal.getImage()

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
        print "frame"
        key = cv2.waitKey(1) & 0xFF

        return size, x_position, y_position
