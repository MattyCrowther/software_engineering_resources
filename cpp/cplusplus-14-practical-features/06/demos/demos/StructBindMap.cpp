#include <iostream> // for std::cout
#include <map>      // for std::map
#include <string>   // for std::string
using namespace std;

int main() {
  map<string, string> italianDictionary{
    {"casa",   "home"},
    {"gatto",  "cat"},
    {"tavolo", "table"}

    // ...
  };

  auto [pos, success] = italianDictionary.insert({"sedia", "chair"});
  if (success) {
    cout << " Insertion OK.\n\n";
  }

  for (const auto& [italian, english] : italianDictionary) {
    cout << ' ' << italian << ": " << english << '\n';
  }
}

