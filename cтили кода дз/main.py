#Задача "Нули ничто, отрицание недопустимо!":
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
quantity = len(my_list)
a = 0
while a < quantity:
    if my_list [a] == 0:
        a = a + 1
        continue
    elif my_list [a] > 0:
        print(my_list[a])
        a = a + 1
    elif my_list [a] < 0:
        break