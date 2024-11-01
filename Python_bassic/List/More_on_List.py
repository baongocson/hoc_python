"""
list.append(x): thêm giá trị x vào cuối list
list.insert(i, x): chèn giá trị x vào vị trí i
list.remove(x): xóa đi giá trị x được tìm thấy đầu tiên trong list
list.pop(): xóa giá trị cuối cùng của list
list.pop(i): xóa giá trị ở vị trí i
list.extend(iterable): thêm/mở rộng một/nhiều giá trị mới vào cuối list ban đầu 
list.clear(): xóa hết giá trị có trong list và trả về []
list.reverse(): lật ngược lại list ban đầu
list.sort(): xắp xếp list theo thứ tự tăng dần (list chỉ có chuỗ thì theo thứ tự bảng chữ cái)
list.sort(reverse=true): xắp xếp list theo thứ tự giảm dần

list[i] = x: thay thế giá trị x vào vị trí i 
biến = list.count(x): đếm giá trị x xuất hiện mấy lần trong list (do nó có giá trị trả về nên cần phải có 1 nới để lưu trữ giá trị đó vì thế ta cần phải gán nó vào một biến)
biến = len(list): trả về độ dài của list
biến = list.index(x): trả về vị trí/chỉ số của giá trị x trong list
"""

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits_new = ["chilli", "tomato"]

print(fruits) #pear: quả lê
print(fruits_new)

print(fruits.count('apple')) #2

print(len(fruits)) #7

fruits.append("mango")
print(fruits)
#['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'mango']

fruits.insert(3, "jackfruit") #jackfruit: trái mít
print(fruits)
#['orange', 'apple', 'pear', 'jackfruit', 'banana', 'kiwi', 'apple', 'banana', 'mango']

fruits.remove("banana")
print(fruits)
#[orange', 'apple', 'pear', 'jackfruit', 'kiwi', 'apple', 'banana', 'mango']

fruits.pop()
print(fruits)
#['orange', 'apple', 'pear', 'jackfruit', 'kiwi', 'apple', 'banana']

fruits.extend(fruits_new) # == fruits.extend("chilli", "tomato")
print(fruits)
#['orange', 'apple', 'pear', 'jackfruit', 'kiwi', 'apple', 'banana', 'chilli', 'tomato']

fruits.reverse()
print(fruits)
#['tomato', 'chilli', 'banana', 'apple', 'kiwi', 'jackfruit', 'pear', 'apple', 'orange']

fruits.sort()
print(fruits)
#['apple', 'apple', 'banana', 'chilli', 'jackfruit', 'kiwi', 'orange', 'pear', 'tomato']

fruits.sort(reverse=True)
print(fruits)
#['tomato', 'pear', 'orange', 'kiwi', 'jackfruit', 'chilli', 'banana', 'apple', 'apple']

fruits.clear()
print(fruits)
