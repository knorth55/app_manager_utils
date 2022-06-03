from jsk_rosbag_tools.bag_to_audio import bag_to_audio
import os
import rospy

from app_manager import AppManagerPlugin


class RosbagAudioConverterPlugin(AppManagerPlugin):
    def __init__(self):
        super(RosbagAudioConverterPlugin, self).__init__()

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        rosbag_file_path = os.path.join(
            str(plugin_args['rosbag_path']),
            str(plugin_args['rosbag_title']))
        kwargs = {'wav_outpath': str(plugin_args['audio_path']),
                  'topic_name': str(plugin_args['audio_topic_name']),
                  'samplerate': int(plugin_args['audio_sample_rate']),
                  'channels': int(plugin_args['audio_channels'])}
        try:
            bag_to_audio(rosbag_file_path, **kwargs)
        except ValueError as e:
            # topic is not included in bagfile
            rospy.logerr('{}'.format(e))
        return ctx
