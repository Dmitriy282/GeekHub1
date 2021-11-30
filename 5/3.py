#На основі попередньої функції створити наступний кусок кода:
#а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:

class NamePasswordValid(Exception):
    pass
def validate(name,password):
    if len(name) < 3 or len(name) > 50:
        raise NamePasswordValid('Довжина вашого імя має бути від 3 до 50 символів.')
    elif name.isdigit():
        raise NamePasswordValid('Ваше імя має цифри')
    elif len(password) < 8 :
        raise NamePasswordValid("Ваш пароль має менше 8 символів")
    elif not list(i for i in password if i.isdigit()):
        raise NamePasswordValid("Ваш пароль повинен мати як мінінімум одну цифру")
    else:
        return True




list_dct = [{'name':'asdada','password':'asadaffa12',
            'name':'az','password':'adassfdfs',
            'name':'dsdaf','password':'ad'}]
for data in list_dct:
    for key,val in data.items():
        print(f'Name: {key}')
        print(f'Password: {val}')
        print(f'Status: ', end='')
        try:
            if(validate(key,val)):
                print('OK')
        except NamePasswordValid as err:
            print(err)

        print('-----')