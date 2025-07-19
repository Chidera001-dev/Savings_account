balance = 0#starting balance
name = input("Enter your name: ")

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Choose an option(1-4): ")
    match choice:
        case "1":
            print (f"Your current balance is: ${balance:.2f}")
        case "2":
            amount = float(input("Enter amount to deposit: "))
            if amount < 0:
                print("Amount must be more than zero.")
            else:
                balance += amount
                print(f"You deposited ${amount}. New balance is : ${balance}")
        case "3":
            amount_withdrew = float(input("Enter amount to withdraw: "))
            if amount_withdrew > balance :
                print("Insufficient funds!!!")
            else:
                balance -= amount_withdrew
                print(f"Your withdrew ${amount_withdrew}. New balance is ${balance}")
        case "4":
            print(f"Thank you for banking with us, {name}!")
            break
        case _ :
            print("invalid choice. Pleasetry again. Enter a number between 1-4")

                



    