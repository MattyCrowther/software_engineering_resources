#include <iostream>
#include <memory>
using namespace std;
 
int main() {
  auto p = make_unique<int>(64);
  
  auto lambda = [](){ 
    cout << " Inside the lambda -- value = " << *p << '\n'; 
  };

  lambda(); 
}

