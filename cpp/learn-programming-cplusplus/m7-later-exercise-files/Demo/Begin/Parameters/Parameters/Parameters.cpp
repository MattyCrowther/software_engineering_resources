#include "Transaction.h"
#include <iostream>
using namespace std;

void tryToChangeTransaction(Transaction t)
{
	t.DoubleAmount();
}

void changeTransaction(Transaction& t)
{
	t.DoubleAmount();
}



int main()
{
	Transaction deposit(50, "Deposit");
	cout << "Original: " << deposit.Report() << endl;
	tryToChangeTransaction(deposit);
	cout << "After pass by value: " <<  deposit.Report() << endl;
	changeTransaction(deposit);
	cout << "After pass by reference: " <<  deposit.Report() << endl;


	return 0;
}

