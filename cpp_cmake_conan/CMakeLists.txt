cmake_minimum_required(VERSION 3.14)

project(greeting)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

add_subdirectory(app)
add_subdirectory(library)
add_subdirectory(tests)
