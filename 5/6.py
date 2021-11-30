#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#P.S. Повинен вертатись генератор.
#P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def my_range(start,stop,step=1):
    x = start
    while x<stop:
        yield x
        x += step
for i in my_range(2,9,5):
    x = []
    x.append(i)
    print(x)