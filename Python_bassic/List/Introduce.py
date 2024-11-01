# "name List" = []
'''
mỗi giá trị trong list ngăn cách nhau bởi dấu phẩy
một list có thể chưa nhiều kiểu dữ liệu 
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#chỉ số    0  1  2    3  4
#chỉ số   -5 -4 -3   -2 -1
numbers = [1, 2, 3.5, 4, 5,] #chỉ số của list luôn bắt đầu ở vị trí 0
numbers[0] = 24 #thay thế giá trị đầu tiên thành giá trị mới sau =

print(numbers)
print(type(numbers)) #class 'list'
print(numbers) # [1, 2, 3.5, 4, 5]
print(numbers[0]) #in ra giá trị ở vị trí đầu tiên 
print(numbers[-1]) #in ra giá trị ở vị trí cuối cùng


