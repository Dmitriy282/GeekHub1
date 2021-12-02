#Програма-світлофор.
#Створити програму-емулятор світлофора для авто і пішоходів.
#Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
#Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
import time
 
while True:
    for i in range(4):
        print('Red      Green')
        time.sleep(1)
 
    for i in range(2):
        print('Yellow   Green')
        time.sleep(1)
 
    for i in range(4):
        print('Green    Red')
        time.sleep(1)
 
    for i in range(2):
        print('Yellow   Red')
        time.sleep(1)
