class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        # a dictionary referenced by self.accounts that holds all the instances of BankAccount for a User
        self.accounts = {
            "Checkings": BankAccount(int_rate=0.02, balance=0),
            "Savings" : BankAccount(int_rate=0.02, balance=0)
        }


    def make_deposit(self, amount, account_name="Checkings"):
        """ make a deposit into a User's specified bank account and if no account is named,
            the default is the Checkings account """
        self.accounts[account_name].deposit(amount)
        return self

    def make_withdrawal(self, amount, account_name="Checkings"):
        """ make a withdrawal from a User's specified bank account and if no account is named,
            the default is the Checkings account """
        self.accounts[account_name].withdraw(amount)
        return self

    def display_user_balance(self):
        """ Display the all of the User's BankAccount instances with the correct balance """
        for key, val in self.accounts.items():
            print(f"User: {self.name}, {key} Balance: {val.balance}")
        return self

    def transfer_money(self, amount, other_user):
        """ transfer money out from the self User into another User's account """
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self



class BankAccount:
    # don't forget to add some default values for these parameters!
    # a class attribute that is a list to hold all BankAccount instances
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        """ Deposit a given amount into an account """
        self.balance += amount
        return self

    def withdraw(self, amount):
        """ Withdraw a given amount into an account if possible"""
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        """ print the accounts info """
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        """ yield the intrest on the account if the account's balance is positive """
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self

    @classmethod
    def all_balances(cls):
        """ a class method to print the information of all the accounts """
        for account in cls.all_accounts:
            account.display_account_info()


# initialize user 1
user_1 = User("John", "john@email.com")
# make two deposits into user one's accounts and print their info
user_1.make_deposit(50).make_deposit(25, "Savings").display_user_balance()


# initialize user 2
user_2 = User("Dave", "dave@email.com")
# make two deposits into user two's accounts and print their info
user_2.make_deposit(50).make_deposit(50, "Savings").display_user_balance()


#transfer money from user 2 to user 1
user_2.transfer_money(15, user_1)


# print the account info for both users
user_1.display_user_balance()
user_2.display_user_balance()
