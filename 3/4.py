#Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
import math
def func():
    def students():
        print("Hello students!")
    students()

    def square():
        a = float(input("Введіть довжину сторони квадрата: "))
        s = a ** 2
        S = "Площа квадрата: " + str(s)
        print(S)
    square()
    def theorem_Pythagorean():

        a = float(input("Введіть довжину першого катета прямокутного трикутника: "))
        b = float(input("Введіть довжину другого катета прямокутного трикутника: "))
        c = (a**2) + (b**2)
        d = math.sqrt(c)
        print("Гіпотенуза дорівнює: "+ str(d))
    theorem_Pythagorean()

func()
