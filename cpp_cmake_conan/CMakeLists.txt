cmake_minimum_required(VERSION 3.14)

project(greeting)

include_directories(${PROJECT_SOURCE_DIR}/library)
include_directories(${PROJECT_SOURCE_DIR}/tests)
include_directories(${PROJECT_SOURCE_DIR}/tests/catch2/catch2)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(library)
add_subdirectory(tests)
add_subdirectory(app)

enable_testing()
add_test(test_all tests/unit_tests)


