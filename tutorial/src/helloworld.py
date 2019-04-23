#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node("talker",anonymous=True)
    pub = rospy.Publisher("chat",String,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello = 'hello world ! %s' % rospy.get_time()
        pub.publish(hello)
        rospy.loginfo(hello)
        rate.sleep()

if __name__ == "__main__":
    main()


    