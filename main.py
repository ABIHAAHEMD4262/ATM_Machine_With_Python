class ATM:
    def __init__(self):
        # Initialize with a default balance and PIN
        self.balance = 1000
        self.pin = "1234"
        self.pin_verified = False

    def check_pin(self, input_pin):
        """Verify if the entered PIN is correct"""
        if input_pin == self.pin:
            self.pin_verified = True
            print("PIN verified successfully.\n")
        else:
            self.pin_verified = False
            print("Incorrect PIN. Please try again.\n")

    def check_balance(self):
        """Display the current balance if PIN is verified"""
        if self.pin_verified:
            print(f"Your current balance is: ₹{self.balance}\n")
        else:
            print("Access denied. Please verify your PIN first.\n")

    def deposit(self, amount):
        """Deposit a positive amount if PIN is verified"""
        if not self.pin_verified:
            print("Access denied. Please verify your PIN first.\n")
            return

        if amount <= 0:
            print("Invalid amount. Please enter a positive value.\n")
        else:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated balance: ₹{self.balance}\n")

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance and PIN is verified"""
        if not self.pin_verified:
            print("Access denied. Please verify your PIN first.\n")
            return

        if amount <= 0:
            print("Invalid amount. Please enter a positive value.\n")
        elif amount > self.balance:
            print("Insufficient balance.\n")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining balance: ₹{self.balance}\n")

    def exit(self):
        """Exit the ATM session"""
        print("Thank you for using the ATM. Goodbye!")
        exit()


# --------------------
# Menu-Based Interface
# --------------------

def atm_menu():
    atm = ATM()
    
    print("Welcome to ATM")
    user_pin = input("Please enter your PIN: ")
    atm.check_pin(user_pin)

    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $ "))
                atm.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
        elif choice == "4":
            atm.exit()
        else:
            print("Invalid choice. Please select between 1-4.\n")


# Run the ATM system
atm_menu()
