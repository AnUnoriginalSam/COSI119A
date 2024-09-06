#!/usr/bin/env python3
import math
import rospy
from geometry_msgs.msg import Point, Pose, Twist
from tf.transformations import euler_from_quaternion

MAX_TIME_SEC = 60
SPEED = 0.3

# BasicMoverPA
class BasicMoverPA:
    def __init__(self):
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.twist = Twist()

    def run(self):
        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            if True:
                #accel
                self.twist.linear.x = SPEED / 2
                self.twist.angular.z = SPEED
            #elif false:
                #decel
            else:
                return
            self.cmd_vel_pub.publish(self.twist)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('basic_mover_pa')
    BasicMoverPA().run()
