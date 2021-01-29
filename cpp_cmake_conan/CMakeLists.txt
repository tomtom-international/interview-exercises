cmake_minimum_required(VERSION 3.14)

project(greeting)

include_directories(${PROJECT_SOURCE_DIR}/library)
include_directories(${PROJECT_SOURCE_DIR}/build/bin)

# Included the conan build information
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(library)
add_subdirectory(tests)
add_subdirectory(app)

enable_testing()
add_test(NAME greet COMMAND "tests"
         WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/build/bin
)
