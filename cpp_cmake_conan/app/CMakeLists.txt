cmake_minimum_required(VERSION 3.14)

include( "${CMAKE_CURRENT_SOURCE_DIR}/project-meta-info.in" )

project( greeting_app
    VERSION ${project_version}
    DESCRIPTION ${project_description}
    LANGUAGES CXX
    )

if(NOT TARGET Tomtom::greeting_lib)
    find_package(greeting_lib CONFIG REQUIRED)
endif()

add_executable( greeting_app
        main.cpp
        )

target_include_directories( greeting_app
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include
    )

set_target_properties( greeting_app PROPERTIES
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED YES
    )

target_link_libraries( greeting_app
                        PRIVATE Tomtom::greeting_lib
                        )

install( TARGETS greeting_app
    RUNTIME DESTINATION bin
    )
