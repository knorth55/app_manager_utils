import rospy

from app_manager_plugin import AppManagerPlugin


class TestStartPlugin(AppManagerPlugin):
    def __init__(self):
        super(TestStartPlugin, self).__init__()

    @classmethod
    def app_manager_start_plugin(cls, app, ctx):
        rospy.loginfo('Testing start plugin: {}'.format(app.display_name))
