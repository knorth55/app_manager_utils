#!/usr/bin/env python

import sys
import time

import rospy


def main():
    rospy.init_node('test_app')
    param1 = rospy.get_param('~param1')
    param2 = rospy.get_param('~param2')
    rospy.loginfo('test_app started.')
    rospy.loginfo('param1: {}'.format(param1))
    rospy.loginfo('param2: {}'.format(param2))
    time.sleep(30)
    rospy.loginfo('test_app stopped.')
    sys.exit(0)


if __name__ == '__main__':
    main()
