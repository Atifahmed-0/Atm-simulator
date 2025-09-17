balance = 100000
pin = 1234

Pass = int(input("ENTER YOUR PIN: "))

if Pass != pin:
    print("❌ INVALID PIN")
else:
    while True:
        print("\n🏧 ATM Menu:")
        print("1. 💰 Check Balance")
        print("2. ➕ Deposit")
        print("3. ➖ Withdraw")
        print("4. 🚪 Exit")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            print(f"💳 YOUR BALANCE IS: PKR {balance}")

        elif choice == 2:
            amount = int(input("ENTER AMOUNT TO DEPOSIT: "))
            balance += amount
            print("✅ AMOUNT DEPOSITED SUCCESSFULLY")

        elif choice == 3:
            amount = int(input("ENTER AMOUNT TO WITHDRAW: "))
            if amount <= balance:
                balance -= amount
                print("✅ AMOUNT WITHDRAWN SUCCESSFULLY")
            else:
                print("❌ INSUFFICIENT BALANCE")

        elif choice == 4:
            print("👋 THANK YOU FOR USING THE ATM!")
            break

        else:
            print("❌ INVALID OPTION, PLEASE TRY AGAIN")
