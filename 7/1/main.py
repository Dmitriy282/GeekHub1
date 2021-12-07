#Програма-банкомат.
#   Створити програму з наступним функціоналом:
#      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
#      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
#      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
#   Особливості реалізації:
#      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
#      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
#      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
#   Особливості функціонала:
#      - за кожен функціонал відповідає окрема функція;
#      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
#      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
#      - потім - елементарне меню типа:
#        Введіть дію:
#           1. Продивитись баланс
#           2. Поповнити баланс
#           3. Вихід
#      - далі - фантазія і креатив :)

import json
import os


def createUsersData():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users_data.data')
    users = {"Dmitriy": "123",
             "Andriy": "321",
             "Sergiy": "312",
             "Geekhub": "213"
             }
    with open(users_data, "w") as write_file:
        json.dump(users, write_file)
    write_file.close()

    for _ in users:
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{_}_balance.data')
        balance = 0
        with open(balance_data, "w") as write_file:
            json.dump(balance, write_file)
            write_file.close()
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{_}_transactions.data')
        transactions = []
        with open(transactions_data, "w") as write_file:
            json.dump(transactions, write_file)
            write_file.close()


def start():
    name = str(input('Введіть імя: '))
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users_data.data')
    with open(users_data, 'r') as data_names:
        json_users = json.load(data_names)
        if name in json_users:
            password = str(input('Введіть пароль: '))
            if json_users[name] == password:
                print(f'{name}, ''ласкаво просимо!')
            else:
                print('Невірний пароль!')
                return False
        else:
            print(f'Не існує такого імя {name}!')
            return False
        data_names.close()

    desire = int(input('Натисніть 1 для ПЕРЕВІРКИ БАЛАНСУ\n'
                       'Натисніть 2 для ОТИРМАННЯ ГОТІВКИ\n'
                       'Натисніть 3 для ПОПОВНЕННЯ БАЛАНСУ\n'))
    if desire == 1:
        checkBalance(name)
    elif desire == 2:
        getCash(name)
    elif desire == 3:
        topUpBalance(name)
    else:
        print('Спробуйте ще раз')


def checkBalance(name):
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_balance.data')
    with open(balance_data, 'r') as balance:
        json_balance = json.load(balance)
        print('Ваш баланс: ', json_balance, '$')
    balance.close()


def getCash(name):
    desire = int(input('Видача готівки: '))
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_balance.data')
    with open(balance_data, 'r') as balance:
        json_balance = json.load(balance)
        if desire > json_balance:
            print('Недостатньо грошей на вашому балансі!')
        else:
            with open(balance_data, 'w') as balance:
                new_balance = json_balance - desire
                json.dump(new_balance, balance)
            balance.close()
            transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_transactions.data')
            with open(transactions_data, 'a') as new_transaction:
                transaction = f'Отримайте готівку: {desire}'
                json.dump(transaction, new_transaction)
            new_transaction.close()
    balance.close()


def topUpBalance(name):
    desire = int(input('Роздрукувати суму грошей для поповнення: '))
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_balance.data')
    with open(balance_data, 'r') as balance:
        json_balance = json.load(balance)
        with open(balance_data, 'w') as balance:
            new_balance = json_balance + desire
            json.dump(new_balance, balance)
        balance.close()
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{name}_transactions.data')
        with open(transactions_data, 'a') as new_transaction:
            transaction = f'Поповніть баланс: {desire}'
            json.dump(transaction, new_transaction)
        new_transaction.close()
    balance.close()


start()