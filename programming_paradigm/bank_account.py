class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount <= 0:
            print("deposit must a natural number")
        else: 
            self.account_balance += amount

    def withdrawal(self, amount):
        if amount <= 0:
            print("The amount being withdrawn must be a natural number.")
            return False
        if amount < self.account_balance:
            self.account_balance -=amount
            return True
        else:
            print ("Insufficient funds")

    def display_balance(self):
        print(f"Current balance:${self.account_balance:.2f}")
    

