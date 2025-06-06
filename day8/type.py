import acc
print("Welcome to SBI Bank")
while True:
    try:
        print("1.accouunt type of enter the number:")
        print("2.Savingsaccount:")
        print("3.currentaccount:")
        print("4.Exist")
        choice = int(input("enter choice:"))
        
        if choice == 1:
            manager = acc.Manager()
            manager = 
        elif choice == 2:
            acc.deposit()
        elif choice == 3:
            acc.deposit()
        else:
            print("thank you")
            break
        
    except Exception as error:
        print("Error occured")
    finally:
        print("Thank you for choosing SBI Bank")
        