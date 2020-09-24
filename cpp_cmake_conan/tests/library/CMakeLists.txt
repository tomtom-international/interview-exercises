project(greeting_lib_test)

add_executable(${PROJECT_NAME})
include(sources.cmake)
target_include_directories(${PROJECT_NAME}
    PRIVATE
        $<TARGET_PROPERTY:greeting_lib,INCLUDE_DIRECTORIES>
)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
        greeting_lib
        CONAN_PKG::catch2
)

add_test(
    NAME ${PROJECT_NAME}
    COMMAND ${PROJECT_NAME}
)
