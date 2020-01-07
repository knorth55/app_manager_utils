#!/usr/bin/env roseus

(ros::roseus-add-msgs "std_msgs")

(ros::roseus "sample2")
(ros::ros-info "sample2 start")
(one-shot-publish "/app_scheduler/sample2"
                  (instance std_msgs::String :init :data "sample2"))
(ros::ros-info "sample2 finish")
(exit)
