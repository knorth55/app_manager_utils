import yaml

import rospy

import schedule

from app_manager.msg import AppStatus
from app_manager.srv import ListApps
from app_manager.srv import StartApp
from app_manager.srv import StopApp


class AppScheduler(object):

    def __init__(self, robot_name, yaml_path, duration):
        self.robot_name = robot_name
        self.yaml_path = yaml_path
        self.running_app_names = []
        self.running_jobs = {}
        self.list_apps = rospy.ServiceProxy(
            '/{}/list_apps'.format(self.robot_name), ListApps)
        self.start_app = rospy.ServiceProxy(
            '/{}/start_app'.format(self.robot_name), StartApp)
        self.stop_app = rospy.ServiceProxy(
            '/{}/stop_app'.format(self.robot_name), StopApp)
        self.timer = rospy.Timer(rospy.Duration(duration), self._timer_cb)
        self.sub = rospy.Subscriber(
            '/{}/application/app_status'.format(self.robot_name),
            AppStatus, self._sub_cb)
        self._load_yaml()
        self._register_apps()

    def _load_yaml(self):
        with open(self.yaml_path, 'r') as yaml_f:
            self.apps = yaml.load(yaml_f)

    def _register_apps(self):
        for app in self.apps:
            rospy.loginfo(
                'register app schedule: {0} {1}'.format(
                    app['name'], app['app_name']))
            self._register_app(app)

    def _register_app(self, app):
        app_schedule = app['app_schedule']
        start_job = self._create_start_job(app['name'], app['app_name'])  # NOQA
        eval('schedule.{}.do(start_job)'.format(app_schedule['start']))
        if 'stop' in app_schedule:
            stop_job = self._create_stop_job(app['name'], app['app_name'])  # NOQA
            eval('schedule.{}.do(stop_job)'.format(app_schedule['stop']))

    def _create_start_job(self, name, app_name):
        def start_job():
            start_res = self.start_app(app_name)
            self.running_jobs[name] = {
                'app_name': app_name,
                'running': start_res.started
            }
        return start_job

    def _create_stop_job(self, name, app_name):
        def stop_job():
            if app_name in self.running_app_names:
                stop_res = self.stop_app(app_name)
                self.running_jobs[name] = {
                    'app_name': app_name,
                    'running': not stop_res.stopped
                }
        return stop_job

    def _update_running_app_names(self):
        list_apps_res = self.list_apps()
        self.running_app_names = [x.name for x in list_apps_res.running_apps]

    def _update_running_jobs(self):
        for name, job_data in self.running_jobs.items():
            if (job_data['running']
                    and job_data['app_name'] not in self.running_app_names):
                self.running_jobs[name]['running'] = False

    def _timer_cb(self, event):
        self._update_running_app_names()
        self._update_running_jobs()
        schedule.run_pending()

    def _sub_cb(self, msg):
        # INFO
        if msg.type == AppStatus.INFO:
            rospy.loginfo('app_scheduler: {}'.format(msg.status))
        # WARN
        elif msg.type == AppStatus.WARN:
            rospy.logwarn('app_scheduler: {}'.format(msg.status))
        # ERROR
        else:
            rospy.logerr('app_scheduler: {}'.format(msg.status))
