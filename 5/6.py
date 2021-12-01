#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#P.S. Повинен вертатись генератор.
#P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
def my_range(start,stop=0,step=1):
    while start<stop:
        yield start
        start += step
    if stop<start:
        stop += 1
for i in my_range(1,20,8):
    print(i)
