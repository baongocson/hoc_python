#and or not 
# <; >; <=; >=; ==
#0 là False. != 0 là True
#ctrl + shift + L: phím tắt chọn nhiều từ giống nhau 
#ctrl + D: phím tắt chọn nhiều từ giống nhau sau dòng được chọn
#ctrl + /: chuyển một dòng thành comment

print(.5 > 1) #False: .5 = 0.5

"""falsy = 0; 0.0; 0j / None: no value"""
print(bool(0.0)) #False
print(bool(0j)) #False
print(bool(None)) #False
print(bool(0)) #False
print(bool(1)) #True

"""or: khi trong điều kiện chỉ cần có 1 dữ kiện đúng là xuất ra giá trị True"""
print(True or True) #True
print(True or False) #True
print(False or False) #False
print(False or True) #True
print(0 or 1) #1
print(1 or 2) #1: trả về giá trị đúng đầu tiên
"""and: khi trong điều kiện tất cả dữ kiện đúng thì mới trả về giá trị True"""
print(True and True) #True
print(True and False) #False
print(False and False) #False
print(False and True) #False
print(0 and 1) #0
print(1 and 2) #2: giá trị đầu đùng thì trả về giá trị hai

"""not: trả về giá trị ngược lại"""
print(not True)
print(not False)

"""
set: set()
list: []
dict: {}
tupel: ()
empty string: "" , ''
"""
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(set())) #False
print(bool('')) #False
print(bool("")) #False
