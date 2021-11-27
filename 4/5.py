#Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
n = int(input('Введіть число: '))
def sum_fib(n):
    c=1
    p=0
    s=0
    fibonacci = []
    while (c <= n):
        fibonacci += [c]
        s+=c
        c,p=c+p,c
    return fibonacci

print(sum_fib(n))
