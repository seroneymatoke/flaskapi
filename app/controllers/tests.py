# TalaAtm
# Created by Seroney on 04-Dec-16 7:15 PM
import pytest
import mock
from login import log_in, validate_pin
from transaction_mgt import deposit, withdrawal, validate_withdrawal_transaction, validate_deposit_transaction


ips = 'builtins.input'


@pytest.mark.incremental
# login tests
def test_validate_pin_pass():
    pin = str(2425)
    assert validate_pin(pin), True


def test_validate_pin_fail():
    pin = str(2000)
    assert validate_pin(pin) == False


def test_login_pass():
    with mock.patch(ips, return_value='2425'):
        assert log_in(), True


def test_login_fail():
    with mock.patch(ips, return_value='2423'):
        assert log_in() != True


# Transaction Management tests
def test_deposit_pass():
    balance = 2000
    with mock.patch(ips, return_value='2000'):
        assert deposit(balance) == 4000


def test_deposit_fail():
    balance = 2000
    with mock.patch(ips, return_value='6000'):
        assert deposit(balance) != 4000


def test_withdrawal_greater_than_balance_pass():
    balance = 0
    with mock.patch(ips, return_value='6000'):
        assert withdrawal(balance) == 0


def test_withdrawal_pass():
    balance = 200
    with mock.patch(ips, return_value='50'):
        assert withdrawal(balance) == 150


def test_validate_deposit():
    with mock.patch(ips, return_value='50'):
        balance = 9000
        assert validate_withdrawal_transaction(balance), 9050


def test_validate_deposit_fail():
    with mock.patch(ips, return_value='9000'):
        balance = 6000
        assert validate_deposit_transaction(balance) != -15000














