#include <vector>
#include <string>
#include "Transaction.h"

class Account
{ 
private:
	int balance;
	std::vector<Transaction> log;
	int limit;
public:
	Account();
	std::vector<std::string> Report() const;
	bool Deposit(int amt);
	bool Withdraw(int amt);
	int GetBalance() const {return balance;}
};

