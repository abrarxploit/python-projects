class BankAccount:
    def __init__(self):
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount:.2f}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount:.2f}")
            
    def check_balance(self):
        print(f"Balance: ₹{self.balance:.2f}")

def main():
    account = BankAccount()
    print("=== BANK ACCOUNT MANAGER ===")
    
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Choose: ")
        
        if choice == '1':
            try:
                amount = float(input("Amount: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount")
        elif choice == '2':
            try:
                amount = float(input("Amount: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount")
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()