cmake_minimum_required(VERSION 3.14)

project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

if(NOT TARGET Tomtom::greeting_lib)
    find_package(greeting_lib CONFIG REQUIRED)
endif()

add_executable(example example.cpp)

target_link_libraries( example
                        PRIVATE Tomtom::greeting_lib
                        )

