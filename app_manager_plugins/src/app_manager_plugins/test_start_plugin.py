import rospy


class TestStartPlugin(object):
    @classmethod
    def app_manager_start_plugin(cls, ctx=None):
        rospy.loginfo('Testing start plugin')

    @classmethod
    def app_manager_stop_plugin(cls, ctx=None):
        pass
