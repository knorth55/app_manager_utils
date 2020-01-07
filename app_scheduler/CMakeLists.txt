cmake_minimum_required(VERSION 2.8.3)
project(app_scheduler)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package() 

install(DIRECTORY apps sample scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS)
