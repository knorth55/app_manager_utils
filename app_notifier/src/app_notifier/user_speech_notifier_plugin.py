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
        if 'warning' in plugin_args:
            warning = plugin_args['warning']
        else:
            warning = False
        username = rospy.get_param('/app_manager/running_user_name', None)

        speech_text = None
        if username:
            speech_text = "{} is starting {} app".format(
                username, app.display_name)
        elif warning:
            speech_text = "Unknown user is starting {} app".format(
                app.display_name)

        if speech_text is not None:
            lang = None
            if 'lang' in plugin_args:
                lang = plugin_args['lang']
            client = actionlib.SimpleActionClient(
                client_name, SoundRequestAction)
            speak(client, speech_text, lang=lang)
        return ctx
