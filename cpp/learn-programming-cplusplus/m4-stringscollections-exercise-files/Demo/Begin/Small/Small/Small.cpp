#include <iostream>
#include <string>

using namespace std;

int main()
{
    string name;
    cout << "who are you? ";
    cin >> name;
    string greeting = "Hello, " + name;
    if (name == "Kate")
    {
        greeting += ", I know you!";
    }
    cout << greeting << endl;
    return 0;
}

