class MyBank:
    def __init__(self, accountNo, accountBalance, holder, holderBirth, currency):
        self.account_number = accountNo
        self.holder_name = holder
        self.holder_birth = holderBirth
        self.currency_sign = currency
        self.account_balance = accountBalance

    def deposit(self):
        amount = float(input("How much would you like to deposit: "))
        self.account_balance += amount
        print(f"{self.currency_sign}:{amount} money is deposited!")
        print(f"Account balance updated: {self.currency_sign}:{self.account_balance}")

    def withdraw(self):
        amount = float(input("How much would you like to withdraw: "))
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"{self.currency_sign}:{amount} money is withdrawn!")
            print(f"Updated account balance: {self.currency_sign}:{self.account_balance}")
        else:
            print(f"Insufficient funds on {self.account_number} Account!!")

# Create an instance of the MyBank class
bank = MyBank(accountNo="123456", holder="Testing", holderBirth="0000-00-00", accountBalance=2000, currency="Rs")
bank.deposit()
bank.withdraw()
