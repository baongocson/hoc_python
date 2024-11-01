"""
str + str = True
str + int = False
"""
"""f-string: nhúng một giá trị vào chỗ mình muốn nó xuất hiện 
cú pháp là: print(f"chuoi{bien}")
"""
# print("{}".format()): truyền giá trị từ dấu () vào dấu {}

age = 18
# I am 18 
# print("I am " + 18) -> tuypeError
age_as_str = str(age)
print("I am " + age_as_str)
print("I am " + str(age))
print(f"I am {age}")
print("I am {}".format(age))

