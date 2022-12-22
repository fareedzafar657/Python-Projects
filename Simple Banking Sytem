class User:  #parent class
    def __init__(self, name: str, age:int, gender:str):      #initializer
        self.name = name
        self.age = age
        self.gender = gender

    def user_details(self):
        print("User details: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Bank(User):       #child class
    def __init__(self, name: str, age:int, gender:str):     #setting the allowed data type
        super().__init__(name, age, gender)       #super to import the parent class initializer atrributes
        self.balance = 0        #value is assigned inside the initializer

    def get_deposit(self,amount:int):   #Depositing money in self.balance
        self.amount = amount    #turning to class self object
        self.balance = self.balance + self.amount
        print(f"Account balance: ${self.balance}")

    def withdraw(self,amount: int):     #windrawing the money from self.balance
        self.amount = amount
        if self.amount <= self.balance and self.amount >= 0:
            self.balance = self.balance - self.amount
        else:
            print("Insufficient Balance")

        print(f"Account balance: ${self.balance}")

    def view_balance(self):
        self.user_details()
        print(f"Balance: ${self.balance}")

###################
# fareed = Bank("Fareed", 21, "Male")
# fareed.get_deposit(20000)
# fareed.view_balance()
#
# fareed.withdraw(200)
