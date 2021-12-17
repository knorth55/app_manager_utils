^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package app_notifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.3 (2021-12-17)
------------------

0.0.2 (2021-12-11)
------------------

0.0.1 (2021-10-06)
------------------
* do not check if python-dateutil version is low
* fix bug when username is None
* add stopping notifier for speech notifier
* escape _ and - in speech notifier
* add check_timestamp_before_start
* support python3.7 and above
* refactor mail_notifier_plugin
* support for python3.7 and above
* add python-dateutil in package.xml
* Merge pull request `#22 <https://github.com/knorth55/app_manager_utils/issues/22>`_ from 708yamaguchi/use-instance
  Filter notification using timestamp
* Use python-dateutil to compare datetime.datetime
* fix typo in app_notifier/README.md
* update app_notifier README
* set default use_timestamp_title
* Merge pull request `#23 <https://github.com/knorth55/app_manager_utils/issues/23>`_ from 708yamaguchi/add-timestamp-usage
  Add use_timestamp_title usage to README.md
* Add use_timestamp_title usage to README.md
* [tweet_notifier] Filtering notification using timestamp
* [speech_notifier] Filtering notification using timestamp
* [mail_notifier] Filtering notification using timestamp
* Merge pull request `#19 <https://github.com/knorth55/app_manager_utils/issues/19>`_ from knorth55/json-speak-tweet
  Speak and tweet about object recognition result
* add space to avoid concat
* fix typo in util.py
* tweet in 280 words
* speak and tweet about object recognition
* use util functions
* add get_notification_json_paths and load_jsons
* update README.md
* format mail_notifier_plugin.py
* Merge pull request `#18 <https://github.com/knorth55/app_manager_utils/issues/18>`_ from 708yamaguchi/add-smach-notification
* Add newline between json notifications
* Do not notify location if location string is empty
* Add location information in the mail
* Add app_notification_saver dependency to app_notifier
* Use app_notification_saver in mail_notifier_plugin
* Add error message to prompt installing mailutils
* update for noetic
* update readme
* add e-mail settings link
* fix app_notifier conditions
* refactor app_notifier
* flake8
* refactor notifier english
* add stopped conditions for app notifiers
* add start plugin in TweetNotifierPlugin
* add descriptions
* update readme
* update readme in app_notifier
* add speak in tweet_notifier
* update package.xml
* add TweetNotifierPlugin
* add warning in UserSpeechNotifierPlugin
* update __init_\_.py in app_notifier
* add UserSpeechNotifierPlugin
* add util in app_notifier
* Merge pull request `#12 <https://github.com/knorth55/app_manager_utils/issues/12>`_ from knorth55/add-superlinter
* fix markdown lint
* remove app_manager_plugin package
* remove debug line in mail_notifier_plugin.py
* add use_timestamp in mail title
* update README
* refactor speech text
* fix typo
* fix typo in speech_notifier_plugin
* add SpeechNotifierPlugin
* fix typo in mail_notifier_plugin
* update readme
* add README.md
* Merge pull request `#7 <https://github.com/knorth55/app_manager_utils/issues/7>`_ from knorth55/add-plugins
* use package forma=2
* update mail_notifier_plugin
* updata plugin_args
* add mail notifier plugin
* add app_notifier package
* Contributors: Naoya Yamaguchi, Shingo Kitagawa
