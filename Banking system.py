class Atm:
    def __init__(self):
        self.__pin=""
        self.__balance=0
        self.menu()
    
    def menu(self):
        user_input = input("""
        Hello,how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to Exit
    """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        elif user_input=="5":
            print("Exit")
        else:
            print("invalid option")
    
    def create_pin(self):
        self.__pin=int(input("Enter your pin: "))
        print("pin set succesfully")
        
    def deposit(self):
        temp=int(input("enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            self.__balance=self.__balance+amount
            print("Deposit succesful")
        else:
            print("Invalid pin")
            
    def withdraw(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            amount=int(input("Enter the amount: "))
            if amount<=self.balance :
                    self.__balance=self.__balance-amount
                    print("Operation Succesful")
            else:
                    print("Insufficient balance")
                    
    def check_balance(self):
        temp=int(input("Enter your pin: "))
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin")
