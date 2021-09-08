# app_publisher

ROS topic publisher plugin for `app_manager`

## `app_manager` plugins

### `app_notifier/rostopic_publisher_plugin`: ROS topic publisher plugin

This plugin publishes ROS topic at the beginning or end of the app.

#### `plugin_args`: Plugin arguments

- `start_topics`: topic which is published at the beginning of app
  - `name`: name of the topic
  - `pkg`: package name of the message
  - `type`: type of the message
- `stop_topics`: topic which is published at the end of app
  - `name`: name of the topic
  - `pkg`: package name of the message
  - `type`: type of the message
  - `field`: content of the message field

#### `launch_args`: Plugin launch arguments

`None`

#### Sample plugin description

```yaml
plugin_args:
  start_topics:
    - name: /test_bool
      pkg: std_msgs
      type: Bool
    - name: /test_polygon_stamped
      pkg: geometry_msgs
      type: PolygonStamped
      field:
        header:
          seq: 0
          stamp:
            secs: 1631124596
            nsecs: 589318
          frame_id: /test
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
  stop_topics:
    - name: /test_cancel
      pkg: actionlib_msgs
      type: GoalID
```
