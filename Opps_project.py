
#Bank operation using oop
class Bank:
    bank_name = "Indian National Bank"
    branch = "New Delhi,India"

    def __init__(self, name, pan, address_person):
        self.name = name
        self.pan = pan
        self.address_person = address_person
class Account(Bank):
    #Account creation
    def __init__(self, name, pan, address_person, user_name, password, account_number, balance=0):
        super().__init__(name, pan, address_person)
        self.user_name = user_name
        self.password = password
        self.account_number = account_number
        self.balance = balance
        print(f"Hello {name} congrats! your account created successfully")
     #Account login
    def login(self, entered_user_name, entered_password):
        return entered_user_name == self.user_name and entered_password == self.password

    #Amount Deposite
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Deposited successfully,Your current account balance is:\t{self.balance}")
    #Amount Withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} Withdraw successfully,Your current account balance is:\t{self.balance}.If not done,fwd this SMS to 92589325000 or call 18000112545")
        else:
            print("Insufficient Balance...")
    #Display Account balance
    def account_balance(self):
        print(f"Your Account Balance is {self.balance}")
print(f"Welcome to {Bank.bank_name}, {Bank.branch}")
name=input("Enter your Name:\t")
pan=input("Enter your PAN:\t")
address_person=input("Enter your Address:\t")
user_name=input("Enter your Username:\t")
password=input("Enter your Password:\t")
account_number=input("Enter your Account Number:\t")

account1=Account(name,pan,address_person,user_name,password,account_number,balance=0)
entered_user_name = input("Enter your Username:\t")
entered_password = (input("Enter your password:\t"))

if account1.login(entered_user_name,entered_password):
    print("Login successful.")
else:
    print("Login failed. Incorrect Password or Username .")
    reset_username_password = input("Do you want to try again ?:\t")
    if reset_username_password == "yes":
        entered_user_name = input("Enter your Username:\t")
        entered_password = (input("Enter your password:\t"))
        account1.login(entered_user_name, entered_password)
        print("Login successful.")
    else:
        print("Thanks for using Indian National Bank.... ")
        exit()

while True:

    print("Please select any option!\n1.Deposited\n2.Withdraw\n3.Account Balance\n4.logout")
    option=int(input(""))
    if option==1:
        ammount=float(input("Enter Deposited Amount:\t"))
        account1.deposit(ammount)
    elif option==2:
        ammount = float(input("Enter Withdraw Amount:\t"))
        account1.withdraw(ammount)
    elif option==3:
        account1.account_balance()
    elif option==4:
        print("Thanks for using Indian National Bank.... ")
        break
    else:
        print("Invalid option please select a valid option")




