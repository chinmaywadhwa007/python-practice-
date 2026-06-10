# banking system with the help of oops in python

class bankAccount:

    def __init__(self, acc_number, Holder_name, balance=0):
        self.acc_number = acc_number
        self.Holder_name = Holder_name
        self.balance = balance


def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print(f"deposited ₹{amount}.new balance:₹{self.balance}")

    else:
        print("deposit amount must be in postive!!!")


def withdraw(self, amount):
    if amount > self.balance:
        print("insufficient balance !!")
    elif amount <= 0:
        print("withdrowal ammount must be positive !!")

    else:
        self.balance -= amount  # self.balance=self.balance-amount
        print(f"Withdrew ₹{amount}. Remaining Balance: ₹{self.balance}")


def check_bal(self):
    print(f"amount holder : {self.Holder_name}")
    print(f"account_Num : {self.acc_number}")
    print(f"balance will be  : {self.balance}")


def main():
    print("===welcome to the bank management system ===")
    acc_no = input("enter your bank number:-")
    name = input("enter your name :-")
    amount = bankAccount(acc_no, name)

    while True:
        print("\n---menu---")
        print("1.deposit money")
        print("2.withdraw money")
        print("3.check bal")
        print("4.exit")

        choice = input("enter choice:")
        if choice == '1':
            amount = float(input("enter amount to deposit :"))
            amount.deposit(amount)
        elif choice == '2':
            amount = float(input("enter amount to withdraw :"))
            amount.withdraw(amount)
        elif choice == '3':
            amount.check_bal()

        elif choice == '4':
            print("thankyou for using the bank acc system !!!")
            break
        else:
            print("nikkal lodo")


main()
