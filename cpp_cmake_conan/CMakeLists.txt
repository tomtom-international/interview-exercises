cmake_minimum_required(VERSION 3.14)

project(greeting LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(app)
add_subdirectory(library)

enable_testing()
add_subdirectory(tests)
