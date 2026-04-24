import operations

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", operations.check_balance())

    elif choice == "2":
        amt = int(input("Enter amount: "))
        result = operations.deposit(amt)
        print(result)

    elif choice == "3":
        amt = int(input("Enter amount: "))
        result = operations.withdraw(amt)
        print(result)

    elif choice == "4":
        t = operations.show_transactions()
        if len(t) == 0:
            print("No record")
        else:
            for i in t:
                print(i)

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Wrong choice")