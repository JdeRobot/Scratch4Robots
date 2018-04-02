# Getting started

Source your catkin workspace

    cd catkin_workspace
    source devel/setup.bash

You can two between two examples file, robot_example_1.sb2 or robot_example_2.sb2


## Make the translation from Scratch to python

	roslaunch scratch4robots scratch2python_example_robot.launch file:=robot_example_2.sb2

## Launch the simulated world

In other terminal run:

    roslaunch kobuki_gazebo kobuki_empty_world.launch --screen

## Execute the generated code

	roscd scratch4robots
	cd examples/robot_example/src
	./robot_example_2.py robot_ros.yml
