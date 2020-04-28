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

### Sample plugin description

```
display: Test app
platform: all
launch: test_app_manager/test_app.xml
interface: test_app_manager/test_app.interface
plugins:
  - name: test_start_plugin
    type: app_manager_plugin/test_start_plugin
  - name: test_stop_plugin
    type: app_manager_plugin/test_stop_plugin
  - name: video_recorder_plugin
    type: app_recorder/video_recorder_plugin
    launch_args:
      video_path: /tmp
      video_title: test.avi
      video_topic_name: /wide_stereo/right/image_rect_color
      video_fps: 20
  - name: rosbag_recorder_plugin
    type: app_recorder/rosbag_recorder_plugin
    launch_args:
      rosbag_path: /tmp
      rosbag_title: test.bag
      rosbag_topic_names: /tf /joint_states
  - name: gdrive_uploader_plugin
    type: app_uploader/gdrive_uploader_plugin
    plugin_args:
      upload_file_paths:
        - /tmp/test.avi
        - /tmp/test.bag
      upload_file_titles:
        - test.avi
        - test.bag
      upload_parents_path: logs
      upload_server_name: /gdrive_server
  - name: mail_notifier_plugin
    type: app_notifier/mail_notifier_plugin
    plugin_args:
      mail_title: Test app
      sender_address: hoge
      receiver_address: hoge
```

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
