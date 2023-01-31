#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

void print(milliseconds ms) {
  cout << ms.count() << "ms \n";
}

int main() {
  auto x = 2s;
  cout << " x = 2s :    "; print(x);

  auto y = 150ms;
  cout << " y = 150ms : "; print(y);

  auto z = x + y;
  cout << " z = x + y : "; print(z);

  constexpr auto timeLimit = 3s;
  cout << "\n Time limit is "; print(timeLimit);
  if (z < timeLimit) {
    cout << " All right! \n";
  } else {
    cout << " Out of time! \n";
  }
}

