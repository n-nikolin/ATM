from datetime import datetime

transactions = [
    {
        'id': 1,
        'operation': 'deposit',
        'description': 'ATM Deposit',
        'date': datetime.strptime('2022-12-01 00:00:00', "%Y-%m-%d %H:%M:%S"),
        'amount': 100
    },
    {
        'id': 2,
        'operation': 'deposit',
        'description': 'ATM Deposit',
        'date': datetime.strptime('2022-01-02 00:00:00', "%Y-%m-%d %H:%M:%S"),
        'amount': 100
    },
    {
        'id': 3,
        'operation': 'withdrawal',
        'description': 'ATM Withdrawal',
        'date': datetime.strptime('2022-01-04 00:00:00', "%Y-%m-%d %H:%M:%S"),
        'amount': 100
    },
    {
        'id': 4,
        'operation': 'deposit',
        'description': 'ATM Deposit',
        'date': datetime.strptime('2022-01-05 00:00:00', "%Y-%m-%d %H:%M:%S"),
        'amount': 100
    }
]

balance_history = [
    {'id': 0, 'date': datetime.strptime(
        '2022-01-01 00:00:00', "%Y-%m-%d %H:%M:%S"), 'balance': 100},
    {'id': 1, 'date': datetime.strptime(
        '2022-12-01 00:00:00', "%Y-%m-%d %H:%M:%S"), 'balance': 200},
    {'id': 2, 'date': datetime.strptime(
        '2022-01-02 00:00:00', "%Y-%m-%d %H:%M:%S"), 'balance': 300},
    {'id': 3, 'date': datetime.strptime(
        '2022-01-04 00:00:00', "%Y-%m-%d %H:%M:%S"), 'balance': 200},
    {'id': 4, 'date': datetime.strptime(
        '2022-01-05 00:00:00', "%Y-%m-%d %H:%M:%S"), 'balance': 300}
]