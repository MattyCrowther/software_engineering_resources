
#include "Person.h"

using namespace std;

Person::Person(string first,string last,
	int arbitrary) : firstname(first),lastname(last),
	arbitrarynumber(arbitrary), pResource(nullptr)
{
}

Person::~Person()
{
}

string Person::GetName() const
{
	return firstname + " " + lastname;
}


void Person::AddResource()
{
	pResource=new Resource("Resource for " + GetName());
}
