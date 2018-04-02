# Getting started

Source your catkin workspace

    cd catkin_workspace
    source devel/setup.bash

You can choose between two examples file, drone_example_1.sb2 or drone_example_2.sb2


## Make the translation from Scratch to python

	roslaunch scratch4robots scratch2python_example_drone.launch file:=drone_example_1.sb2

## Launch the simulated world

In other terminal run:

    gazebo ArDrone.world

## Execute the generated code

	roscd scratch4robots
	cd examples/drone_example/src
	./drone_example_1.py drone_ice.yml
