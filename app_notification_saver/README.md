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

The sample output of the json file is like below:
```
{
    "object recognition": [
        {
            "date": "2021-07-28T19:17:59",
            "message": "Dish is found"
        },
        {
            "date": "2021-07-28T19:18:09",
            "message": "Cup is found"
        }
    ],
    "navigation failure": [
        {
            "date": "2021-07-28T19:18:29",
            "message": "Stucked in front of the chair"
        }
    ]
}
```

## Parameters
- `~json_path` (`String`, default: `/tmp/app_notification.json`)

  Path to json file which contains app notification
