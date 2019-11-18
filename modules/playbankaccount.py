import os, json

transactions_path = 'transactions.json'

def pressenter_stopping(func):
    def stopping(transactions):
        func(transactions)
        input('\nНажмите Enter чтобы продолжить ')
    return stopping

def save_transactions(transactions, transactions_path):
    with open(transactions_path, 'w', encoding='utf-8') as tfile:
        tfile.write(json.dumps(transactions, ensure_ascii=False))

def read_transactions(transactions_path):
    with open(transactions_path, 'r', encoding='utf-8') as tfile:
        transactions = json.loads(tfile.read())
    return transactions

@pressenter_stopping
def put_cash(transactions):
    amount = input('Введите сумму для пополнения: ')
    while not amount.isdecimal() or not int(amount)>0:
        print('Некорректная сумма для пополнения счета!')
        amount = input('Введите сумму для пополнения: ')
    transactions.append(("Пополнение счета", int(amount)))
    save_transactions(transactions, transactions_path)
    print(f'Счет пополнен!')

@pressenter_stopping
def buy(transactions):
    sum_transactions = sum([transaction[1] for transaction in transactions])
    if sum_transactions == 0:
        print('Необходимо пополнить счет перед покупкой!')
    else:
        amount = input('Введите сумму покупки: ')
        while not amount.isdecimal() or int(amount)<1:
            print('Некорректная сумма покупки!')
            amount = input('Введите сумму покупки: ')
        if not int(amount) > sum_transactions:
            product_name = input('Введите название продукта: ')
            transactions.append(('Покупка '+product_name, -int(amount)))
            save_transactions(transactions, transactions_path)
            print(f'Покупка "{product_name}" выполнена!')
        else:
            print('Недостаточно средств для покупки на данную сумму!')

@pressenter_stopping
def get_transactions_history(transactions):
    print('История операций со счетом:')
    if len(transactions) == 0:
        print('***Отсутствуют операции со счетом на данный момент')
    else:
        for name, amount in transactions:
            print(f'--- {name}: {amount} валюты')

def play_bank_account():
    print('Game Bank Account v0.1')
    option_putting_cash = '1. пополнение'
    option_buying = '2. покупка'
    option_transactions_history = '3. история покупок'
    option_exit_game = '4. выход'
    if os.path.isfile(transactions_path):
        try:
            transactions = read_transactions(transactions_path)
        except:
            print('Ошибка чтения файла с транзакциями, произведен сброс')
            transactions = []
    else:
        transactions = []
    while True:
        print('*'*20)
        sum_transactions = sum([transaction[1] for transaction in transactions])
        print('Баланс счета:', sum_transactions)

        print('Меню операций со счетом:')
        print(option_putting_cash)
        print(option_buying)
        print(option_transactions_history)
        print(option_exit_game)
        print('-'*20)

        choice = input('Выберите пункт меню: ')
        if choice == option_putting_cash[0]:
            print('Опция:', option_putting_cash)
            put_cash(transactions)
        elif choice == option_buying[0]:
            print('Опция:', option_buying)
            buy(transactions)
        elif choice == option_transactions_history[0]:
            print('Опция:', option_transactions_history)
            get_transactions_history(transactions)
        elif choice == option_exit_game[0]:
            print('Завершение Bank Account...')
            break
        else:
            print('Неверный пункт меню')
    return transactions
