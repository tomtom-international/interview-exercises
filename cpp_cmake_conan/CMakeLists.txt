cmake_minimum_required(VERSION 3.14)

project(greeting)#subprojects

include_directories(${PROJECT_SOURCE_DIR}/library)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


add_subdirectory(library)
add_subdirectory(app)


