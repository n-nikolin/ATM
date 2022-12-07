from tabulate import tabulate, SEPARATING_LINE  # type: ignore

def create_table(transactions):
    table_rows = []
    for transaction in transactions:
        row = []
        for v in transaction.values():
            row.append(v)
        table_rows.append(row)
    headers = ['Date', 'Description', 'Withdrawals', 'Deposits', 'Balance']
    table_rows.insert(1, SEPARATING_LINE)
    table_rows.insert(-1, SEPARATING_LINE)
    table = tabulate(table_rows, headers, tablefmt="simple", stralign="right")
    return table
