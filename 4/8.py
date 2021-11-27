#Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список простих чисел всередині цього діапазона.
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
nums = [1, 2, 3, 4, 5]
shift(nums, 1)
nums1 = [1, 2, 3, 4, 5]
shift(nums1, -2)
print(nums)
print(nums1)