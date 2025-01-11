# ATM Application

# Account information will be stored. (dict)
# Define functions: menu, withdrawMoney, checkBalance, depositMoney.
# If the requested amount exceeds the account balance, ask if the extra account should be used.

accounts = [
    {
        "name": "Bilal Sevinc",
        "accountNo": "12345",
        "balance": 20000,
        "extraAccount": 5000,
        "username": "bilalsevinc",
        "password": "1234"
    },
    {
        "name": "Yunus Sevinc",
        "accountNo": "12345",
        "balance": 30000,
        "extraAccount": 10000,
        "username": "yunussevinc",
        "password": "1234"
    }
]

def menu(account):
    print("\n")
    print(f"Hello, {account['name']}")
    print("1- Check Balance")
    print("2- Withdraw Money")
    print("3- Deposit Money")

    action = input("Choose an action: ")

    if action == "1":
        checkBalance(account)
    elif action == "2":
        withdrawMoney(account)
    elif action == "3":
        depositMoney(account)
    else:
        print("Invalid selection")

    menu(account)

def depositMoney(account):
    amount = float(input("Enter the amount to deposit: "))
    account["balance"] += amount
    print(f"{amount} has been deposited into your account.")
    checkBalance(account)

def checkBalance(account):
    print(f"Balance: {account['balance']}")
    print(f"Extra Balance: {account['extraAccount']}")

def withdrawMoney(account):
    amount = float(input("Enter the amount to withdraw: "))

    if account["balance"] >= amount:
        account["balance"] -= amount
        print("You can take your money.")
    else:
        total = account["balance"] + account["extraAccount"]

        if total >= amount:
            useExtraAccount = input("Do you want to use the extra account? (y/n): ")

            if useExtraAccount == "y":
                amountToUse = amount - account["balance"]
                account["balance"] = 0
                account["extraAccount"] -= amountToUse
                print("You can take your money.")
            else:
                print("Insufficient balance.")
        else:
            print("Insufficient balance.")

def login():
    username = input("Username: ")
    password = input("Password: ")

    isLoggedIn = False

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            isLoggedIn = True
            menu(account)
            break

    if not isLoggedIn:
        print("Invalid username or password")

login()

# Output:

"""

Username: bilalsevinc
Password: 1234


Hello, Bilal Sevinc
1- Check Balance
2- Withdraw Money
3- Deposit Money
Choose an action: 1
Balance: 20000
Extra Balance: 5000


Hello, Bilal Sevinc
1- Check Balance
2- Withdraw Money
3- Deposit Money
Choose an action: 2
Enter the amount to withdraw: 100
You can take your money.


Hello, Bilal Sevinc
1- Check Balance
2- Withdraw Money
3- Deposit Money
Choose an action: 3
Enter the amount to deposit: 200
200.0 has been deposited into your account.
Balance: 20100.0
Extra Balance: 5000


Hello, Bilal Sevinc
1- Check Balance
2- Withdraw Money
3- Deposit Money
Choose an action: 4
Invalid selection


Hello, Bilal Sevinc
1- Check Balance
2- Withdraw Money
3- Deposit Money
Choose an action:

"""
