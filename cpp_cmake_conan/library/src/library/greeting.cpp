#include <library/greeting.h>

namespace greeting
{

auto Greeting::greet() -> std::string
{
    return std::string{"hello"};
}

}
