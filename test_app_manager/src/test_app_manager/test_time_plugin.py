import rospy

from app_manager import AppManagerPlugin


class TestTimePlugin(AppManagerPlugin):
    def __init__(self):
        super(TestTimePlugin, self).__init__()

    def app_manager_start_plugin(self, app, ctx, plugin_args):
        self.start_time = rospy.Time.now()
        rospy.loginfo('Testing time plugin: {}'.format(app.display_name))
        rospy.loginfo('Testing time plugin: Start time is {}'.format(
            self.start_time.to_sec()))
        return ctx

    def app_manager_stop_plugin(self, app, ctx, plugin_args):
        self.stop_time = rospy.Time.now()
        rospy.loginfo('Testing time plugin: {}'.format(app.display_name))
        rospy.loginfo('Testing time plugin: Stop time is {}'.format(
            self.stop_time.to_sec()))
        rospy.loginfo('Testing time plugin: Duration is {}'.format(
            self.stop_time.to_sec() - self.start_time.to_sec()))
        return ctx
