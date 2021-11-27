#Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
n = int(input("Введіть число:"))
def fib(n):
    if (n==1 or n==2):
        return 1
    return fib(n-2)+fib(n-1)

print(fib(n))