#include <iostream>
#include "Functions.h"

using namespace std;

int main()
{
	auto a = add(3,4);
	cout << "3 + 4 is " << a;
	double b = add(1.2,3.4);
	cout << endl;
	cout << "1.2 + 3.4 is " << b;

	cout << endl;
	auto c = add(1.1,2.2,3.3);
	cout << "1.1 + 2.2 + 3.3 is " << c;

	add(0,0);
	add(0,0,0);

	if (test(true))
	{
		cout << "true passes the test" << endl;
	}
	if (test(3.2))
	{
		cout << "3.2 passes the test" << endl;
	}

	//if (test(3))
	//{
	//	cout << "3 passes the test" << endl;
	//}

	return 0;
}

