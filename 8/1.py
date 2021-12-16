# 1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
#   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
#  Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
#   Особливості реалізації:
#   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
#   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
#     - переглянути наявні купюри;
#     - змінити кількість купюр;
#   - видача грошей для користувачів відбувається в межах наявних купюр;
#   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
# 2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
#   До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
import json
import os


def check_user():
    tries = 0
    while tries < 3:
        file_json = "users.json"
        with open(file_json, "r") as f:
            users_data = json.load(f)
        username = input("Введіть ім'я користувача: ")
        password = input('Введіть пароль: ')
        if any(i.get('username') == username for i in users_data):
            if any(i.get('password') == password for i in users_data):
                print("Ви ввійшли до банківської системи!\n")
                if username and password == 'admin':
                    atm_collection(username)
                return username
            else:
                print('Ви ввели невірний пароль !')
                tries += 1
        else:
            print("Будь ласка, введіть коректне ім'я!")
            tries += 1
    print('Вибачне, але Ви тричі ввели невірні данні.\n Ваша картка буде заблокована!')
    return False


def atm_collection(user):
    while True:
        selection = int(input('''Введіть дію: 
    1. Переглянути залишок коштів у банкоматі
    2. Поповнити банкомат
    3. Добавити користувача
    4. Вихід
 Ваш вибір: '''))
        if selection == 1:
            print('Перегляд балансу банкомату.')
            operation = "check balance ATM"
            print(f'Всього в банкоматі {check_balance_ATM(operation)} грн.\n')
        elif selection == 2:
            print('Поповнення банкомату.')

            load_atm(user)
        elif selection == 3:
            addUser()
        elif selection == 4:
            print('Вихід!')
            print('Дякуємо за Ваш вибір!')
            break
        else:
            print('Неправильний вибір! Повторіть спробу!')
    else:
        print('Програма "Банкомат" завершила свою роботу!')





def get_money(money, arg=0):
    
    with open('admin_balance.json', 'r') as g:
        real_banknotes = json.load(g)
        lst_banknotes_new = real_banknotes
        lst_banknotes = {int(key): value for key, value in real_banknotes.items()}
    
    res = []

    for k, v in lst_banknotes.items():
        while money-k >= 0 and v > 0:
            money -= k
            v -= 1
            res.append(k)
            if arg == 1:
                lst_banknotes_new[str(k)] = lst_banknotes[k]-1
                lst_banknotes[k] = lst_banknotes[k]-1

    if arg == 1:
        with open('admin_balance.json', 'w') as ed:
            json.dump(lst_banknotes_new, ed)
    
    return res, money




def check_enough_banknotes_atm(money):
    lst_banknotes = get_money(money)
    dict_number_banknotes = {str(i): lst_banknotes.count(i) for i in lst_banknotes}
    user = 'admin'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        dict_admin_balance = json.load(f)
    result_dict = {key: dict_admin_balance[key] - dict_number_banknotes[key] for key in dict_admin_balance if
                   key in dict_number_banknotes}
    return all(value >= 0 for value in result_dict.values())


def check_balance_ATM(operation):
    user = 'admin'
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance = json.load(f)
    all_money = (sum(int(bancknote) * value for bancknote, value in admin_balance.items()))
    if operation == "check balance ATM":
        print(f'Всього у банкоматі: {all_money} грн.', '\n')
        print('У банкоматі знаходиться: ')
        for bancknote, value in admin_balance.items():
            print(f"Банкнот {bancknote} грн. - {value} шт.")
        add_transaction(user, operation, all_money)
    return all_money


def check_banknote(user, banknote):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance = json.load(f)
    banknote = str(banknote)
    return admin_balance[banknote]


def add_cash_to_atm(user, banknote, number):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        admin_balance = json.load(f)
    banknote = str(banknote)
    admin_balance[banknote] += number
    with open(user_file, "w") as f:
        json.dump(admin_balance, f)
    with open(user_file, "r") as f:
        balance = json.load(f)
    operation = "load ATM"
    banknote = int(banknote)
    money = banknote * number
    add_transaction(user, operation, money)
    print(f'В банкомат завантажено {number} банкнот  по {banknote} грн. Всього завантажено {money} грн.\n')


def load_atm(user):
    banknote = input('Введіть номінал поповнення 10, 20, 50, 100, 200, 500 чи 1000 грн.: ')
    if banknote.isdigit():
        banknote = int(banknote)
        if banknote in [10, 20, 50, 100, 200, 500, 1000]:
            number = input('Введіть кількість банкнот поповнення: ')
            if number.isdigit():
                number = int(number)
                if 0 < number < 100:
                    banknotes_in_atm = check_banknote(user, banknote)
                    if number + banknotes_in_atm <= 100:
                        add_cash_to_atm(user, banknote, number)
                    else:
                        print(f'В банкоматі банкнота {banknote} грн. у кількості {banknotes_in_atm} шт. \n\
Можна цю банкноту покласти у кількості {100 - banknotes_in_atm} шт.')
                else:
                    print('В банкомат можна завантажити від 1 до 100 банкнот. Ввведіть коректну кількість.')
            else:
                print('Будь ласка, введіть лише цифрове значення!\n')
        else:
            print('Банкомат не підтримує даний номінал!')
    else:
        print('Будь ласка, введіть лише цифрове значення!\n')


