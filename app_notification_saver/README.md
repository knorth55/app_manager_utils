# app_notification_saver

Save notification to json file to pass it to `app_notifier`.

## ServiceNotificationSaver

Save notification via service call.

### Launch service_notification_saver node

```bash
roslaunch app_notification_saver service_notification_saver.launch
```

### Save app notification

You can save app notification with service call.

```bash
rosservice call /service_notification_saver/save_app_notification "title: 'object recognition'
stamp:
  secs: 1627467479
  nsecs: 13279914
location: 'kitchen'
message: 'Dish is found'"
```

You can also clear app notification.

```bash
rosservice call /service_notification_saver/clear_app_notification "{}"
```

The sample output of the json file is like below:

```json
{
    "object recognition": [
        {
            "date": "2021-07-28T19:17:59",
            "message": "Dish is found",
            "location": "kitchen"
        },
        {
            "date": "2021-07-28T19:18:09",
            "message": "Cup is found",
            "location": "kitchen"
        }
    ],
    "navigation failure": [
        {
            "date": "2021-07-28T19:18:29",
            "message": "Stucked in front of the chair",
            "location": "living room"
        }
    ]
}
```

### Parameters

- `~json_path` (`String`, default: `/tmp/app_notification.json`)

  Path to json file which contains app notification
