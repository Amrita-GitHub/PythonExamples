def divide(x,y):
    try:
        result = x//y  #result after truncating
        print("after execution..1")

    except ZeroDivisionError:
        print("division by zero")
    else:
        print("Your answer is..", result)

    finally:
        print("Executing finally block..!!!")


#ZeroDivisionError: integer division or modulo by zero
divide(3,10)