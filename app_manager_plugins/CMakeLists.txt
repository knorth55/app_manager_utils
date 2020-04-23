cmake_minimum_required(VERSION 2.8.3)
project(app_manager_plugins)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

include_directories()

install(DIRECTORY apps launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
