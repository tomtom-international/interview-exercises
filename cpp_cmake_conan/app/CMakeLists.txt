project(greeting_app)

add_executable(${PROJECT_NAME})
include(sources.cmake)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
        greeting_lib
)
