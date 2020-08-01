class Error(Exception):
    pass
class ValueError(Error):
    pass
class InsufficientBalanceError(Error):
    pass

class Bankaccount(): 
    def __init__(self):
        file = open("login1.txt","r")
        for lines in file:
            lines = lines.split()
            self.bal=int(lines[3])
        minbal=0
    def withdraw(self):
        minbal=5000
        while True:
            try:
                amt = int(input("Enter amount to withdraw: "))
                balance=self.bal-minbal
                if  balance >= amt:
                    self.bal = self.bal-amt                     
                    print("Your Withdraw Amount is:", amt)
                    print(f"Now your Balance is: {self.bal}")
                    f =open('login1.txt' ,'a+')
                    for lines in file:
                        lines = lines.split()
                        lines[3]=self.bal
                    break
                elif balance < amt:
                    raise InsufficientBalanceError;
            except InsufficientBalanceError:
                print("\nInsufficient Balance in your account-Minimum amount required in account is 5000")
            except (Exception, ValueError):
                print("\n Enter proper Value")
    def Deposit(self):
        dep=int(input("Enter amount which you want to deposit: "))
        self.bal = self.bal +dep
        f =open('login1.txt' ,'a+')
        for lines in f:
                lines = lines.split()
                lines[3]=self.bal
        print(f"Now your Balance is: {self.bal}")
    def changename(self):
        name: input("Enter your Changed Name: ")
        f =open('login1.txt' ,'a+')
        for lines in f:
                lines = lines.split()
                lines[0]=name
    def balance(self):
        balance=50000
        if self.bal!=0:
            print(f"Your Account Balance is {self.bal}")
        else:
            print(f"Your last transaction is:\n you withdraw {amt} Rs")
            print(f"Your Account Balance is {balance}")

