cmake_minimum_required(VERSION 3.5)
project(rover_navigation)

# Find dependencies
find_package(ament_cmake REQUIRED)

install(
  DIRECTORY launch params behavior_trees
  DESTINATION share/${PROJECT_NAME}
)

ament_package()