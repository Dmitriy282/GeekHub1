#Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
#-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
#-  Повиннi опрацювати такi умови:
#-  x > y;       вiдповiдь - х бiльше нiж у на z
#-  x < y;       вiдповiдь - у бiльше нiж х на z
#-  x == y.      вiдповiдь - х дорiвнює z
def construct():
    x = int(input("Введіть число X: "))
    y = int(input("Введіть число Y: "))
    print('X=' + str(x))
    print('Y=' + str(y))
    if x < y:
        z = x - y
        print("у бiльше нiж х на z")
        print('Z=' + str(z))
    elif x > y:
        z = x - y
        print("х бiльше нiж у на z")
        print('Z=' + str(z))
    else:
        x = y
        print("х дорiвнює z")


construct()
