import importlib

from app_manager import AppManagerPlugin
import rospy


class RostopicPublisherPlugin(AppManagerPlugin):
    def __init__(self):
        super(RostopicPublisherPlugin, self).__init__()

    def publish_topic(self, topic):
        msg = getattr(
            importlib.import_module(
                '{}.msg'.format(topic['pkg'])), topic['type'])
        pub = rospy.Publisher(topic['name'], msg, queue_size=1)
        rospy.sleep(1)
        pub.publish(msg())

    def app_manager_start_plugin(self, app, ctx, plugin_args):
        if 'start_topics' not in plugin_args:
            return
        topics = plugin_args['start_topics']
        for topic in topics:
            self.publish_topic(topic)

    def app_manager_stop_plugin(self, app, ctx, plugin_args):
        if 'stop_topics' not in plugin_args:
            return
        topics = plugin_args['stop_topics']
        for topic in topics:
            self.publish_topic(topic)
