import os
import yaml

import rospy

import schedule


class AppScheduler(object):

    def __init__(self, app_service_name, yaml_path, duration=1):
        self.app_service_name = app_service_name
        self.yaml_path = yaml_path
        self.timer = rospy.Timer(rospy.Duration(duration), self._timer_cb)
        self._load_yaml()
        self._register_apps()

    def _load_yaml(self):
        with open(self.yaml_path, 'r') as yaml_f:
            self.apps = yaml.load(yaml_f)

    def _register_apps(self):
        for app in self.apps:
            self._register_app(app)

    def _register_app(self, app):
        job = self._create_job(app['app_name'])  # NOQA
        eval('schedule.{}.run(job)'.format(app['app_schedule']))

    def _create_job(self, app_name):
        job_str = 'rosservice call {0} {1}'.format(
            self.app_service_name,
            '"name: \'{}\'"'.format(app_name))

        def job():
            os.system(job_str)
        return job

    def _timer_cb(self, event):
        schedule.run_pending()
