#!/usr/bin/env python

import datetime
import json
import os
import rospy
from std_srvs.srv import Empty, EmptyResponse
from app_notification_saver.srv import SaveAppNotification, SaveAppNotificationResponse # NOQA


class AppNotificationSaver(object):
    def __init__(self):
        self.json_path = rospy.get_param(
            '~json_path', '/tmp/app_notification.json')
        rospy.Service(
            '~save_app_notification',
            SaveAppNotification,
            self.save_app_notification_cb)
        rospy.Service(
            '~clear_app_notification',
            Empty,
            self.clear_app_notification_cb)

    def save_app_notification_cb(self, req):
        # Load notification json
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r') as j:
                notification = json.load(j)
        else:
            notification = {}
        # Append notification
        stamp = datetime.datetime.fromtimestamp(float(req.stamp.secs))
        new_notification = {'date': stamp.isoformat(),
                            'message': req.message}
        if req.type in notification:
            notification[req.type].append(new_notification)
        else:
            notification[req.type] = [new_notification]
        # Dump json
        with open(self.json_path, 'w') as j:
            json.dump(notification, j, indent=4)
        rospy.loginfo(json.dumps(notification, indent=4))
        return SaveAppNotificationResponse(True)

    def clear_app_notification_cb(self, req):
        if os.path.exists(self.json_path):
            os.remove(self.json_path)
            rospy.loginfo('Remove file {}'.format(self.json_path))
        return EmptyResponse()


if __name__ == '__main__':
    rospy.init_node('app_notification_saver')
    AppNotificationSaver()
    rospy.spin()
