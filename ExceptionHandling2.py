a=[1,2,3]
try:
    print("Element at index .", a[5])

    #name="hello"
    name1=str("dinesh") #NameError: name 'name' is not defined

    print(name, ' ' , name1)

#IndexError: list index out of range
except (IndexError, NameError):   #multicatchblock
        print("Encountered either of these errors in code..!!!")
        print("Invalid index..must be in the range od 0-3 only")

        print("var name not found in scope")

