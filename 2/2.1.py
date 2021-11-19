#Елементами списку повинні бути як рядки, так і числа.
values = [1,2,'test',10,'foo']
x = ""
for i in values:
  x += str(i)
print(x)
