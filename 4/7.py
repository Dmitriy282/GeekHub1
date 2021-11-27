#Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
MyList = [1, 3, 3, 1, 1, 1, 1, 'g', (1, "a", 2), (1, "a", 2)]
def analysis(MyList):

    duplicate_dict = {i: MyList.count(i) for i in MyList}
    print(duplicate_dict)

analysis(MyList)