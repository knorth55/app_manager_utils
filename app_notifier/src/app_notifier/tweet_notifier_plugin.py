import actionlib
from app_manager import AppManagerPlugin

from app_notifier.util import tweet

from rostwitter.msg import TweetAction


class TweetNotifierPlugin(AppManagerPlugin):
    def __init__(self):
        super(TweetNotifierPlugin, self).__init__()
        self.client = None

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        client_name = plugin_args['client_name']
        image = False
        if 'image' in plugin_args:
            image = plugin_args['image']
        if image and 'image_topic_name':
            image_topic_name = plugin_args['image_topic_name']
        client = actionlib.SimpleActionClient(client_name, TweetAction)
        if ctx['exit_code'] == 0:
            tweet_text = "I succeeded to do {} app.".format(app.display_name)
        else:
            tweet_text = "I failed to do {} app.".format(app.display_name)
        if 'upload_successes' in ctx:
            if all(ctx['upload_successes']):
                tweet_text += " I succeeded to upload data."
            else:
                tweet_text += " I failed to upload data."
        tweet(
            client, tweet_text, image=image,
            image_topic_name=image_topic_name)
        return ctx
