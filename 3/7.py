#Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
def func():
    a = float(input('Введіть 1-й аргумент: '))
    b = input('Введіть знак дії "+", "-", "*" або "/": ')
    c = float(input('Введіть 2-й аргумент: '))
    if b == '+':
        d = a + c
    elif b == '-':
        d = a - c
    elif b == '*':
        d = a * c
    elif b == '/':
        if c != 0:
            d = a / c
        else:
            print("Ділення на ноль неможливо!")
    else:
        print("Неправильний знак дії")

    print(f'{a} {b} {c} = {d}')
func()
