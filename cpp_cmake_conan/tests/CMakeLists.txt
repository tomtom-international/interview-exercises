cmake_minimum_required(VERSION 3.5)
project(greeting_test)


set(CMAKE_CXX_STANDARD 11)


######################################
#include(${PROJECT_SOURCE_DIR}/build/conanbuildinfo.cmake)
#conan_basic_setup()
find_package(Catch2)
include(ParseAndAddCatchTests)
include(Catch)
add_executable(greeting_test greeting_test.cpp)
target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
#########################################
enable_testing()
add_test(greet greeting_test)

target_link_libraries(greeting_test
       greeting_lib
       ${CONAN_LIBS}
)
catch_discover_tests(${PROJECT_NAME})