# app_publisher

ROS topic publisher plugin for `app_manager`

## `app_manager` plugins

### `app_notifier/rostopic_publisher_plugin`: ROS topic publisher plugin

This plugin publishes ROS topic at the beginning or end of the app.

#### `plugin_args`: Plugin arguments

- `start_topics`: topic which is published at the beginning of app
  - `name`: name of the topic
    `pkg`: package name of the message
    `type`: type of the message
- `stop_topics`: topic which is published at the end of app
  - `name`: name of the topic
    `pkg`: package name of the message
    `type`: type of the message

#### `launch_args`: Plugin launch arguments

`None`

#### Sample plugin description

```yaml
plugin_args:
  start_topics:
    - name: /test_bool1
      pkg: std_msgs
      type: Bool
    - name: /test_bool2
      pkg: std_msgs
      type: Bool
  stop_topics:
    - name: /test_cancel
      pkg: actionlib_msgs
      type: GoalID
```
