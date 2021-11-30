#Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.

def gen(x):
    ind = 0
    while True:
        try:
            yield x[ind]
        except IndexError:
            ind = 0
            yield x[ind]
        ind += 1


test = gen(['1', '2', '3'])

print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))