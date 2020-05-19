import actionlib
import rospy
from sound_play.msg import SoundRequestAction
from sound_play.msg import SoundRequestGoal

from app_manager_plugin import AppManagerPlugin


def _speak(client, speech_text, lang=None):
    client.wait_for_server(timeout=rospy.Duration(1.0))
    sound_goal = SoundRequestGoal()
    sound_goal.sound_request.sound = -3
    sound_goal.sound_request.command = 1
    sound_goal.sound_request.volume = 1.0
    if lang is not None:
        sound_goal.sound_request.arg2 = lang
    sound_goal.sound_request.arg = speech_text
    client.send_goal(sound_goal)
    client.wait_for_result()
    return client.get_result()


class SpeechNotifierPlugin(AppManagerPlugin):
    def __init__(self):
        super(SpeechNotifierPlugin, self).__init__()
        self.client = None

    @classmethod
    def app_manager_start_plugin(cls, app, ctx, plugin_args):
        client_name = plugin_args['client_name']
        lang = None
        if 'lang' in plugin_args:
            lang = plugin_args['lang']
        client = actionlib.SimpleActionClient(client_name, SoundRequestAction)
        speech_text = "I'm starting {} app.".format(app.display_name)
        _speak(client, speech_text, lang=lang)
        return ctx

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        client_name = plugin_args['client_name']
        lang = None
        if 'lang' in plugin_args:
            lang = plugin_args['lang']
        client = actionlib.SimpleActionClient(client_name, SoundRequestAction)
        speech_text = "I'm stopping {} app.".format(app.display_name)
        if ctx['exit_code'] == 0:
            speech_text += "I succeeded to do {} app.".format(app.display_name)
        else:
            speech_text += "I failed to do {} app.".format(app.display_name)
        if 'upload_successes' in ctx:
            if all(ctx['upload_successes']):
                speech_text += "I succeeded to upload data."
            else:
                speech_text += "I failed to upload data."
        _speak(client, speech_text, lang=lang)
        return ctx
