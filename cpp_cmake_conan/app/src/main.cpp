#include <library/greeting.h>

#include <iostream>

int main(int /*argc*/, char **/*argv*/)
{
  greeting::Greeting g;
  std::cout << g.greet() << std::endl;
  return 0;
}
