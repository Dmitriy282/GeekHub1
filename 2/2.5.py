#Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
data = {'a':100,'b':200,'c':200}
c=list(data.values())
print(c)
b=list(dict.fromkeys(c))
print(b)