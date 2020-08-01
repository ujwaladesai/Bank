from transaction import Bankaccount
from register_bank import Registerbankaccount

print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("*****Detroit United Bank******")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
print("*****Welcome in Bank*****")
a= Bankaccount()
b=Registerbankaccount()

class banking:
    def __init__(self):
        pass
    def bank(self):
            print("Are you an existing user of Bank: Y -Yes and N-No")
            c=input("Enter your answer : ")
            if c=='Y':
                s=b.login()
                while True:
                    if s!='':
                        print("Now your Banking profile is visible to you")
                        print(s)
                        print("Your Options for Banking are :\n1- Deposit Money\n2- Withdraw Money\n3- Change Name\n4- Balance \n5- Exit")
                        ch1=input("Enter your choice : ")
                        if ch1 == '1':
                            a.Deposit()
                        elif ch1== '2':
                            a.withdraw()
                        elif ch1== '3':
                            a.changename()
                        elif ch1== '4':
                            a.balance()
                        else :
                            print("Thank you for using Detroit United Bank Banking")
                            break
                    else:
                        print("Thank you for using Detroit United Bank Netbanking")
                    co=input("Do you want to continue:\n1.Yes\n2.No : ")
                    if co=='1':
                        continue
                    else:
                        print("Thank you for using Detroit United Bank Banking")
                        break
            else:
                print("Register your Banking account with Bank")
                b.register()
                s=b.login()
                while True:
                        if s!='':
                            print("Now your Banking profile is visible to you")
                            print(s)
                            print("Your Options for Banking are :\n1- Deposit Money\n2- Withdraw Money\n3- Change Name\n4- Balance \n5- Exit")
                            ch2=input("Enter your choice : ")
                            if ch2 == '1':
                                a.Deposit()
                            elif ch2== '2':
                                a.withdraw()
                            elif ch2== '3':
                                a.changename()
                            elif ch2== '4':
                                a.balance()
                            else :
                                print("Thank you for using Detroit United Bank Banking")
                                break
                            co=input("Do you want to continue:\n1.Yes\n2.No : ")
                            if co=='1':
                                continue
                            else:
                                print("Thank you for using Detroit United Bank Banking")
                                break
n=banking()
n.bank()
