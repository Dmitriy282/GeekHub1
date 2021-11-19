#Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
data = {'a':100,'b':200,'c':200}
result = {}

for key,value in data.items():
    if value not in result.values():
        result[key] = value

print(result)
