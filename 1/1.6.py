def is_group_member(datagroup, n):
   return n in datagroup

print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))