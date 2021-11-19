#Написати скрипт, який видалить пусті елементи із списка. 
data = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
list = []
for i in data:
  if i:
     list.append(i)
print(list)
