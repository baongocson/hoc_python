"""
list slicing sẽ trả về cho ta một new list
cú pháp: new_list = list[satrt:end:step]
new_list sẽ không nhận giá trị ở vị trí end
step mặc định của nó là 1
"""

#             0         1         2            3
movies = ["doremon", "conan", "pokemon", "dragon_ball"]
new1_movies = movies[0:2:1] # lấy từ 0 cho đến 2 bước nhảy là 1
new2_movies = movies[:2] # lấy từ 0 cho đến 2 bước nhảy là 1
new3_movies = movies[1:] # lấy từ 1 cho đến hết 
new4_movies = movies[:] #==movies.copy # lấy từ 0 cho đến hết
new5_movies = movies[:-1] # lấy từ không cho đến sát cuối 
new6_movies = movies[1:-1] # lấy giá trị ở giữa loại bỏ đi gí trị đầu và cuối
new7_movies = movies[::-1] # lật ngược lại cái list ban đầu

print(new1_movies)
print(new2_movies)
print(new3_movies)
print(new4_movies)
print(new5_movies)
print(new6_movies)
print(new7_movies)