dict = {"cat" : "bob", "dog": 23, 19: 18, 90:"fish"}
print(dict)
total = 0
for key, value in dict.items():
    # print(key, value)
    result = isinstance(value, int)
    if result == True:
        total += value
print(total)
        