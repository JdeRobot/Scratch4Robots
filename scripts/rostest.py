#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Empty


def land():
    pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

def takeoff():
    pub = rospy.Publisher("ardrone/takeoff", Empty, queue_size=10 )
    rospy.init_node('takeoff', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

if __name__ == '__main__':
    try:
        takeoff()
        # time.sleep(2)
        # land()
    except rospy.ROSInterruptException:
        pass

# if __name__ == '__main__':
#     try:
#         rospy.init_node('fly_x_meters', anonymous=True)
#         rate = rospy.Rate(10)  # 10hz
#         pub_takeoff = rospy.Publisher("ardrone/takeoff", Empty, queue_size=1)
#         pub_land = rospy.Publisher("ardrone/land", Empty, queue_size=1)
#         pub_twist = rospy.Publisher("cmd_vel", Twist, queue_size=1)
#         pub_reset = rospy.Publisher("ardrone/reset", Empty, queue_size=10)
#
#         hover_msg = Twist()
#         hover_msg.linear.x = 0
#         hover_msg.linear.y = 0
#         hover_msg.linear.z = 0
#         hover_msg.angular.x = 0
#         hover_msg.angular.y = 0
#         hover_msg.angular.z = 0
#
#         # starts simulated clock
#         while rospy.get_time() == 0:
#             rospy.get_time()
#
#         start_time = rospy.get_time()
#         print(start_time)
#
#         while not rospy.is_shutdown():
#             print(rospy.get_time())
#             if rospy.get_time() < start_time+3.0:
#                 pub_takeoff.publish(Empty())
#                 pub_twist.publish(hover_msg)
#             elif rospy.get_time() > start_time+10.0:
#                 pub_reset.publish(Empty())
#                 break
#             elif rospy.get_time() > start_time+8.0:
#                 pub_twist.publish(hover_msg)
#                 pub_land.publish(Empty())
#             else:
#                 pub_twist.publish(hover_msg)
#             rate.sleep()
#
#     except rospy.ROSInterruptException:
#         pass
