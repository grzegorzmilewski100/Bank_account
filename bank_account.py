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
        print(f"Your bank account is: {self.balance}$")

johan = Bank("Johan", 25)
johan.deposit(250)
johan.withdraw(350)
johan.show_bank_account()
