
def put_cash(transactions):
    amount = input('Введите сумму для пополнения: ')
    while not amount.isdecimal() or not int(amount)>0:
        print('Некорректная сумма для пополнения счета!')
        amount = input('Введите сумму для пополнения: ')
    transactions.append(("Пополнение счета", int(amount)))

def buy(transactions):
    sum_transactions = sum([trans[1] for trans in transactions])
    if sum_transactions == 0:
        print('Необходимо пополнить счет перед покупкой!')
        input('\nНажмите Enter чтобы продолжить ')
    else:
        amount = input('Введите сумму покупки: ')
        while not amount.isdecimal() or int(amount)<1:
            print('Некорректная сумма покупки!')
            amount = input('Введите сумму покупки: ')
        if not int(amount) > sum_transactions:
            product_name = input('Введите название продукта: ')
            transactions.append(('Покупка '+product_name, -int(amount)))
        else:
            print('Недостаточно средств для покупки на данную сумму!')
            input('\nНажмите Enter чтобы продолжить ')

def get_transactions_history(transactions):
    print('История операций со счетом:')
    if len(transactions) == 0:
        print('***Отсутствуют операции со счетом на данный момент')
    else:
        for name, amount in transactions:
            print(f'--- {name}: {amount} валюты')
    input('\nНажмите Enter чтобы продолжить ')

def play_bank_account(transactions = []):
    print('Game Bank Account v0.1')
    option_putting_cash = '1. пополнение'
    option_buying = '2. покупка'
    option_transactions_history = '3. история покупок'
    option_exit_game = '4. выход'
    while True:
        print('*'*20)
        sum_transactions = sum([trans[1] for trans in transactions])
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
