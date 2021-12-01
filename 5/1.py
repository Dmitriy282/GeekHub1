#Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
# Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
# Логіка наступна:
# якщо введено коректну пару ім'я/пароль - вертається <True>;
# якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
class LoginException(Exception):
    pass
def f(username, password, silent=False):
    dct = [{'sfgdg': 'xvdsd'},
           {'dgdsg': 'xcsdf'},
           {'dggsge': 'dfsef'},
           {'admin': 'admin'},
           {'Geekhub': 'forever'}]
    x,y,z,a,d = dct
    x.update(y)
    x.update(z)
    x.update(a)
    x.update(d)

    res = x.get(username) == password
    if not res and not silent:
        raise LoginException('Непраивльний логін і пароль')
    return res


print(f('username1', 'pass21', silent=True))
print(f('Geekhub', 'forever'))
print(f('admin','admin'))
print(f('dssdada','dsadadafsfa'))
