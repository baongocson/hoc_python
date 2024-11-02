"""
set được tạo bởi cặp dấu ngoặc nhọn {}, ko thể chứa những phần tử trùng lặp
set ko có thứ tự nên không thể truy cập vào chỉ số/ vị trí của các giá trị
set được sử dụng khi so sánh 2 hay nhiều tập hợp có điểm chung
set dùng để check những dòng trùng ở các file vì nó nhanh hơn
"""

set1 = set()

set1.add(10)
set1.update([1, 2, 4])
set1.remove(10)
set2 = set1.copy()
print(set1) 

print(set1 is set2) #False 
print(set1 == set2) #True

set1.clear()
print(set1)

set3 = {1, 2, 3, 4}
# set3.add([4, 5]) ---> TypeError: unhashable type: 'list'
set3.add("kraken")
print(set3)

