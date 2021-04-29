project(greeting_app)

add_executable(greeting_app main.cpp)
target_include_directories(greeting_app PUBLIC ${CMAKE_SOURCE_DIR}/library)
target_link_libraries(greeting_app PRIVATE greeting_lib)
