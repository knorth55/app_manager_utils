# app_notifier

Notifier plugin for `app_manager`

## `app_notifier/mail_notifier_plugin`: Mail notifier plugin

### `plugin_args`: Plugin arguments

- `mail_title`: mail title
- `sender_address`: mail sender address 
- `receiver_address`: mail receiver address

### `launch_args`: Plugin launch arguments

`None`

### Sample plugin description

```
plugins:
  - name: mail_notifier_plugin
    type: app_notifier/mail_notifier_plugin
    plugin_args:
      mail_title: Test app
      sender_address: hoge
      receiver_address: hoge
```
