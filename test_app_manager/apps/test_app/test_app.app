display: Test app
platform: all
launch: test_app_manager/test_app.xml
interface: test_app_manager/test_app.interface
timeout: 300 
plugins:
  - name: test_start_plugin
    type: test_app_manager/test_start_plugin
  - name: test_stop_plugin
    type: test_app_manager/test_stop_plugin
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
      rosbag_topic_names:
        - /tf
        - /joint_states
plugin_order:
  start_plugin_order:
    - test_start_plugin
    - test_stop_plugin
    - video_recorder_plugin
    - rosbag_recorder_plugin
  stop_plugin_order:
    - test_start_plugin
    - test_stop_plugin
    - video_recorder_plugin
    - rosbag_recorder_plugin
