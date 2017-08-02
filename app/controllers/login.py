# Project - TalaAtm
# Created by Seroney on 02-Dec-16 10:00 AM


def validate_pin(pin):
    if pin == '2425':
        return True
    else:
        return False


def log_in():
    tries = 0
    pin_limit = 3
    while tries < pin_limit:
        pin = input('Please Enter You 4 Digit Pin: ')
        if validate_pin(pin):
            print("Pin accepted!")
            return True
        else:
            tries += 1
            print("Invalid pin. No of retries remaining: " + str(pin_limit-tries))
    print("To many incorrect tries. Could not log in")
    return False

