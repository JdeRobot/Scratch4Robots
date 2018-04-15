# Getting started

This example is ready for work directly with ROS

You have an example here:

https://www.youtube.com/watch?v=hv0OtbSlIYg

## Prepare your workspace

Source your catkin workspace

    cd catkin_workspace
    source devel/setup.bash

You can two between two examples file, robot_example_1.sb2 or robot_example_2.sb2

## Go to example directory

    roscd scratch4robots
    cd examples/robot_example/src

## Make the translation from Scratch to python

    rosrun scratch4robots scratch2python.py robot_example_1.sb2

## Launch the simulated world

In other terminal run:

    roslaunch kobuki_gazebo kobuki_empty_world.launch --screen

## Execute the generated code

	./robot_example_2.py ../cfg/robot_ros.yml
