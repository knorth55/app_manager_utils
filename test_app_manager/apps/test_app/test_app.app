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
  - name: test_time_plugin
    type: test_app_manager/test_time_plugin
  - name: test_rostopic_publisher_plugin
    type: app_publisher/rostopic_publisher_plugin
    plugin_args:
      start_topics:
        - name: /test_bool
          pkg: std_msgs
          type: Bool
          field:
            data: true
      stop_topics:
        - name: /test_polygon_stamped
          pkg: geometry_msgs
          type: PolygonStamped
          field:
            header:
              seq: 0
              stamp: now
              frame_id: test
            polygon:
              points:
                - x: 1
                  y: 0
                  z: 0
                - x: 0
                  y: 1
                  z: 0
                - x: 0
                  y: 0
                  z: 1
          cond:
            - success
            - stopped
  - name: result_recorder_plugin
    type: app_recorder/result_recorder_plugin
    plugin_args:
      result_path: /tmp
      retult_title: result.yaml
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
    - test_time_plugin
    - test_rostopic_publisher_plugin
    - result_recorder_plugin
    - video_recorder_plugin
    - rosbag_recorder_plugin
  stop_plugin_order:
    - test_start_plugin
    - test_stop_plugin
    - test_time_plugin
    - test_rostopic_publisher_plugin
    - result_recorder_plugin
    - video_recorder_plugin
    - rosbag_recorder_plugin
