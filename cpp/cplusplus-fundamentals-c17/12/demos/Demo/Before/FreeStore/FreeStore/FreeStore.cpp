// FreeStore.cpp : Defines the entry point for the console application.
//

#include "Resource.h"
#include <string>
using std::string;

int main()
{
	{
		Resource localResource ("local");
		string localString = localResource.GetName();
	}
	Resource* pResource = new Resource("created with new");
	string newString = pResource->GetName();
	int j =3;
	delete pResource;
	string string3 = pResource->GetName();

	return 0;
}

