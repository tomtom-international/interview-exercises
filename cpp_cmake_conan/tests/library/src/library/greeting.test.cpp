#define CATCH_CONFIG_MAIN

#include <library/greeting.h>

#include <catch2/catch.hpp>

class GreetingTest
{
protected:
    greeting::Greeting uut;
};

TEST_CASE_METHOD(GreetingTest, 
    "Should return \"hello\"",
    "[acceptance]")
{
    using Catch::Equals;

    REQUIRE_THAT(uut.greet(), Equals("hello"));
}
