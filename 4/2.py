#Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток, ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна принтануть і вернуть суму, яка буде на рахунку.
a = int(input("Введіть розмір вкладу:"))
years = int(input("На скільки років: "))
percents = 10

def bank(a,years,percents):
    for _ in range(years):
        a=(1+percents/100)*a
    return a
print(bank(a,years,percents))