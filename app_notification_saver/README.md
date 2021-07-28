# app_notification_saver

Save notification to json file to pass it to `app_notifier`.

## Launch app_notification_saver node
```bash
rosrun app_notification_saver app_notification_saver_node.py
```

## Save app notification
You can save app notification with service call.
```bash
rosservice call /app_notification_saver/save_app_notification "stamp:
  secs: 1627467479
  nsecs: 13279914
type: 'object detection'
message: 'Dish is found'"
```

You can also clear app notification.
```bash
rosservice call /app_notification_saver/clear_app_notification "{}"
```

## Parameters
- `~json_path` (`String`, default: `/tmp/app_notification.json`)

  Path to json file which contains app notification
