display: Test app
platform: all
launch: test_app_manager/test_app.xml
interface: test_app_manager/test_app.interface
plugins:
  - name: test_start_plugin
    type: app_manager_plugin/test_start_plugin
  - name: test_stop_plugin
    type: app_manager_plugin/test_stop_plugin
