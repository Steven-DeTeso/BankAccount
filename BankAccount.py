# Start of assignment: Write a new BankAccount class

class BankAccount: #created a class called "BankAccount"
    account = [] # this is going to be used for the @class method, it is a variable attached to this BankAccount class
    balance = 0  # these are attributes that belong to this class only
    int_rate = 0.00

    def __init__(self, int_rate, balance): # here is where i can initiate instances of the class
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account.append(self) #this adds to the list account variable when a new instance gets created
    
    def deposit(self, amount): 
        self.balance = self.balance + amount
        print(f"You deposited {amount}")
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance = self.balance - amount
            print(f"You withdrew {amount}")
        else: 
            print("Insufficient funds: Charging a $5 fee") 
            self.balance = self.balance - 5 
        return self
    
    def display_account_info(self):
        print("You're balance is", str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        print(f"You're interest is {self.int_rate}")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.account:
            account.display_account_info()


Steven = BankAccount(0.05, 1000) # initializing an instance of Bank Account for Steven 

Maggie = BankAccount(0.10, 500)
Honey = BankAccount(0.025, 2000)

# print(Steven.display_account_info()) #checking intial account info
# print(Steven.deposit(5000)) #this is to check that the deposit methor works
# print(Steven.display_account_info()) #output here confirms deposit worked

Steven.deposit(100)
Steven.deposit(200)
Steven.deposit(250)

Steven.display_account_info() # invoking the deposit method to make sure that all the deposits are accuring correctly into the balance. It's working, output is now 1550

Steven.withdraw(150)
Steven.display_account_info() #invoking the withdraw method to see if it is executing correctly. On the ouput it is. 
Steven.yield_interest() # this line invokes the yield interest method onto the Steven instance 
Steven.display_account_info() # this line displays the output of the yielded interest. 

# this line below is "chaining" (displaying the account's info all in one line of code)
Steven.deposit(10).deposit(20).deposit(20).withdraw(50).yield_interest().display_account_info() # IMPORTANT - i learned here that you need to have a "return self" statement under all the methods you're chaining together. 

Maggie.deposit(100).deposit(200).withdraw(10).withdraw(20).withdraw(10).withdraw(5).yield_interest().display_account_info()

BankAccount.print_all_accounts() # this calls the class and displays all the account balances that correspond to all the different instances of the Bank accounts that were created (ie. Steven, Maggie and Honey)