#define CATCH_CONFIG_MAIN

#include "catch.hpp"
#include "greeting.h"

TEST_CASE("Test greeting return", "[greeting_test]")
{
  Greeting g;
  REQUIRE(g.greet() == "hello");
}
