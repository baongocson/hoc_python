"""
copy list
"""

list1 = [1, 2, 3, 4]
list2 = list1 

print(id(list1), id(list2)) #2350797381696 2350797381696
print(list1 is list2) #list1 có phải là list2 không
print(list1 == list2)

#cái khác khi sử dụng copy
list3 = [5, 6, 7, 8]
list4 = list3.copy()

print(id(list3), id(list4)) #1837111091520 1837112819520
print(list3 is list4) #False
print(list3 == list4) #True