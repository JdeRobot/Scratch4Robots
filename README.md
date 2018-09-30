# Scratch4Robots

## Full installation video

[![Scratch4Robots](http://img.youtube.com/vi/5JYuD8N0RBs/1.jpg)](https://www.youtube.com/watch?v=5JYuD8N0RBs "Scratch4Robots")

## Prerequisites

### Scratch 2.0

    wget -O adobe-air.sh http://drive.noobslab.com/data/apps/AdobeAir/adobe-air.sh
    chmod +x adobe-air.sh; sudo ./adobe-air.sh

Download the scratch file from here: https://scratch.mit.edu/scratchr2/static/sa/Scratch-456.0.2.air and then double click to install it.

### ROS

Follow the ROS tutorial installation: http://wiki.ros.org/kinetic/Installation/Ubuntu

### Python requirements

    pip install -r requirements.txt

### Gazebo and worlds

Follow the Gazebo tutorial installation: http://gazebosim.org/tutorials?tut=install_ubuntu

With this line we get some prepared worlds based on ROS ready to use:

    sudo apt-get install ros-${ROS_DISTRO}-kobuki-gazebo


## Installing

### Install our ROS package

    sudo apt-get install ros-kinetic-scratch4robots

### Install Scartch4Robots extension to use in Scratch

In scratch keep pressing shift key while you click on "File" > "Import experimental HTTP extension" and add our extension.
The extension will be stored in the "extension" directory of your package.

    Note: This step is necessary each time you initialize Scratch

### Download the tool from git

Here you will find some usefull examples.

    git clone https://github.com/JdeRobot/Scratch4Robots.git

## How to Use

### Make a scratch project

Make a scratch project and save it.

### Make the translation from Scratch to python

Generate the code:

    rosrun scratch4robots scratch2python /path/to/your/scratchproject.sb2

This command will generate the python script on your current work directory


### Launch the simulated world

For example:

    roslaunch kobuki_gazebo kobuki_empty_world.launch --screen


### Execute the generated code

The generated code need a configuration file .yml as parameter, you will find some usefull configuration files in this git repository.

	./myscratchfile.py /path/to/robot_ros.yml

## Running an example

You have all you need for running the examples in the examples folder


# More information about the tool

http://jderobot.org/Scratch4Robots
