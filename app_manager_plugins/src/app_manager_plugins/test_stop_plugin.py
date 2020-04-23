import rospy


class TestStopPlugin(object):
    @classmethod
    def app_manager_start_plugin(cls, ctx=None):
        pass

    @classmethod
    def app_manager_stop_plugin(cls, ctx=None):
        rospy.loginfo('Testing stop plugin')
