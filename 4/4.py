#Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
lower = int(input("Введіть початок діапазону: "))
upper = int(input("Введіть кінець діапазону: "))
def prime_list(lower,upper):
    for num in range(lower, upper):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            print(num)
print(prime_list(lower,upper))