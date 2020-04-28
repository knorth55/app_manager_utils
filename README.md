# app_manager_utils
[![](https://travis-ci.com/knorth55/app_manager_utils.svg?branch=master)](https://travis-ci.com/github/knorth55/app_manager_utils)

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

## app_manager_plugin

Plugin base script for `app_manager`

**Caution**

`app_manager_plugin` depends on [knorth55/app_manager@add-app-manager-plugin](https://github.com/knorth55/app_manager/tree/add-app-manager-plugin)  branch.

## app_recorder

Recorder plugin for `app_manager`

For detailed information, please read [app_recorder](app_recorder/README.md).

**Caution**

`app_recorder` depends on [knorth55/app_manager@add-app-manager-plugin](https://github.com/knorth55/app_manager/tree/add-app-manager-plugin)  branch.

## app_uploader

Uploader plugin for `app_manager`

For detailed information, please read [app_uploader](app_uploader/README.md).

**Caution**

`app_uploader` depends on [knorth55/app_manager@add-app-manager-plugin](https://github.com/knorth55/app_manager/tree/add-app-manager-plugin)  branch.

## app_notifier

Notifier plugin for `app_manager`

For detailed information, please read [app_notifier](app_notifier/README.md).

**Caution**

`app_notifier` depends on [knorth55/app_manager@add-app-manager-plugin](https://github.com/knorth55/app_manager/tree/add-app-manager-plugin)  branch.

## test_app_manager

Simple test package for `app_manager`
