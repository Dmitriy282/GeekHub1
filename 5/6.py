#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#P.S. Повинен вертатись генератор.
#P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def my_range(start,stop=0,step=1):
    if start < stop:
        while start<stop:
            yield start
            start += step
    else:
        while stop < start:
            yield stop
            stop+=1
for i in my_range(1,10,3):
    print(i)


