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

	int l = greeting.length();
	cout << "\"" + greeting + "\" is " 
		<< l << " characters long." << endl;
	auto space = greeting.find(' ');
	string beginning = greeting.substr(space + 1);
	cout << beginning << endl;;
	if (beginning == name)
	{
		cout << "expected result." << endl;
	}
    return 0;
}

