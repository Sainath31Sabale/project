# ATM Machine Software using Python Programming

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    
    def check_balance(self):
        print(f"\nYour current balance is: ₹{self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n₹{amount} has been deposited. New balance is ₹{self.balance}")
        else:
            print("\nInvalid deposit amount")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\n₹{amount} has been withdrawn. New balance is ₹{self.balance}")
        else:
            print("\nInvalid withdrawal amount or insufficient funds")

def atm_menu():
    print("\n=== Welcome to the ATM ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    atm = ATM(1000)  # Initial balance ₹1000
    
    while True:
        atm_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            atm.check_balance()
        
        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            atm.deposit(amount)
        
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            atm.withdraw(amount)
        
        elif choice == '4':
            print("\nThank you for using the ATM!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
