#Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#- ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#  - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#  - щось своє :)
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
validate('swsfdsgegrgcsc','456')