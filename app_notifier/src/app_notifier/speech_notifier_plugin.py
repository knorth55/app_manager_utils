import actionlib
from app_manager import AppManagerPlugin

from app_notifier.util import speak

from sound_play.msg import SoundRequestAction


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
        speak(client, speech_text, lang=lang)
        return ctx

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        client_name = plugin_args['client_name']
        lang = None
        if 'lang' in plugin_args:
            lang = plugin_args['lang']
        client = actionlib.SimpleActionClient(client_name, SoundRequestAction)
        if ctx['exit_code'] == 0:
            speech_text = "I succeeded to do {} app.".format(app.display_name)
        else:
            speech_text = "I failed to do {} app.".format(app.display_name)
        if 'upload_successes' in ctx:
            if all(ctx['upload_successes']):
                speech_text += " I succeeded to upload data."
            else:
                speech_text += " I failed to upload data."
        speak(client, speech_text, lang=lang)
        return ctx
