#1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
#   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
#  Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
#   Особливості реалізації:
#   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
#     - переглянути наявні купюри;
#     - змінити кількість купюр;
#   - видача грошей для користувачів відбувається в межах наявних купюр;
#   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
#2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
#   До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
import json
import os


def restart():

    del_file_list = [ f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if f.endswith(".data") ]
    for f in del_file_list:
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))

    users = {"Dmitriy": "123",
             "Andriy": "321",
             "Sergiy": "312",
             "Geekhub": "213"
             }
    
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),'users.data')
    with open(users_data, 'w') as write_file:
        json.dump(users, write_file)
    
    banknotes_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banknotes.data')
    with open(banknotes_data, 'w') as write_file:
        banknotes = {'1000':100, '500':100, '200':100, '100':100, '50':100, '20':100, '10':100}
        json.dump(banknotes, write_file)
    
    for user in users:
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_balance.data')
        with open(balance_data, 'w') as write_file:
            start_balance = 1000
            json.dump(start_balance, write_file)
    
    for user in users:
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_transactions.data')
        with open(transactions_data, 'w') as write_file:
            start_transactions = []
            json.dump(start_transactions, write_file)

def addUser():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)),'users.data')
    with open(users_data, 'r') as write_file:
        users = json.load(write_file)
        amount = int(input('Введіть кількість нових користувачів: '))
        new_users = {} 
        for _ in range(amount):
            new_users_name = input(f'Введіть імя нового користувача #{_ + 1}: ')
            new_users_password = input(f'Введіть новий пароль користувача  #{_ + 1}: ')
            users[new_users_name] = new_users_password
            new_users [new_users_name] = new_users_password
    with open(users_data, 'w') as write_file:
        json.dump(users, write_file)

    print('Ви добавили: ', end='')
    for user in new_users:
        print(f'{user}, ', end='')
    print('\n')

    for user in new_users:
        balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_balance.data')
        with open(balance_data, 'w') as write_file:
            start_balance = 1000
            json.dump(start_balance, write_file)

    for user in new_users:
        transactions_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user}_transactions.data')
        with open(transactions_data, 'w') as write_file:
            start_transactions = []
            json.dump(start_transactions, write_file)
    a = input('Продовжувати,так чи ні?')
    if a == 'так' and 'Так':
        addUser()
    elif a == 'ні' and 'Ні':
        start()
    else:
        print('Помилка! Повертаємся до головного меню.')
        start()
def autoriationUser():
    status_user = True
    user_name = input('Введіть імя: ')
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.data')
    with open(users_data, 'r') as users_data:
        users_dict = json.load(users_data)
        if user_name in users_dict:
            user_password = str(input ('Введіть пароль: '))
            counter = 2
            for _ in range(3):
                if users_dict[user_name] == user_password:
                    print(f'\n{user_name}, ласкаво просимо!')
                    status_user = True
                    break
                else:
                    print(f'Невірний пароль! Спробуйте ще раз, у вас є {counter} спроб')
                    counter -= 1             
                    user_password = str(input ('Введіть ваш пароль ще раз: '))
        else:
            print(f'Не існує такого імя {user_name}.')
    return(status_user, user_name)




def getMoney(user_name):
    desire = int(input('Введіть суму грошей: '))
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open(balance_data, 'r') as read_file:
        users_balace = json.load(read_file)
    if desire <= users_balace:
        new_users_balace = users_balace - desire
        desire1 = desire

        counter1000 = desire//1000
        desire -= 1000 * counter1000
        counter500 = desire//500
        desire -= 500 * counter500
        counter200 = desire//200
        desire -= 200 * counter200
        counter100 = desire//100
        desire -= 100 * counter100
        counter50 = desire//50
        desire -= 50 * counter50
        counter20 = desire//20
        desire -= 20 * counter20
        counter10 = desire // 10
        desire -= 10 * counter10
        transaction_text = f'Отримав гроші: {desire1}'

        with open(balance_data, 'w') as write_file:
            json.dump(new_users_balace, write_file)

        transaction_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_transactions.data')
        with open(transaction_data, 'r') as read_file:
            transactions_list = json.load(read_file)
        transactions_list.append(transaction_text)
        with open(transaction_data, 'w') as write_file:
            json.dump(transactions_list, write_file)
        print(f'Отримати гроші: {desire1} UAH!\nБанкноти:1000 UAH x {counter1000}, 500 UAH x {counter500}, 200 UAH x {counter200}, 100 UAH x {counter100}, 50 UAH x {counter50}, 20 UAH x {counter20}, 10 UAH x {counter10}')
    else:
        print('Недостатньо грошей!')
    a = input('Продовжувати,так чи ні?')
    if a == 'так' and 'Так':
        getMoney(user_name)
    elif a == 'ні' and 'Ні':
        start()
    else:
        print('Помилка! Повертаємся до головного меню.')
        start()
