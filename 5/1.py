#Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception):
    pass
def f(username, password, silent=False):
    data = [['sfgdg', 'xvdsd'],
                 ['dgdsg', 'xcsdf'],
                 ['dggsge', 'dfsef'],
                 ['admin', 'admin'],
                 ['Geekhub', 'forever']]
    list_user1 = [i[0] for i in data]
    passwords1 = [i[1] for i in data]
    if username in list_user1 and password in passwords1 and silent == False:
        return True
    elif username not in list_user1 and password not in passwords1 and silent == True:
        return False
    elif username not in list_user1 or password not in passwords1 and silent == True:
        return False
    elif username in list_user1 and password in passwords1 and silent == True:
        return True
    else:
        raise LoginException('Невірно логін або пароль')

print(f('Geekhub','forever'))
print(f('ап', 'sf',True))
print(f('admin','admin',True))
print(f('dsfa','fsasfa',True))
print(f('Geekhub','sdsdadfsaf'))
