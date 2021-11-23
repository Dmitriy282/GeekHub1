#Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
def season():
    month = int(input("Введіть номер місяця: "))
    numbers = [[12, 1, 2], [3, 4, 5],
             [6, 7, 8], [9, 10, 11]]

    if month in numbers[0]:
        print("Зима")
    elif month in numbers[1]:
        print("Весна")
    elif month in numbers[2]:
        print("Літо")
    elif month in numbers[3]:
        print("Осінь")
    else:
        print("Неправильний номер місяця")

        return month
season()