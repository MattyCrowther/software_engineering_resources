#include "Person.h"

using namespace std;

Person::Person(string first,string last,
	int arbitrary) : firstname(first),lastname(last),
	arbitrarynumber(arbitrary)
{
}

Person::~Person()
{
}

string Person::GetName() const
{
	return firstname + " " + lastname;
}
