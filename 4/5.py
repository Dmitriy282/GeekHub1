#Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
def fib(n):
    if (n==1 or n==2):
        return 1
    elif n==0:
        return 0
    return fib(n-2)+fib(n-1)

[print(fib(n)) for n in range (int(input("Введіть число: ")))]
