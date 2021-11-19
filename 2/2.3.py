#Написати скрипт, який видалить пусті елементи із списка. 
list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]

for i in list:
  if i is True:
     list.append(i)
print(list)