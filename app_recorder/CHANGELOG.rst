^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package app_recorder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.7 (2023-04-02)
------------------
* Merge pull request `#56 <https://github.com/knorth55/app_manager_utils/issues/56>`_ from knorth55/jsk-rosbag-tools-fix-import
  fix import of jsk_rosbag_tools
* skip using bag_to_audio/video in plugin
* fix import of jsk_rosbag_tools
* Contributors: Shingo Kitagawa

0.0.6 (2022-07-29)
------------------
* Merge pull request `#54 <https://github.com/knorth55/app_manager_utils/issues/54>`_ from 708yamaguchi/rosbag-converter
* [app_recorder] Exit if jsk_rosbag_tools is not found
* Avoid linter error: E501 line too long (80 > 79 characters)
* [app_recorder] Use rospy.logerr() instead of print()
* Add README.md
* [app_recorder] Add rosbag converter plugins
* Contributors: Naoya Yamaguchi, Shingo Kitagawa

0.0.5 (2022-02-08)
------------------

0.0.4 (2021-12-27)
------------------
* Merge pull request `#46 <https://github.com/knorth55/app_manager_utils/issues/46>`_ from 708yamaguchi/save-ctx-as-result
* [app_recorder] Save ctx directly as app result
* Contributors: Naoya Yamaguchi, Shingo Kitagawa

0.0.3 (2021-12-17)
------------------

0.0.2 (2021-12-11)
------------------

0.0.1 (2021-10-06)
------------------
* update readme
* add machine tag in rosbag_recorder
* add machine tag in audio_recorder.launch
* set default machine_file
* Merge pull request `#34 <https://github.com/knorth55/app_manager_utils/issues/34>`_ from knorth55/use-decompressed-name
  use decompressed topic name
* use decompressed topic name
* Merge pull request `#32 <https://github.com/knorth55/app_manager_utils/issues/32>`_ from 708yamaguchi/machine-name
* load machine file
* Add machine to audio_video_recorder
* Add machine to video_recorder
* Merge pull request `#31 <https://github.com/knorth55/app_manager_utils/issues/31>`_ from 708yamaguchi/compressed-video-recorder
* Do not change video_topic_name
* Use anon to node name for multiple use
* Add default value to video_compressed_topic_name in audio_video_recorder
* Add default value to video_compressed_topic_name
* Add image_transport dependency
* Add option to record compressed audio video
* Add option to record compressed video
* update app_recorder/README.md
* update README.md
* update for noetic
* remove do_timestamp param
* update file_name
* linter
* update app_recorder readme
* add stopped in result_recorder_plugin
* add audio_video_recorder plugin
* add ResultRecorderPlugin
* Merge pull request `#8 <https://github.com/knorth55/app_manager_utils/issues/8>`_ from 708yamaguchi/add-audio-recorder
  Add audio record plugin
* Add audio record plugin
* add video_codec in video_recorder.launch
* remove app_manager_plugin package
* add compress option in rosbag_recorder
* use module: null syntax
* update readme
* add README.md
* Merge pull request `#7 <https://github.com/knorth55/app_manager_utils/issues/7>`_ from knorth55/add-plugins
* use package forma=2
* refactor app_recorder app_uploader package.xml
* fix app_recorder plugin names
* fix typo
* add plugin name
* add RosbagRecorderPlugin and VideoRecorderPlugin
* add app_recorder package
* Contributors: Naoya Yamaguchi, Shingo Kitagawa
