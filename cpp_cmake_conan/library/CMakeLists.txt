project(greeting_lib)

add_library(${PROJECT_NAME})

include(sources.cmake)

set_target_properties(${PROJECT_NAME}
    PROPERTIES
        CXX_STANDARD 11
)

target_include_directories(${PROJECT_NAME}
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include/
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src/
)
