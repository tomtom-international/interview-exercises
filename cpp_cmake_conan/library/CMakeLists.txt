cmake_minimum_required(VERSION 3.14)

include( "${CMAKE_CURRENT_SOURCE_DIR}/project-meta-info.in" )

project( greeting_lib
    VERSION ${project_version}
    DESCRIPTION ${project_description}
    LANGUAGES CXX
    )

add_library( greeting_lib
    SHARED
    )

target_sources( greeting_lib
    PRIVATE greeting.cpp
    )

target_include_directories( greeting_lib PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
    )

set_target_properties( greeting_lib PROPERTIES 
    CXX_STANDARD 11
    CXX_STANDARD_REQUIRED YES
    PUBLIC_HEADER include/greeting.h
    )

install( TARGETS greeting_lib EXPORT greeting_lib_targets
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include
    RUNTIME DESTINATION bin
    )

install( EXPORT greeting_lib_targets
    DESTINATION lib/cmake/greeting_lib
    FILE greeting_libConfigTargets.cmake
    NAMESPACE Tomtom::
    )

include( CMakePackageConfigHelpers )

write_basic_package_version_file( greeting_libConfigVersion.cmake
    COMPATIBILITY SameMajorVersion
)
install(FILES greeting_libConfig.cmake ${CMAKE_CURRENT_BINARY_DIR}/greeting_libConfigVersion.cmake
    DESTINATION lib/cmake/greeting_lib
    )

add_library( Tomtom::greeting_lib ALIAS greeting_lib)
