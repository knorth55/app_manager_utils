# app_manager_utils
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knorth55/app_manager_utils/CI)

## Build 

```
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

## test_app_manager

Simple test package for `app_manager`
