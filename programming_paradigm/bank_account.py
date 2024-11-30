class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self,amount):
        if amount <= 0:
            print("deposit must a natural number")
        else: 
            self._account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and self._account_balance > amount:
            self._account_balance -= amount
            return True
        else:
            print ("Insufficient funds")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    

