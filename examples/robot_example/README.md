# Make the translation from Scratch to python
	
	roslaunch Scratch4Robots scratch2python_example.launch file:=robot_example.sb2

# Launch the simulated world

	roslaunch roslaunch kuboki_world.launch

or

	roslaunch kobuki-simple-world.launch

# Execute the generated code
	
	./robot_example.py robot_ros.yml
