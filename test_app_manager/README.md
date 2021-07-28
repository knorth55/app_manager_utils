# test_app_manager

Simple test package for `app_manager`

## Setup workspace

See https://github.com/knorth55/app_manager_utils#build

## Launch app_manager

Launch `app_manager` with loading `test_app_manager/apps`.

```bash
roslaunch app_manager app_manager.launch use_applist:=true applist:=$(rospack find test_app_manager)/apps
```

## Use test_app

You can start or stop the app at any time with service call.

```bash
# Start
rosservice call /robot/start_app "name: 'test_app_manager/test_app'"
# Stop
rosservice call /robot/stop_app "name: 'test_app_manager/test_app'"
```

In the app, the following plugins are executed according to `test_app.app`.

  - test\_start\_plugin
  - test\_stop\_plugin
  - result\_recorder\_plugin
  - video\_recorder\_plugin
  - rosbag\_recorder\_plugin

By default, the app will automatically close in 10 seconds.
