import sys

class BankAccount:
    def __init__(self, name, id, pin, balance):
        self.name = name
        self.id = id
        self.pin = pin
        self.balance = balance

    def deposit(self, id, pin, amt):
        if isinstance(id, int) and isinstance(pin, int) and isinstance(amt, int):
            if self.id == id and self.pin == pin:
                self.balance += amt
                print(f"Deposited {amt} rupees into your bank account!")
            else:
                print("Incorrect ID or PIN entered. Try again!")
                sys.exit()
        else:
            print("Invalid Input. Try again!")
            sys.exit()

    def withdraw(self, id, pin, amt):
        if isinstance(id, int) and isinstance(amt, int) and isinstance(pin, int):
            if self.id == id and self.pin == pin:
                if amt <= self.balance:
                    self.balance -= amt
                    print(f"Withdrew {amt} rupees from your bank account!")
                else:
                    print("Insufficient funds. Try again!")
                    sys.exit()
            else:
                print("Incorrect ID or PIN entered. Try again!")
                sys.exit()
        else:
            print("Invalid Input. Try again!")
            sys.exit()

    def curr_balance(self):
        print(f"Available Funds: {self.curr_balance}!")
    
def main():
    customer1 = BankAccount("Sankar Addala", 21314254, 111, 100)
    customer1.deposit(21314254, 111, 100)
    print(customer1.curr_balance())
    customer1.withdraw(21314254, 111, 50)
    print(customer1.curr_balance())

if __name__ == "__main__":
    main()
