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
    if [username, password] in data:
        return True
    elif [username, password] not in data and silent == True:
        return False
    else:
        raise LoginException('Неправильний логін або пароль')


print(f('admin','admin',False))
print(f('ап', 'sf',True))
print(f('dsfa','fsasfa',True))
print(f('Geekhub','admin'))

