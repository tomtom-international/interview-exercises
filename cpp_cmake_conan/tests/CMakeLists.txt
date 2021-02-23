cmake_minimum_required(VERSION 3.14)

include( "${CMAKE_CURRENT_SOURCE_DIR}/project-meta-info.in" )

project( greeting_test
    VERSION ${project_version}
    DESCRIPTION ${project_description}
    LANGUAGES CXX
    )

find_package( Catch2 REQUIRED )

if(NOT TARGET Tomtom::greeting_lib)
    find_package(greeting_lib CONFIG REQUIRED)
endif()

add_executable( greeting_test 
    greeting_test.cpp )

set_target_properties( greeting_app PROPERTIES 
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED YES
    )

target_link_libraries( greeting_test
    PRIVATE Tomtom::greeting_lib
    PRIVATE Catch2::Catch2
    )

add_test(UT_TEST greeting_test COMMAND greeting_test)
