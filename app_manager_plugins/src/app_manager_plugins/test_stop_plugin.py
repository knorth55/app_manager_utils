import rospy


class TestStopPlugin(object):
    @classmethod
    def app_manager_start_plugin(cls, app):
        pass

    @classmethod
    def app_manager_stop_plugin(cls, app, exit_code):
        if exit_code == 0:
            rospy.loginfo('Succeeded to do task: {}'.format(app.display_name))
        else:
            rospy.logerr('Failed to do task: {}'.format(app.display_name))
