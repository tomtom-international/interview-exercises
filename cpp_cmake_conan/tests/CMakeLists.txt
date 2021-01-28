cmake_minimum_required(VERSION 3.5)
project(greeting_test)


set(CMAKE_CXX_STANDARD 11)
add_subdirectory(catch2)



# enable CTest testing
enable_testing()
# Add a testing executable
add_executable(unit_tests greeting_test.cpp)

target_link_libraries(unit_tests
    Catch2::Test
    greeting_lib
)

add_test(test_all unit_tests)