def add_transaction(user, operation, money):
    transaction_file = user + "_transactions.json"
    if os.path.isfile(transaction_file):
        with open(transaction_file, "r", encoding="utf-8") as f:
            info = json.load(f)
            number_transaction = info[-1]["Transaction"] + 1
    else:
        number_transaction = 1
    if operation == "deposite":
        money = "+" + str(money)
    elif operation == "withdraw":
        money = "-" + str(money)
    user_info = {"Transaction": number_transaction,
                 "Operation": operation,
                 "Balance": money}
    if os.path.isfile(transaction_file):
        with open(transaction_file, "r", encoding="utf-8") as f:
            info = json.load(f)
        info.append(user_info)
        with open(transaction_file, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=4, ensure_ascii=False)
    else:
        with open(transaction_file, "w", encoding="utf-8") as f:
            lst = []
            lst.append(user_info)
            json.dump(lst, f, indent=4, ensure_ascii=False)
    return


def check_balance(user, operation):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        balance = json.load(f)
    money = balance["account"]
    if operation == "deposite" or operation == "withdraw":
        return money
    else:
        add_transaction(user, operation, money)
    return money


def deposite(user, money):
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        balance = json.load(f)
    balance["account"] += money
    with open(user_file, "w") as f:
        json.dump(balance, f)
    with open(user_file, "r") as f:
        balance = json.load(f)
    operation = "deposite"
    add_transaction(user, operation, money)
    return balance["account"]


def withdraw(user, money):
    operation = "withdraw"
    user_file = user + "_balance.json"
    with open(user_file, "r") as f:
        balance = json.load(f)
    balance["account"] -= money
    with open(user_file, "w") as f:
        json.dump(balance, f)
    add_transaction(user, operation, money)
    user = 'admin'

    add_transaction(user, operation, money)
    return


def addUser():
    users_data = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.json')
    with open(users_data, 'r') as write_file:
        users = json.load(write_file)
    username = input('Введіть імя нового користувача: ')
    password = input("Введіть новий пароль користувача: ")
    user_info = {'username': username, 'password': password}
    users.append(user_info)
    with open(users_data, 'w') as write_file:
        json.dump(users, write_file)
    print(f'Ви добавили {username} користувача')

def start():
    user = check_user()
    if user and user != 'admin':
        while True:
            selection = int(input('''Введіть дію: 
    1. Продивитись баланс
    2. Поповнити баланс
    3. Зняти кошти
    4. Вихід
 Ваш вибір: '''))
            if selection == 1:
                print('Перегляд балансу.')
                operation = "check balance"
                print(f'На Вашому рахунку {check_balance(user, operation)} грн.\n')
            elif selection == 2:
                print('Поповнення балансу.')
                money = input('Введіть суму поповнення: ')
                if money.isdigit():
                    money = int(money)
                    if money in [1000, 500, 200, 100, 50, 20,10]:
                        print(f'На Вашому рахуноку {deposite(user, money)} грн., його поповнено на суму {money} грн.\n')
                    else:
                        print('Банкомат приймає лише номінали 10,20, 50, 100, 200, 500 або 1000 грн.!\n')
                else:
                    print('Будь ласка, введіть лише цифрове значення!\n')

            elif selection == 3:
                print('Зняття коштів.')
                operation = "withdraw"
                money = input('Введіть необхідну суму: ')
                if money.isdigit():
                    money = int(money)
                    if money != 0 and money % 10 == 0 and money not in [0,10]:
                        if check_balance(user, operation) - money >= 0:
                            if check_balance_ATM(operation) - money >= 0:
                                if check_enough_banknotes_atm(money):
                                    banknotes, change = get_money(money, 1)
                                    if change == 0:
                                        withdraw(user, money)
                                        print(
                                        f'На Вашому рахуноку {check_balance(user, operation)} грн., з нього знято {money} грн.')
                                        print(banknotes)
                                    else:
                                        print('Немає купюр для виводу')

                                    return start()
                                else:
                                    print('У банкоматі немає банкнот для видачі зазначену суму!')
                            else:
                                print('На даний момент у банкоматі недостатньо коштів для видачі вказаної суми!\n')
                        else:
                            print('На Вашому рахунку недостатньо коштів!\n')
                    else:
                        print(
                            f'Введенної суми, {money} грн., банкомат не може видати наявними номіналами 10, 20, 50, 100, 200, 500 і 1000 грн!')
                else:
                    print('Будь ласка, введіть лише цифрове значення!\n')

            elif selection == 4:
                print('Вихід!')
                print('Дякуємо за Ваш вибір!')
                print('Програма "Банкомат" завершила свою роботу!')
                break
            else:
                print('Неправильний вибір! Повторіть спробу!')
    else:
        print('Програма "Банкомат" завершила свою роботу!')


start()
