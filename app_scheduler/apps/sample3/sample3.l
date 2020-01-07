#!/usr/bin/env roseus

(ros::roseus-add-msgs "std_msgs")

(ros::roseus "sample3")
(ros::ros-info "sample3 start")
(ros::ros-info "publishing /app_scheduler/sample3 ...")
(one-shot-publish "/app_scheduler/sample3"
                  (instance std_msgs::String :init :data "sample3"))
(ros::ros-info "sample3 finish")
(exit)
