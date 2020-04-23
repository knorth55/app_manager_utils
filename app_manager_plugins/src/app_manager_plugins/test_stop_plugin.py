import rospy


class TestStopPlugin(object):
    @classmethod
    def app_manager_start_plugin(cls, app):
        pass

    @classmethod
    def app_manager_stop_plugin(cls, app):
        rospy.loginfo('Testing stop plugin: {}'.format(app.display_name))
