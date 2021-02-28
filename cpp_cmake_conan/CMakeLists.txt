cmake_minimum_required(VERSION 3.14)

include( "${CMAKE_CURRENT_SOURCE_DIR}/project-meta-info.in" )

project( greeting
    VERSION ${project_version}
    DESCRIPTION ${project_description}
    LANGUAGES CXX
    )

include(${CMAKE_BINARY_DIR}/conan_paths.cmake OPTIONAL)

set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

list(FIND CMAKE_PLATFORM_IMPLICIT_LINK_DIRECTORIES "${CMAKE_INSTALL_PREFIX}/lib" isSystemDir)
if("${isSystemDir}" STREQUAL "-1")
    set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
endif("${isSystemDir}" STREQUAL "-1")

option(BUILD_SHARED_LIBS "Build shared libraries (.dll/.so) instead of static ones (.lib/.a)" ON)

add_subdirectory(library)
add_subdirectory(app)
enable_testing()
add_subdirectory(tests)
