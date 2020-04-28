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
      upload_parents_path: logs/20200428_app_manager_utils_test
      upload_server_name: /gdrive_server
  - name: mail_notifier_plugin
    type: app_notifier/mail_notifier_plugin
    plugin_args:
      mail_title: Test app
      sender_address: hoge
      receiver_address: hoge
