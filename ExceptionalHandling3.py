def accept():
    while(True):
        try:
            n = int(input("Eneter a number"))
            print("You eetered ..." , n)
        except ValueError:
            print("Not a valid number....Try again...!!!")


accept()
