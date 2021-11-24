#Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя
def foo(in_str):
    if len(in_str) > 50:
        print('Geekhub')
    elif len(in_str) < 30:
        s = 0
        new_str = ''
        for ch in in_str:
            if ch.isdigit():
                s += int(ch)
            else:
                new_str += ch
        print(s)
        print(new_str)
    else:
        print(len(in_str))
        print(len([i for i in in_str if i.isdigit()]))
        print(len([i for i in in_str if i.isalpha()]))


s = 'f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345'
foo(s)
s = 'f98neroi4nr0c3n30irn03ien3c0rfekdno400we'
foo(s)
s = '4nr0'
foo(s)
