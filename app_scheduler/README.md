# app_scheduler

Scheduler for `app_manager` with `schedule` python package

## Sample launch

```bash
roslaunch app_scheduler sample_app_scheduler.launch
```

## Sample schedule yaml

You can set schedule with `schedule` python package syntax.

```yaml
- name: sample0
  app_name: app_scheduler/sample0
  app_schedule:
    start: every(2).minutes
- name: sample1
  app_name: app_scheduler/sample1
  app_schedule:
    start: every(60).seconds
- name: sample2
  app_name: app_scheduler/sample2
  app_schedule:
    start: every(1).hour
- name: sample3
  app_name: app_scheduler/sample3
  app_schedule:
    start: every().day.at("10:00:00")
    stop: every().day.at("10:00:03")
```
