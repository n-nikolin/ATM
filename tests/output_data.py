from datetime import datetime

table_data = [
    {
        'date': '',
        'description': 'Previous balance',
        'withdrawal': '',
        'deposit': '',
        'balance': '$200.0'
    },

    {
        'date': datetime.strptime('2022-01-02 00:00:00', "%Y-%m-%d %H:%M:%S"),
        'description': 'ATM Deposit',
        'withdrawal': '',
        'deposit': '$100.0',
        'balance': '$300.0'

    },
    {
        'date': datetime.strptime('2022-01-04 00:00:00', "%Y-%m-%d %H:%M:%S"),
        'description': 'ATM Withdrawal',
        'withdrawal': '$100.0',
        'deposit': '',
        'balance': '$200.0'
    },
    {
        'date': '',
        'description': 'Totals',
        'withdrawal': f"${float(100)}",
        'deposit': f"${float(100)}",
        'balance': f"${float(200)}"
    }
]
