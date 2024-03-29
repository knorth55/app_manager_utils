# app_manager_utils

[![main](https://github.com/knorth55/app_manager_utils/actions/workflows/main.yml/badge.svg)](https://github.com/knorth55/app_manager_utils/actions/workflows/main.yml)
[![linter](https://github.com/knorth55/app_manager_utils/actions/workflows/linter.yaml/badge.svg)](https://github.com/knorth55/app_manager_utils/actions/workflows/linter.yaml)

## Dependency

- [PR2/app_manager kinetic-devel branch](https://github.com/PR2/app_manager)
- [python-dateutil >= 2.7.0](https://github.com/dateutil/dateutil)

## Build

```bash
mkdir ~/catkin_ws/src -p
cd ~/catkin_ws/src
wstool init
wstool merge  https://raw.githubusercontent.com/knorth55/app_manager_utils/master/fc.rosinstall
wstool up
rosdep install --ignore-src --from-path . -y -r
cd ~/catkin_ws
catkin build
```

## app_scheduler

Scheduler for `app_manager`

For detailed information, please read [app_scheduler](app_scheduler/README.md).

## app_recorder

Recorder plugin for `app_manager`

For detailed information, please read [app_recorder](app_recorder/README.md).

## app_uploader

Uploader plugin for `app_manager`

For detailed information, please read [app_uploader](app_uploader/README.md).

## app_notifier

Notifier plugin for `app_manager`

For detailed information, please read [app_notifier](app_notifier/README.md).

## app_notification_saver

Notification saver plugin for `app_manager`

For detailed information, please read [app_notification_saver](app_notification_saver/README.md).

## app_publisher

Publisher plugin for `app_manager`

For detailed information, please read [app_publisher](app_publisher/README.md).

## test_app_manager

Simple test package for `app_manager`

For detailed information, please read [test_app_manager](test_app_manager/README.md).
