#Step 1: Define the class
class Account2 :
        #Step 1.1: Initialize the account with the specified values
        def __init__(self, owner, account, initial) :
                self.__acct_name = owner
                self.__acct_number = account
                self.__balance = initial
        #Step 1.2: Define a method to provide a one-line description of the account
        def __str__(self) :
                return "{:d}{:>20s}{:>10.2f}".format(self.__acct_number, self.__acct_name, self.__balance)
        #Step 1.3: Define a method to perform the deposit transaction
        def deposit(self, amount) :
                if (amount > 0) :
                        self.__balance = self.__balance + amount
                return self.__balance
        #Step 1.4: Define a method to perform a withdraw transaction
        def withdraw(self, amount, fee) :
                if (amount > 0 and fee >= 0 and amount+fee < self.__balance) :
                        self.__balance = self.__balance - amount - fee
                return self.__balance
        #Step 1.5: Define a method to add interest to the account
        def add_interest(self) :
                self.__balance += (self.__balance * 0.035)
                return self.__balance
        #Step 1.6: Define the methods to get the  state of the account
        def get_name(self) :
                return self.__acct_name
        def get_balance(self) :
                return self.__balance
        def get_acct_number(self) :
                return self.__acct_number
#Step 2: Test the class
acct1 = Account2("Tina Murphy", 72354, 25.59)
acct2 = Account2("Angelica Adams", 69713, 500.00)
acct3 = Account2("Edward Demsey", 93757, 769.32)
print(acct1)
print(acct2)
print(acct3)
