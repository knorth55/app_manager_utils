import actionlib
from app_manager import AppManagerPlugin
import rospy

from app_notifier.util import speak

from sound_play.msg import SoundRequestAction


class UserSpeechNotifierPlugin(AppManagerPlugin):
    def __init__(self):
        super(UserSpeechNotifierPlugin, self).__init__()
        self.client = None

    @classmethod
    def app_manager_start_plugin(cls, app, ctx, plugin_args):
        client_name = plugin_args['client_name']
        username = rospy.get_param('/app_manager/running_user_name', None)
        lang = None
        if 'lang' in plugin_args:
            lang = plugin_args['lang']
        client = actionlib.SimpleActionClient(client_name, SoundRequestAction)
        if username:
            speech_text = "{} is starting {} app".format(
                username, app.display_name)
        else:
            speech_text = "Unknown user is starting {} app".format(
                app.display_name)
        speak(client, speech_text, lang=lang)
        return ctx
