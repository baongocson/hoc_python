"""
Tuple: là một bộ giá trị, một cấu trúc dữ liệu có kí tự, có thể chứa những phần tử trùng lặp
được đặt trong dấu ()
Tuple khác list ở điểm không thể thay đổi bản thân nó hoặc các giá trị có trong nó 
"""

tup1 = 1, 2, 3, 7,
tup2 = (1, 4, 8)
tup3 = 9,
tup4 =(5,)

print(type(tup1), tup1) #<class 'tuple'> (1, 2, 3, 7)
print(type(tup2), tup2) #<class 'tuple'> (1, 4, 8)
print(type(tup3), tup3) #<class 'tuple'> (9,)
print(type(tup4), tup4) #<class 'tuple'> (5,)

#các hàm
tup1.__add__(tup4) #trả về 1 tup new
print(tup1.__add__(tup4))

print(tup1.index(2)) # in ra vị trí của giá trị 2 trong tup1

tup3 += tup1
tup4 += (1, 2, 3, 7)
print(tup3)
print(tup4)