def topUpBalance(user_name):
    desire = int(input('Введіть суму грошей: '))
    transaction_text = f'Поповнив баланс: {desire}'
   
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open(balance_data, 'r') as read_file:
        users_balace = json.load(read_file)
    users_balace += desire

    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open(balance_data, 'w') as write_file:
        json.dump(users_balace, write_file)

    transaction_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_transactions.data')
    with open (transaction_data, 'r') as read_file:
        transactions_list = json.load(read_file)
    with open(transaction_data, 'w') as write_file:
        transactions_list.append(transaction_text)
        json.dump(transactions_list, write_file)
    print(f'Ви поповнили баланс на {desire} UAH\n')
    a = input('Продовжувати,так чи ні?')
    if a == 'так' and 'Так':
        topUpBalance(user_name)
    elif a == 'ні' and 'Ні':
        start()
    else:
        print('Помилка! Повертаємся до головного меню.')
        start()
def checkBalance(user_name):
    balance_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{user_name}_balance.data')
    with open (balance_data, 'r') as read_file:
        balance = json.load(read_file)
    print('Ваш баланс: ', balance, 'UAH')

def topUpBanknotes():
    banknotes_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banknotes.data')
    with open(banknotes_data, 'r') as read_file:
        banknotes = json.load(read_file)
    for banknote in banknotes:
        count = int(input(f'Скільки {banknote} блокнот ви б додали? '))
        banknotes[banknote] = banknotes[banknote] + count
    with open(banknotes_data, 'w') as write_file:
        json.dump(banknotes, write_file)
    print('Успішно!')
    a = input('Продовжувати,так чи ні?')
    if a == 'так' and 'Так':
        topUpBanknotes()
    elif a == 'ні' and 'Ні':
        start()
    else:
        print('Помилка! Повертаємся до головного меню.')
        start()
def checkBanknotesBalance():
    banknotes_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banknotes.data')
    with open(banknotes_data, 'r') as read_file:
        banknotes = json.load(read_file)
    money = 0
    print('')
    for banknote in banknotes:
        print(f'{banknote} UAH x', banknotes[banknote])
        money += int(banknote) * banknotes[banknote]
    print('Гроші в касі: ', money, ' UAH')

def checkRequiredFilse():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.data')
    status = os.path.isfile(users_data)
    if status == False:
        restart()
    return(status)


def start():
    checkRequiredFilse()
    user_status, user_name = autoriationUser()
    if user_name == 'admin' and user_status:
        while True:
            desire = int(input("\nIncasator menu:\nНатисніть 0 для ВИХОДУ\n"
                               "Натисніть 1 для ПОПОВНЕННЯ БАНКНОТ\n"
                               "Натисніть 2 для ПЕРЕЗАПУСК ДАННИХ\n"
                               "Натисніть 3 для ДОДАВАННЯ НОВОГО(ИХ) КОРИСТУВАЧА(ІВ)\n"
                               "Натисніть 4 для ПЕРЕВІРКИ БАЛАНС БАНКНОТ\n"))
            if desire == 1:
                topUpBanknotes()
            elif desire == 0:
                break
            elif desire == 2:
                restart()
            elif desire == 3:
                addUser()
            elif desire == 4:
                checkBanknotesBalance()
            else:
                print('Спробуйте ще раз')
                break
    else:
        if user_status:
            while True:
                desire = int(input('\nMenu:\nНатисніть 0 для ВИХОДУ\n'
                                   'Натисніть 1 для ПЕРЕВІРКИ БАЛАНСУ\n'
                                   'Натисніть 2 для ОТИРМАННЯ ГОТІВКИ\n'
                                   'Натисніть 3 для ПОПОВНЕННЯ БАЛАНСУ\n'))
                if desire == 1:
                    checkBalance(user_name)
                elif desire == 2:
                    getMoney(user_name)
                elif desire == 3:
                    topUpBalance(user_name)
                elif desire == 0:
                    break
                else:
                    print('Спробуйте ще раз')
                    break

start()
