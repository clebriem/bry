class bank:
    def __init__(self):
        self.balance=0
        self.run=True  
    def createaccount(self):
        
        self.accno=input("input account number\n")
        self.name=input("input account name\n")
        self.branch=input("input bank branch\n")
    
        print("account successfully created")
    def deposit(self):
        self.deposit=int(input("input amount to deposit\n"))
        self.balance+=self.deposit
    def withdraw(self):
        self.withdraw=input("input amount to withdraw\n")
        if self.balance>200:
            print("enter amount to withdraw\n")
        else:
            print ("withdrawal unsuccessful due to insufficient funds\n")
        self.balance-=self.withdraw
    def checkbalance(self):
        print(self.balance)
    def exit(self):
        input("press any key to exit")
        self.run=False
b=bank()

while b.run:
    print("**************")
    print("WELCOME TO OUR BANK")
    print("**************")
    print("1.create account")
    print("2.deposit money")
    print("3.withdraw")
    print("4.check balance")
    print("5.exit")
    action = input("select an action")
    if action=="1":
        b.createaccount()
    elif action=="2":
        b.deposit()

    elif action=="3":
        b.withdraw()
    elif action=="4":
        b.checkbalance()
    elif action=="5":
        b.exit()
    else:
        input("invalid option")
    if b.run==False:
        break

        
        self.withdraw=withdraw
        self.checkbalance=balance
        self.exit=exit
