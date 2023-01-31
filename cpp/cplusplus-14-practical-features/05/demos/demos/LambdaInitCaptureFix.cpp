#include <iostream>
#include <memory>
using namespace std;
 
int main() {
  auto p = make_unique<int>(64);
  
  auto lambda = [ptr = move(p)](){ 
    cout << " Inside the lambda -- value = " << *ptr << '\n'; 
  };

  lambda(); 
}

