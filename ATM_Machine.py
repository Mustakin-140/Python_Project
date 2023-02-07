username = "Mahi140"
password = "Mahi@cse140"

c_name = input("Enter your username: ")
c_pass = str(input("Enter your password: "))

if c_name == username and c_pass == password:
    print("Successfully logged in to your account! Enjoy our Services!!")
    print('''
    1. Deposit
    2. Withdraw
    3. Ministatement
    4. Exit
     ''')

    amount = 5000
    option = int(input("Select your option: "))
    if option == 1:
        dep = int(input("Enter the amount you want to deposit: "))
        amount += dep
        print("Current total amount: ",amount)

    elif option == 2:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        amount -= withdraw
        print("Current total amount: ",amount)

    elif option == 3:
        print("==========ATM==========")
        print("Username: ",username)
        print("Total Amount: ",amount)
        print("=======================")

else:
    print("Please Enter correct Information")