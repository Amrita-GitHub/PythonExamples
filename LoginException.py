class LoginException(Exception):
    def __init__(self, message):
        self.message  =  message

    def __str__(self):
        return  self.message

class Login:


    name = input("Eneter user name")
    password = input("eneter password")

    if(name.__eq__(password)):
        print("Welcome..." ,name)
    else:
        try:
            raise LoginException("Invalid username/password..!!!")

        except LoginException as le:
            print("Eneter name & password again..!!!" )
            print("cause..", le.__cause__)
            print("message.." , le.message)


        finally:
            print("Thank You..!!!")


l = Login()