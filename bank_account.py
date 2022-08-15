class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Personal details")
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))

class Bank(User):
    def __init__(self, name, age,):
        super().__init__(name, age)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Account balance has been updated: {self.balance}$")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your account has been updated: {self.balance}")
        else:
            print("You have not got enough money to withdraw")
    def show_bank_account(self):
        self.show_details()
        print(f"Your bank account is: {self.balance}$")

