#Написати скрипт, який видалить пусті елементи із списка. 
list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
result = []
for i in list:
  if i:
     result.append(i)
print(result)
