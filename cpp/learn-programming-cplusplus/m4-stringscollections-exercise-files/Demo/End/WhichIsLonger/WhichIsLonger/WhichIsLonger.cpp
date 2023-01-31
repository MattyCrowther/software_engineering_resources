#include <iostream>
#include <string>

using namespace std;

int main()
{
	string word1;
	string word2;

	cout << "Enter a phrase ";
//	cin >> word1;
	getline(cin,word1);

	cout << "Enter another phrase ";
//	cin >> word2;
	getline(cin,word2);

	if (word1.length() == word2.length())
	{
		cout << "They are the same length." << endl;
	}

	if (word1.length() > word2.length())
	{
		cout << "The first word is longer." << endl;
	}

	if (word1.length() < word2.length())
	{
		cout << "The second word is longer." << endl;
	}


	return 0;
}

