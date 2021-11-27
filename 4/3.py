#Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
n = int(input("Введіть число від 0 до 1000: "))

def is_prime(n):
    if 0<n<1000:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        print("Вказане число невірно")
print(is_prime(n))
