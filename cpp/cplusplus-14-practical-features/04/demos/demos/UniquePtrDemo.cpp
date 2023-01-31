#include <iostream>
#include <memory>     // For std::unique_ptr and std::make_unique
using namespace std;

class X {
 public:
   X() {
     cout << " X constructor \n";
   }

   ~X() {
     cout << " X destructor \n";
   }

   void SayHi() {
     cout << " X says hi! :) \n";
   }

 private:
   // Some data members ...
   int m1{};
   double m2{3.14};
};

int main() {
  auto pX = make_unique<X>();
  pX->SayHi();
}

