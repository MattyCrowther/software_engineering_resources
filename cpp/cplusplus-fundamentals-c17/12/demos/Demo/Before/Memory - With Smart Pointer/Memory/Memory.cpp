// Memory.cpp : Defines the entry point for the console application.
//

#include "Person.h"
#include <string>
using std::string;


int main()
{
	{
		Person Kate("Kate", "Gregory", 345);
		Kate.AddResource();
		string s1 = Kate.GetResourceName();
		Kate.AddResource();
	}
	return 0;
}

