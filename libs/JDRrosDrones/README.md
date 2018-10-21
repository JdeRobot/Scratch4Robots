# Run px4


```
cd Firmware
source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/posix_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo
<!-- roslaunch px4 posix_sitl.launch -->
roslaunch px4 mavros_posix_sitl.launch


```

# Run mavros wrapper

```
roslaunch mavros px4.launch fcu_url:="udp://:14550@192.168.1.36:14557"

```
