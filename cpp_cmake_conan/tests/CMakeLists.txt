project(greeting_test)

add_executable(greeting_test greeting_test.cpp)

Include(FetchContent)

FetchContent_Declare(
Catch2
GIT_REPOSITORY https://github.com/catchorg/Catch2.git
GIT_TAG        v2.13.1)

FetchContent_MakeAvailable(Catch2)

target_link_libraries(greeting_test greeting_lib Catch2::Catch2)
target_include_directories(greeting_test PRIVATE ${Catch2_SOURCE_DIR}/single_include/catch2 ${CMAKE_SOURCE_DIR}/library)

add_test(NAME greeting_test COMMAND greeting_test)
