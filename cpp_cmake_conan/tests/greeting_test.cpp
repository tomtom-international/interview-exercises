#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include "greeting.h"

TEST_CASE("Greeting member function", "[Greeting]")
{
    Greeting obj;

    SECTION("greet member function test") {
        REQUIRE( obj.greet() == "hello");
    }
}
