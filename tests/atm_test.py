import pytest
from time import sleep
from datetime import datetime
from client import Client, append_data
from exceptions import is_name, is_amount, is_description, check_balance
import tests.imput_data as imput_data
import tests.output_data as output_data


client = Client('jeff jeff', 1000)


def test_class_init():
    assert client.name == 'jeff jeff'
    assert client.balance == 1000
    date = client.balance_history[0]['date']
    assert len(client.transactions) == 0
    assert client.transactions == []
    assert client.num_transactions == 0
    assert len(client.balance_history) == 1
    assert client.balance_history == [{'id': 0, 'date': date, 'balance': 1000}]


def test_deposit():
    client.deposit(100, 'ATM Deposit')
    date = client.transactions[0]['date']
    assert client.balance == 1100
    assert len(client.transactions) == 1
    assert client.transactions == [{
        'id': 1,
        'operation': 'deposit',
        'description': 'ATM Deposit',
        'date': date,
        'amount': 100.0
    }]
    assert len(client.balance_history) == 2
    assert client.balance_history[1] == {
        'id': 1, 'date': date, 'balance': 1100}


def test_withdraw():
    client.withdraw(100, 'ATM Wihdrawal')
    date = client.transactions[1]['date']
    assert client.balance == 1000
    assert len(client.transactions) == 2
    assert client.transactions[1] == {
        'id': 2,
        'operation': 'withdrawal',
        'description': 'ATM Wihdrawal',
        'date': date,
        'amount': 100.0
    }
    assert len(client.balance_history) == 3
    assert client.balance_history[2] == {
        'id': 2, 'date': date, 'balance': 1000}
    assert len(client.balance_history) == 3
    assert len(client.transactions) == 2


def test_show_bank_statement():
    client_2 = Client('mary jane', 100)
    client_2.transactions = imput_data.transactions
    client_2.balance_history = imput_data.balance_history
    assert client_2.show_bank_statement(
        datetime.strptime('2022-01-02 00:00:00', "%Y-%m-%d %H:%M:%S"),
        datetime.strptime('2022-01-04 00:00:00', "%Y-%m-%d %H:%M:%S")) == output_data.table_data


def test_append_data():
    date = datetime.now()
    transactions = []
    balance_history = [
        {'id': 0, 'date': date, 'balance': 1000}]
    num_transactions = 0
    balance = 1000
    operation = 'deposit'
    description = 'ATM deposit'
    amount = 1000
    append_data(transactions, balance_history, num_transactions,
                balance, operation, description, amount)
    assert transactions == [{
        'id': num_transactions, 'operation': operation,
        'description': description, 'date': date, 'amount': float(amount)}]
    assert len(balance_history) == 2
    assert balance_history == [{'id': num_transactions, 'date': date, 'balance': 1000},
                               {'id': num_transactions, 'date': date, 'balance': 1000}]


def test_exceptions():
    with pytest.raises(ValueError):
        is_amount(-100)
        check_balance(100, 101)
        is_amount('jeff')
        check_balance(100, 101)
    with pytest.raises(TypeError):
        is_name(123)
        is_description(123)
