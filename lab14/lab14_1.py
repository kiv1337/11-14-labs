original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
new_tuple = []

for el in original_tuple:
        if el % 2 != 0:
            new_tuple.append(el)

with open("мусор/lab14_1.txt", "w", encoding="utf-8") as file:
        file.write("Все числа: {}\n".format(original_tuple))
        file.write("Нечётные числа: {}\n".format(new_tuple))

with open("мусор/lab14_1.txt", "r", encoding="utf-8") as file:
        my_tuples = file.read()
        print(my_tuples)

