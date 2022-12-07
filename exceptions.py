msg = {
    'negative_num': 'Amount has to be a positive number',
    'not_enough_cash': 'Entered sum exceeds client balance',
    'amount_wrong_type': 'Amount has to be a number',
    'description_wrong_type': 'Description has to be a string',
    'invalid_name': 'Invalid name'
}


def is_name(name):
    if isinstance(name, str) == False:
        raise TypeError(msg['invalid_name'])


def is_description(description):
    if isinstance(description, str) == False:
        raise TypeError(msg['description_wrong_type'])


def is_amount(amount):
    if isinstance(float(amount), float) == False:
        raise ValueError(msg['amount_wrong_type'])
    if amount < 0:
        raise ValueError(msg['negative_num'])


def check_balance(account, amount):
    if amount > account:
        raise ValueError(msg['not_enough_cash'])
