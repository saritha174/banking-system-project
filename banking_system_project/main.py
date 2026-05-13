class BankAccount:

    def __init__(self, account_number, account_holder, balance=0):

        self.account_number = account_number
        self.account_holder = account_holder

        self.__balance = balance

        self.transaction_history = []
    

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        self.__balance += amount

        self.transaction_history.append(f"Deposited {amount}")

        print(f"{amount} deposited successfully")


    def show_balance(self):
        print(f"Current Balance: {self.__balance}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount > self.__balance:
            print("Insufficient balance")
            return
        self.__balance -= amount

        self.transaction_history.append(f"Withdrawn {amount}")

        print(f"{amount} withdrawn successfully")

    def show_transactions(self):

        print("\nTransaction History:")

        for transaction in self.transaction_history:
            print(transaction)


acc1 = BankAccount(101, "Alice", 5000)



print(acc1.account_holder)
print(acc1.account_number)
acc1.deposit(1000)
acc1.show_balance()
acc1.withdraw(3000)
acc1.show_balance()
acc1.show_transactions()

