#!/usr/bin/env python

import sys
import time

import rospy


def main():
    rospy.init_node('test_app')
    rospy.loginfo('test_app started.')
    time.sleep(10)
    rospy.loginfo('test_app stopped.')
    sys.exit(0)


if __name__ == '__main__':
    main()
