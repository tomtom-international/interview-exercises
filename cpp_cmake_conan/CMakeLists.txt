cmake_minimum_required(VERSION 3.14)

include( "${CMAKE_CURRENT_SOURCE_DIR}/project-meta-info.in" )

project( greeting
    VERSION ${project_version}
    DESCRIPTION ${project_description}
    LANGUAGES CXX
    )

add_subdirectory(library)
add_subdirectory(app)
enable_testing()
add_subdirectory(tests)
