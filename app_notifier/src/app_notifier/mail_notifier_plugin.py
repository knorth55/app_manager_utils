import subprocess

import rospy

from app_manager_plugin import AppManagerPlugin


class MailNotifierPlugin(AppManagerPlugin):
    def __init__(self):
        super(MailNotifierPlugin, self).__init__()

    @classmethod
    def app_manager_stop_plugin(cls, app, ctx, plugin_args):
        mail_title = plugin_args['mail_notifier_title']
        sender_address = plugin_args['mail_notifier_sender_address']
        receiver_address = plugin_args['mail_notifier_receiver_address']
        if ctx['exit_code'] == 0:
            mail_content = "I succeeded to do {}.".format(app.display_name)
        else:
            mail_content = "I failed to do {}".format(app.display_name)
        cmd = "LC_CTYPE=en_US.UTF-8 /bin/echo -e \"{}\"".format(mail_content)
        cmd += " | /usr/bin/mail -s \"{}\" -r {} {}".format(
            mail_title, sender_address, receiver_address)
        exit_code = subprocess.call(cmd, shell=True)
        if exit_code > 0:
            rospy.logerr(
                'Failed to send e-mail:  {} -> {}'.format(
                    sender_address, receiver_address))
        else:
            rospy.loginfo(
                'Succeeded to send e-mail: {} -> {}'.format(
                    sender_address, receiver_address))
        ctx['mail_notifier_exit_code'] = exit_code
        return ctx
