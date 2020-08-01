class Registerbankaccount():
    def __init__(self):
        self.uname=''
        self.pwd=''
        self.fname=''
        self.amt=''

    def register(self):
        self.fname = input("Enter your First Name: ")
        self.uname = input("Enter your Username: ")
        self.pwd = input("Enter your Password: ")
        print("To create account min amount is=5000\n")
        self.amt= int(input("Enter your amount: "))
        try:
            if self.amt >=5000:
                print("Now you can Login using your username and password")
                f =open('login1.txt' ,'a+')
                f.write(f'{self.fname}')
                f.write(" ")
                f.write(f'{self.uname}')
                f.write(" ")
                f.write(f'{self.pwd}')
                f.write(" ")
                f.write(f'{self.amt}')
                f.write(" ")
            elif self.amt <5000:
                print("You can not open account")
                print("Thank you for using Detroit United Bank Service")
        except (ValueError):
            print("\n Enter proper value in Amount")

    def login(self):
        uname = input("Enter your Username: ")
        pwd = input("Enter your Password: ")
        file = open("login1.txt","r")
        for lines in file:
            lines = lines.split()
            if uname == lines[1]:
                if pwd == lines[2]:
                    print("Login Successful")
                    return (f"Welcome {lines[0]} in your profile")
                else:
                    print("Sorry please check your username and password")
                    return ''
                
r= Registerbankaccount()
r.register()
r.login()

