import rospy

from app_manager import AppManagerPlugin


class TestStopPlugin(AppManagerPlugin):
    def __init__(self):
        super(TestStopPlugin, self).__init__()

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        if ctx['exit_code'] == 0:
            rospy.loginfo('Succeeded to do task: {}'.format(app.display_name))
        else:
            rospy.logerr('Failed to do task: {}'.format(app.display_name))
        return ctx
