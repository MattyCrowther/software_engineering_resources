// GuessTheNumber.cpp : a simple console game
//
#include <iostream>

using namespace std;

int main()
{
	int answer = 3;
	int guess;
	bool notguessed = true;
	while (notguessed)
	{
		cout << "Guess my number: ";
		cin >> guess;
		if (guess == answer)
		{
			cout << "Yes!" << endl;
			notguessed = false;
		}
		if (guess < answer)
		{
			cout << "Too low..." << endl;
		}
		if (guess > answer)
		{
			cout << "Too high..." << endl;
		}
	}

	return 0;
}

