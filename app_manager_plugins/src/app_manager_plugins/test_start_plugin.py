import rospy


class TestStartPlugin(object):
    @classmethod
    def app_manager_start_plugin(cls, app):
        rospy.loginfo('Testing start plugin: {}'.format(app.display_name))

    @classmethod
    def app_manager_stop_plugin(cls, app):
        pass
