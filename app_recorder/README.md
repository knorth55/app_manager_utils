# app_recorder

Recorder plugin for `app_manager`

## `app_recorder/video_recorder_plugin`: Video recorder plugin

### `plugin_args`: Plugin arguments

`None`

### `launch_args`: Plugin launch arguments

- `video_path`: video file directory path
- `video_title`: video file name
- `video_topic_name`: image topic name for video
- `video_fps`: video fps

### Sample plugin description

```
plugins:
  - name: video_recorder_plugin
    type: app_recorder/video_recorder_plugin
    launch_args:
      video_path: /tmp
      video_title: test.avi
      video_topic_name: /wide_stereo/right/image_rect_color
      video_fps: 20
```

## `app_recorder/rosbag_recorder_plugin`: Rosbag recorder plugin 

### `plugin_args`: Plugin arguments

`None`

### `launch_args`: Plugin launch arguments

- `rosbag_path`: rosbag file directory path
- `rosbag_title`: rosbag file name
- `rosbag_topic_names`: topic names for rosbag

### Sample plugin description

```
plugins:
  - name: rosbag_recorder_plugin
    type: app_recorder/rosbag_recorder_plugin
    launch_args:
      rosbag_path: /tmp
      rosbag_title: test.bag
      rosbag_topic_names: /tf /joint_states
```
