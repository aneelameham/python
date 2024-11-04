class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, deposit):
        self.accounts[name] = deposit

    def deposit_money(self, name, deposit):
        self.accounts[name] = self.accounts[name] + deposit

    def view_account(self, name):
        balance = self.accounts[name]
        return balance

    def run(self):
        while True:
            print("\n1. Create account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = float(input("Enter choice (1, 2, 3, 4): "))

            if choice == 1:
                name = input("Name of the account holder: ")
                deposit = float(input("initial deposit: "))
                bank_system.create_account(name, deposit)
            elif choice == 2:
                name = input("Name of the account holder: ")
                if name in self.accounts:
                    deposit = float(input("initial deposit: "))
                    bank_system.deposit_money(name, deposit)
                else:
                    print("no such account")
            elif choice == 3:
                print(self.accounts)
                name = input("Name of the account holder: ")
                balance = bank_system.view_account(name)
                print(f"Balance in the account is {balance}")
            elif choice == 4:
                exit()


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()