#Написати скрипт, який видалить пусті елементи із списка. 
x = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
result = []
for i in x:
  if i:
     result.append(i)
print(result)
