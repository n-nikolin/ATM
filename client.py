from datetime import datetime, timedelta
from create_table import create_table
from exceptions import is_name, is_description, is_amount, is_name, check_balance
from time import sleep


def append_data(transactions, balance_history,
                num_transactions, balance,
                operation, description, amount):
    # функция, которая добавления элементов в списки balance_history и
    # transactions
    date = datetime.now()
    balance_history.append({
        'id': num_transactions,
        'date': date,
        'balance': balance
    })
    transactions.append({'id': num_transactions,
                         'operation': operation,
                         'description': description,
                         'date': date,
                         'amount': float(amount)})


class Client:
    """
    списки transactions и balance_history имеют общие id и date
    id нужен, чтобы связывать transaction и balance
    """

    def __init__(self, name, balance=float(0), transactions=[],
                 num_transactions=0, balance_history=[]):
        self.name = name
        is_name(name)
        self.balance = balance
        is_amount(balance)
        self.transactions = transactions
        self.num_transactions = num_transactions
        self.balance_history = balance_history
        # добавление нулевого элемента в список, для сохранения баланса,
        # указанного при создании экземпляра Client
        balance_history.append(
            {'id': num_transactions, 'date': datetime.now(), 'balance': balance})

    def deposit(self, amount, description):
        """фунция внесения денег на личный счет"""
        try:
            # проверки на ошибки
            is_description(description)
            is_amount(amount)
            # переменные, нужные для выполнения функии append_data
            operation = 'deposit'
            self.balance += amount
            self.num_transactions += 1
            append_data(self.transactions, self.balance_history,
                        self.num_transactions, self.balance, operation,
                        description, amount)
            print(f'{description}: {amount}')
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)

    def withdraw(self, amount, description):
        """функция снятия денег со счета"""
        try:
            # проверки на ошибки
            is_description(description)
            is_amount(amount)
            check_balance(self.balance, amount)
            # переменные, нужные для выполнения функии append_data
            operation = 'withdrawal'
            self.balance -= amount
            self.num_transactions += 1
            append_data(self.transactions, self.balance_history,
                        self.num_transactions, self.balance, operation, description, amount)
            print(f'{description}: {amount}')
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)

    def show_bank_statement(self, since, till):
        """
        функция вывода отчета, в которой создается словарь для последующей п
        ереработку данных в таблицу фунцией create_table
        """
        # создание переменных, нужных для составления отчета
        total_deposits = 0
        total_withdrawals = 0
        table_data = []
        # объединение словарей balance_history и transactions по принципу равенства id
        for i in self.transactions:
            for j in self.balance_history:
                if i['id'] == j['id']:
                    # выборка дат на основе соответствия аргументам функции
                    if i['date'] >= since and i['date'] <= till:
                        # пополнения
                        if i['operation'] == 'deposit':
                            total_deposits += i['amount']
                            table_data.append({
                                'id': i['id'],
                                'date': i['date'],
                                'description': i['description'],
                                'withdrawal': '',
                                'deposit': f"${float(i['amount'])}",
                                'balance': f"${float(j['balance'])}"
                            })
                        # списания
                        if i['operation'] == 'withdrawal':
                            total_withdrawals += i['amount']
                            table_data.append({
                                'id': i['id'],
                                'date': i['date'],
                                'description': i['description'],
                                'withdrawal': f"${float(i['amount'])}",
                                'deposit': '',
                                'balance': f"${float(j['balance'])}"
                            })
        # Получение исходного и итогового балансов для указанного временного интервала
        if len(table_data) > 0:
            begin_balance = self.balance_history[table_data[0]
                                                 ['id'] - 1]['balance']
            begin_balance = float(begin_balance)
            end_balance = table_data[-1]['balance']
        # Получене исходного и итогового баланса, если table_data пустой.
        else:
            # Наверное есть более простой и лаконичный способ это сделать,
            # но сегодня уже вряд ли смогу его написать
            dates = [i['date'] for i in self.balance_history]
            begin_balance = 0 
            try:
                # выбор ближайшей наименьщей даты к аргументу since
                nearest_date = min(i for i in dates if i > since)
                for i in self.balance_history:
                    if i['date'] == nearest_date:
                        begin_balance = float(i['balance'])
                end_balance = f'${begin_balance}'
            except ValueError:
                # Если наименьшей ближайшей даты в списке нет, то
                # итоговый и исходный балансы равны последнему элементу списка balance_history
                begin_balance = float(self.balance_history[-1]['balance'])
                end_balance = f'${begin_balance}'
        # избавление от id перед печатью
        for i in table_data:
            if 'id' in i:
                del i['id']
        # ряд с подзаголовком и исходным балансом
        table_data.insert(0, {
            'date': '',
            'description': 'Previous balance',
            'withdrawal': '',
            'deposit': '',
            'balance': f"${float(begin_balance)}"
        })
        # ряд с итоговыми значениями
        table_data.append({
            'date': '',
            'description': 'Totals',
            'withdrawal': f"${float(total_withdrawals)}",
            'deposit': f"${float(total_deposits)}",
            'balance': f"{end_balance}"
        })
        # 
        table = create_table(table_data)
        print(table)
        return table_data

client = Client('john johnson', 1000)
client.deposit(1000, 'ATM')
sleep(1)
sleep(1)
sleep(1)
sleep(1)
client.withdraw(1000, 'ATM')
client.deposit(13330, 'ATM')
client.show_bank_statement(
    datetime.now()-timedelta(seconds=10), datetime.now())

client.show_bank_statement(
    datetime.now()-timedelta(seconds=3), datetime.now()-timedelta(seconds=1))
client.show_bank_statement(
    datetime.now()-timedelta(seconds=15), datetime.now()-timedelta(seconds=10))