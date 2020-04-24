#!/usr/bin/env python


import time

import rospy


def main():
    rospy.init_node('test_app')
    rospy.loginfo('test_app started.')
    time.sleep(10)
    rospy.loginfo('test_app stopped.')
    rospy.signal_shutdown(0)


if __name__ == '__main__':
    main()
