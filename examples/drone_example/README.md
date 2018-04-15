# Getting started

You have an example here:
https://www.youtube.com/watch?v=IVLTRkUutAk

## Prepare your workspace

This example is ready for work with comm library, ICE and ROS communications are allowed

Source your catkin workspace

    cd catkin_workspace
    source devel/setup.bash

You can choose between two examples file, drone_example_1.sb2 or drone_example_2.sb2

## Go to example directory

    roscd scratch4robots
    cd examples/drone_example/src

## Make the translation from Scratch to python

    rosrun scratch4robots scratch2python.py drone_example_1.sb2

## Launch the simulated world

In other terminal run:

    gazebo ArDrone.world

## Execute the generated code

	./drone_example_1.py ../cfg/drone_ice.yml
