#for: vòng lặp

print("-----------------------------------------------------")

#duyệt qua danh sách 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("-----------------------------------------------------")

job_list = ['Data Engineer', 'Senior Data Engineer', 'Data Analyst - Financial Reporting']
# Tạo danh sách rỗng để lưu các công việc liên quan đến Data Analyst
analyst_list = []
# Dùng vòng lặp for để duyệt qua job_list
for job in job_list:
    if 'Senior' in job:
        analyst_list.append(job)
# In ra danh sách các công việc Data Analyst
print(analyst_list)

print("-----------------------------------------------------")

#Vòng lặp với range() mặc định (start = 0)
for i in range(5):
    print(i)

#Vòng lặp với range(start, stop)
for i in range(2, 7):
    print(i)

#Vòng lặp với range(start, stop, step)
for i in range(1, 10, 2):
    print(i)

#Vòng lặp range() với bước nhảy âm
for i in range(10, 0, -2):
    print(i)

print("-----------------------------------------------------")

#Sử dụng range() để duyệt ngược một danh sách
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

#Duyệt các chỉ số chẵn của danh sách với range()
numbers = [10, 20, 30, 40, 50, 60]
for i in range(0, len(numbers), 2):
    print(numbers[i])


