import argparse
import shlex
from datetime import datetime
from client import Client

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        msg = "not a valid date: {0!r}".format(s)
        raise argparse.ArgumentTypeError(msg)

def choose_action(client, args):
    if args.cmd == 'deposit':
        return client.deposit(args.amount, args.description)
    if args.cmd == 'withdraw':
        return client.withdraw(args.amount, args.description)
    if args.cmd == 'show_bank_statement':
        return client.show_bank_statement(args.since, args.till)


def bank():
    parser = argparse.ArgumentParser(prog='PROG', description='description')
    parser.add_argument(
        'cmd', choices=['deposit', 'withdraw', 'show_bank_statement', 'help', 'quit'])
    parser.add_argument('--client', type=str, help='client name')
    parser.add_argument('--amount', type=int,
                        help=' of money to withdraw or deposit')
    parser.add_argument('--description', type=str,
                        help='a description of the performed op')
    parser.add_argument('--since', type=valid_date, help='Since date')
    parser.add_argument('--till', type=valid_date, help='Till date')
    print('Service started!')

    # Создание экземпляра для сессии
    astr = input(r'>: ')
    args = parser.parse_args(shlex.split(astr))
    client = Client(args.client)
    choose_action(client, args)

    while True:
        try:
            # Циклл ввода-вывода
            astr = input(r'>: ')
            args = parser.parse_args(shlex.split(astr))
            if args.cmd == 'quit':
                print('Service stopped!')
                break
            if args.cmd == 'help':
                parser.print_help()
            if client.name == args.client:
                choose_action(client, args)
            else:
                print('Please finish current user session\
                    \nIf you would like to extit current session,\
                    \nplease input "quit" into the commeand prompt')
        # ошибки и исключения для продолжения работы после ввода неверных данных
        except SystemExit:
            print('Invalid args')
        except ValueError:
            print('Invalid value/values')
        except TypeError:
            print('Incomplete request')

if __name__ == '__main__':
    bank()