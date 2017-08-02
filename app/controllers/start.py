# TalaAtm
# Created by Seroney on 02-Dec-16 10:23 AM

from login import log_in
from transaction_mgt import validate_deposit_transaction, validate_withdrawal_transaction


# Start menu Functions
def start_menu():
    print("Welcome To Tala ATM")
    #
    if log_in():
        # Start Menu Option
        while True:
            balance = 0
            try:
                # Set menu options
                print("Enter 1 to check balance")
                print("Enter 2 to Deposit")
                print("Enter 3 to Withdraw")
                print("Enter 0 to Exit")
                menu_option = int(input("Enter Option: "))

                while True:
                    try:
                        total = total
                    except UnboundLocalError:
                        total = balance
                        break
                    else:
                        break

                if menu_option not in (0, 1, 2, 3):
                    print("Invalid Value")
                    continue

                if menu_option == 1:

                    # Display only if balance = 0
                    if total < 0:
                        print("Current Balance: " + str(total))
                        print("Available Balance: " + str(balance))
                    else:
                        print("Current Balance: " + str(total))
                        print("Available Balance: " + str(balance))
                    continue
                elif menu_option == 2:
                    # Deposits menu
                    total = + validate_deposit_transaction(total)
                    continue
                elif menu_option == 3:
                    # Call Withdrawal Function
                    total = validate_withdrawal_transaction(total)
                    continue
                else:
                    print("Exiting- Thank you for using our application")
                    break

            except ValueError:
                print("Enter correct value")
                continue

    else:
        print("Contact TALA admin")

