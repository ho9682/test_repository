data = [1, 2, 3, 4]

new_list = []
for i in data:
    new_list.append(i**2)

print(new_list)

new_list_2 = [x**2 for x in data]
print(new_list_2)
