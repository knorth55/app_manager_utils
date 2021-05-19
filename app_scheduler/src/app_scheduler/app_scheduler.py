import yaml

import rospy

import schedule

from app_manager.msg import AppList
from app_manager.msg import AppStatus
from app_manager.srv import StartApp
from app_manager.srv import StopApp


class AppScheduler(object):

    def __init__(self, robot_name, yaml_path, duration, update_duration):
        self.robot_name = robot_name
        self.yaml_path = yaml_path
        self.running_app_names = []
        self.running_jobs = {}
        self.app_list_topic_name = '/{}/app_list'.format(self.robot_name)
        self.start_app = rospy.ServiceProxy(
            '/{}/start_app'.format(self.robot_name), StartApp)
        self.stop_app = rospy.ServiceProxy(
            '/{}/stop_app'.format(self.robot_name), StopApp)
        self.job_timer = rospy.Timer(rospy.Duration(duration), self._timer_cb)
        self.update_timer = rospy.Timer(
            rospy.Duration(update_duration), self._update_timer_cb)
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
                'register app schedule => name: {0}, app_name: {1}'.format(
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
        try:
            msg = rospy.wait_for_service(
                self.app_list_topic_name, AppList, timeout=1)
        except Exception as e:
            rospy.logwarn(
                'Failed to subscribe {}: {}'.format(
                    self.app_list_topic_name, e))
            return
        self.running_app_names = [x.name for x in msg.running_apps]

    def _update_running_jobs(self):
        for name, job_data in self.running_jobs.items():
            if (job_data['running']
                    and job_data['app_name'] not in self.running_app_names):
                self.running_jobs[name]['running'] = False

    def _timer_cb(self, event):
        schedule.run_pending()

    def _update_timer_cb(self, event):
        self._update_running_app_names()
        self._update_running_jobs()

    def _sub_cb(self, msg):
        if msg.type == AppStatus.INFO:
            # INFO
            rospy.loginfo('app_scheduler: {}'.format(msg.status))
        elif msg.type == AppStatus.WARN:
            # WARN
            rospy.logwarn('app_scheduler: {}'.format(msg.status))
        else:
            # ERROR
            rospy.logerr('app_scheduler: {}'.format(msg.status))
