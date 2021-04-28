project(greeting_test)

add_executable(greeting_test greeting_test.cpp)

target_link_libraries(greeting_test greeting_lib CONAN_PKG::catch2)
target_include_directories(greeting_test PRIVATE ${CONAN_INCLUDE_DIRS}/catch2 ${CMAKE_SOURCE_DIR}/library)

add_test(NAME greeting_test COMMAND greeting_test)
