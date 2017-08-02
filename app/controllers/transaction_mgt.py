# TalaAtm
# Created by Seroney on 02-Dec-16 12:27 PM

from settings import deposit_params, withdrawal_params


# Deposit function
def deposit(balance):
    max_deposit_amount = deposit_params['max_deposit_amount']
    current_deposit_amount_for_day = deposit_params['current_deposit_amount_for_day']
    while True:
        try:
            while True:
                deposit_amount = int(input("Enter Numerical Amount Less or Equal to 40000: "))
                if deposit_amount > max_deposit_amount:
                    print("Deposits amount should be less than " + str(max_deposit_amount) + " per transaction")
                else:
                    break

        except ValueError:
            print("Enter valid numerical Amount Less or Equal to 40000: ")
            continue
        else:
            break

    new_balance = (balance+deposit_amount)
    deposit_params['current_deposit_amount_for_day'] = current_deposit_amount_for_day + deposit_amount
    print("Deposit Amount: " + str(deposit_amount))
    print("Current Balance: " + str(new_balance))
    return new_balance


# Withdrawal Function
def withdrawal(balance):
    # set parameters from settings file
    max_withdrawal_amount = withdrawal_params['max_withdrawal_amount']
    current_withdrawal_amount_per_day = withdrawal_params['current_withdrawal_amount_per_day']
    while True:
        try:
            while True:
                withdrawal_amount = int(input("Enter Numerical Amount"))
                if withdrawal_amount > max_withdrawal_amount:
                    print("Withdrawal amount should be less than " + str(max_withdrawal_amount) + " per transaction")
                else:
                    break

        except ValueError:
            print("Enter valid numerical amount")
            continue
        else:
            break

    if withdrawal_amount > balance:
        print("Cannot withdraw amount more than: " + str(balance))
        print("Exiting:")
        return balance
    else:
        new_with_balance = (balance-withdrawal_amount)
        withdrawal_params['current_withdrawal_amount_per_day'] = current_withdrawal_amount_per_day + withdrawal_amount
        print("Withdrawn Amount: " + str(withdrawal_amount))
        print("Current Balance: " + str(new_with_balance))
        balance = new_with_balance
        return balance


# Validating withdrawal transaction
def validate_deposit_transaction(balance):

    current_deposit_frequency_for_day = deposit_params['current_deposit_frequency_for_day']
    max_deposit_frequency_per_day = deposit_params['max_deposit_frequency_per_day']
    current_deposit_amount_for_day = deposit_params['current_deposit_amount_for_day']
    max_deposit_amount_per_day = deposit_params['max_deposit_amount_per_day']

    if current_deposit_frequency_for_day < max_deposit_frequency_per_day:
        print("Print current deposit frequency: " + str(current_deposit_frequency_for_day))
        print("Print current deposit amount for the day: " + str(current_deposit_amount_for_day))

        if current_deposit_amount_for_day < max_deposit_amount_per_day:
            deposit_params['current_deposit_frequency_for_day'] = current_deposit_frequency_for_day + 1
            return deposit(balance)
        else:
            print("Maximum Deposits Reached for the Day")
            balance = 0
            return deposit(balance)
    else:
        print("Deposit transaction limit reached")
        print("Current deposit frequency for day" + str(deposit_params['current_deposit_frequency_for_day']))
        deposit_params['current_deposit_frequency_for_day'] = 0
        print("Resetting current deposit frequency to: " + str(deposit_params['current_deposit_frequency_for_day']))
    return 0


# Validating withdrawal transaction
def validate_withdrawal_transaction(balance):
    # Setting parameter values from settings file
    current_withdrawal_frequency_for_day = withdrawal_params['current_withdrawal_frequency_for_day']
    max_withdrawal_frequency_per_day = withdrawal_params['max_withdrawal_amount_per_day']
    current_withdrawal_amount_per_day = withdrawal_params['current_withdrawal_amount_per_day']
    max_withdrawal_amount_per_day = withdrawal_params['max_withdrawal_amount_per_day']

    if current_withdrawal_frequency_for_day < max_withdrawal_frequency_per_day:
        print("Print current withdrawal frequency: " + str(current_withdrawal_frequency_for_day))
        print("Print current withdrawal amount for the day: " + str(current_withdrawal_amount_per_day))

        if current_withdrawal_amount_per_day < max_withdrawal_amount_per_day:
            withdrawal_params['current_withdrawal_frequency_for_day'] = current_withdrawal_frequency_for_day + 1
            return withdrawal(balance)
        else:
            print("Maximum Deposits Reached for the Day")
            balance = 0
            return balance
    else:
        print("Withdrawal transaction limit reached")
        print(withdrawal_params['current_withdrawal_amount_per_day'])
        withdrawal_params['current_withdrawal_frequency_for_day'] = 0
        print("Resetting current withdrawal frequency to: " + str(withdrawal_params['current_withdrawal_frequency_for_day']))
    return 0




