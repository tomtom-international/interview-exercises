 #define CATCH_CONFIG_MAIN
 #include "catch2/catch.hpp"
 
#include "Greeting.h"


TEST_CASE( "Positive Case","[greet]")
{
    std::string ecpectedStr = "hello";
    Greeting g;

    REQUIRE( ecpectedStr == g.greet() );
}