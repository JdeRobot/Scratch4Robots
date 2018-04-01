# Installation requirements

    pip install -r requirements.txt


# How to use

## Prepare your workspace

You have a guide for make your own catkin workspace here:
http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Once you have your catkin workspace:

	cd catkin_workspace/src
	git clone https://github.com/JdeRobot/Scratch4Robots.git
	catkin_make

Now your package is ready to use.


## Install Scartch4Robots extension to use in Scratch2.0

In scratch keep pressing shift key while you click on "File" > "Import experimental HTTP extension" and add our extension.
The extension will be stored in the "extension" directory of your package.


## Make a project

Make a scratch project and save it in the data directory of the package


## Make the translation from Scratch to python

	roslaunch scratch4robots scratch2python.launch file:=myscratchfile.sb2


## Launch the simulated world

for example:

    roslaunch kobuki_gazebo kobuki_empty_world.launch --screen


## Execute the generated code

	roscd scratch4robots
	cd src
	./myscratchfile.py robot_ros.yml


# More information about the tool

http://jderobot.org/Scratch4Robots
