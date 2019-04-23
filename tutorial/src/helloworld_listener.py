#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ " I heard %s"%data.data)


def main():
    rospy.init_node("talker",anonymous=True)
    rospy.Subscriber("chat",String,callback)
    rospy.spin()

if __name__ == "__main__":
    main()