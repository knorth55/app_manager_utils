import rospy

from sound_play.msg import SoundRequestGoal


def speak(client, speech_text, lang=None):
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
